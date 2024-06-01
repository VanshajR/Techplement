# Password Generator

This command-line tool generates random passwords with customizable length and complexity.

## Technologies Used

- **Python**: The programming language used to develop the password generator.
- **Argparse**: Python module used to parse command-line arguments and options.
- **Secrets Module**: Python module used for generating cryptographically strong random numbers.

## Command Usage

To use the password generator, run the `password_generator.py` script with the desired options.

### Command Syntax

python password_generator.py [options]

### Options

- `-l`, `--length`: Specifies the length of the password. Default is 20.
- `--no-upper`: Exclude uppercase letters from the password.
- `--no-lower`: Exclude lowercase letters from the password.
- `--no-digits`: Exclude digits from the password.
- `--no-special`: Exclude special characters from the password.
- `--no-brackets`: Exclude brackets (`[`, `]`, `{`, `}`, `(`, `)`, `<`, `>`) from the password.

## Example

### Generate a password with default options:
python password_generator.py

### Generate a password with a length of 30 characters, excluding uppercase letters and special characters:

python password_generator.py -l 30 --no-upper --no-special

### For more information and advanced usage, refer to the command-line help:

python password_generator.py --help


## NOTE: python3 can be used instead of python, -l is lowercase 'L'
