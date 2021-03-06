import requests
import hashlib


def request_pawned_passwords(pass_fragment):
    url = 'https://api.pwnedpasswords.com/range/' + pass_fragment
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching. {res.status_code}')
    return res


def read_potential_matches(response, tail):
    hashes = (line.split(':') for line in response.text.splitlines())
    for potential_hash, count in hashes:
        if potential_hash == tail:
            return count
    return 0


def hash_password(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = sha1password[:5], sha1password[5:]
    response = request_pawned_passwords(first5)
    return read_potential_matches(response, tail)


def check_password(password):
    compromised_count = hash_password(password)
    if compromised_count:
        return f'Oh no. Your password was compromised {compromised_count} times!'
    else:
        return 'No compromises. All good!'
