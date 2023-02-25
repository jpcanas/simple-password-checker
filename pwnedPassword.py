import requests
import hashlib


def request_api_data(query_char='abcde'):
    '''function to connect on pwnedpassword API'''
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        print(f'Error fetching: {res.status_code}, check your api')
        return False
    else:
        return res


def get_pass_leaks_count(hashes, hash_to_check):
    '''Compare the given password (in sha1 hash form)\n
    to the response by pwnedpassword API\n
    Returns the number of times the given password has been hacked'''
    my_hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in my_hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    '''
    Encrypting the given password using sha1 hash generator\n
    Returns sha1 hash value and passes to get_pass_leaks_count() as argument\n
    parameter: pwned_api_check(str=any)
    '''
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char = sha1password[:5]
    tail_char = sha1password[5:]
    response = request_api_data(first5_char)
    return get_pass_leaks_count(response, tail_char)


def password_Check(input_pass):
    count = pwned_api_check(input_pass)
    if count:
        return f'Oh no!, This password has been seen {count} times... You should change it'
    else:
        return 'Good news! The password you have entered has not been hacked'


# if __name__ == '__main__':
#     inputPassword = input('Please input the password to check: ')
#     password_Check(inputPassword)