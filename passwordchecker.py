import re

def check_password_complexity(password):
    """
    Checks the complexity of a password.

    Args:
        password (str): The password to check.

    Returns:
        dict: A dictionary containing the results of the complexity check.
    """
    complexity_criteria = {
        "length": len(password) >= 8,
        "uppercase": re.search(r'[A-Z]', password) is not None,
        "lowercase": re.search(r'[a-z]', password) is not None,
        "digit": re.search(r'\d', password) is not None,
        "special_char": re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None,
    }

    return complexity_criteria


def main():
    password = input("Enter a password to check its complexity: ")
    complexity_results = check_password_complexity(password)

    print("\nPassword Complexity Check Results:")
    print(f"Length (minimum 8 characters): {'Pass' if complexity_results['length'] else 'Fail'}")
    print(f"Contains uppercase letter: {'Pass' if complexity_results['uppercase'] else 'Fail'}")
    print(f"Contains lowercase letter: {'Pass' if complexity_results['lowercase'] else 'Fail'}")
    print(f"Contains digit: {'Pass' if complexity_results['digit'] else 'Fail'}")
    print(f"Contains special character: {'Pass' if complexity_results['special_char'] else 'Fail'}")

    if all(complexity_results.values()):
        print("\nYour password is strong!")
    else:
        print("\nYour password is weak. Please improve its complexity.")


if __name__ == "__main__":
    main()