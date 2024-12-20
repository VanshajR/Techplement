import argparse
import secrets
import string

def generate_password(length=15, include_upper=True, include_lower=True, include_digits=True, include_special=True, exclude_brackets=True):
    chars = ''
    if include_upper:
        chars += string.ascii_uppercase
    if include_lower:
        chars += string.ascii_lowercase
    if include_digits:
        chars += string.digits
    if include_special:
        chars += string.punctuation.replace('[', '').replace(']', '').replace('{', '').replace('}', '').replace('(', '').replace(')', '').replace('<', '').replace('>', '').replace('|', '').replace('"', '').replace("'", '').replace('\\', '').replace('/', '').replace('`', '').replace('~', '')

    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description='''This program was made by Vanshaj Raghuvanshi. Use it to generate random passwords.''')
    parser.add_argument('-l', '--length', type=int, default=20, help='Length of the password')
    parser.add_argument('--no-upper', action='store_false', dest='upper', help='Exclude uppercase letters')
    parser.add_argument('--no-lower', action='store_false', dest='lower', help='Exclude lowercase letters')
    parser.add_argument('--no-digits', action='store_false', dest='digits', help='Exclude digits')
    parser.add_argument('--no-special', action='store_false', dest='special', help='Exclude special characters')
    parser.add_argument('--no-brackets', action='store_false', dest='brackets', help='Exclude brackets')
    args = parser.parse_args()

    password = generate_password(length=args.length, include_upper=args.upper, include_lower=args.lower, include_digits=args.digits, include_special=args.special, exclude_brackets=args.brackets)
    print(password)

if __name__ == '__main__':
    main()
