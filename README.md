# Password Strength Analyzer

## Internship Project

**Project:** Password Strength Analyzer  
**Domain:** Cybersecurity / Python  
**Author:** Srujan Kumar M

## 1. Project Overview

Password Strength Analyzer is a simple Python cybersecurity project that evaluates the strength of a password using common security rules.

The application checks password length, character variety, common-password usage, and repeated characters. It gives the user a strength score and practical suggestions for improving weak passwords.

The project also generates a stronger random password when the entered password is weak or medium.

## 2. Objectives

- Understand basic password-security principles.
- Implement password validation using Python.
- Use regular expressions for character checks.
- Provide useful security feedback to users.
- Generate random passwords using Python's `secrets` module.
- Practice clean project organization and unit testing.

## 3. Features

- Password length validation
- Lowercase character check
- Uppercase character check
- Number check
- Special-character check
- Common weak-password detection
- Repeated-character detection
- Strength score
- Improvement suggestions
- Secure random password generation
- Hidden password input using `getpass`
- Unit tests

## 4. Technologies Used

- Python 3
- Regular Expressions (`re`)
- `getpass`
- `secrets`
- `string`
- `unittest`

No third-party Python packages are required.

## 5. Project Structure

```text
Password-Strength-Analyzer/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── src/
│   └── password_strength_analyzer.py
└── tests/
    └── test_password_strength_analyzer.py
```

## 6. How to Run

Check Python:

```bash
python --version
```

Run the application:

```bash
python src/password_strength_analyzer.py
```

Run unit tests:

```bash
python -m unittest discover -s tests -v
```

## 7. Example

```text
=============================================
       PASSWORD STRENGTH ANALYZER
=============================================
Enter your password:

Password Analysis
-------------------------
Score    : 6 / 6
Strength : Very Strong

Your password satisfies all basic checks.
```

The entered password is not printed on the screen.

## 8. Security Considerations

This project is intended for educational use. It does not store or display the entered password.

The `secrets` module is used for generating random password suggestions.

For a real authentication system, passwords should never be stored as plaintext. A modern password-hashing algorithm such as Argon2id or bcrypt should be used.

## 9. Future Improvements

- Add a graphical user interface.
- Add password entropy estimation.
- Add a larger compromised-password dataset.
- Add a web interface using Flask.
- Add a database demonstration using securely hashed passwords.
- Add CI testing with GitHub Actions.

## 10. Learning Outcomes

Through this project, the developer practices:

- Python functions
- Conditional statements
- Regular expressions
- Secure random generation
- Input handling
- Unit testing
- GitHub project organization
- Basic cybersecurity concepts
