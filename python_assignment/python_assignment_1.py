import re
import getpass

criteria = """
⭐️ Minimum length: The password should be at least 8 characters long.

⭐️ Contains both uppercase and lowercase letters.

⭐️ Contains at least one digit (0-9).

⭐️ Contains at least one special character (e.g., !, @, #, $, %).
"""

def check_password_strength(password):
    """
    Check the strength of the given password based on the specified criteria.
    
    Parameters:
        password (str): The password string to check.
        
    Returns:
        bool: True if the password meets all criteria, False otherwise.
    """
    # Check minimum length of 8 characters
    if len(password) < 8:
        return False
    
    # Check for both uppercase and lowercase letters
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return False
    
    # Check for at least one digit
    if not any(char.isdigit() for char in password):
        return False
    
    # Check for at least one special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    
    return True

if __name__ == "__main__":
    # user_password = input("Enter your password: ")
    user_password = getpass.getpass("Please enter your password: ")
    
    is_strong = check_password_strength(user_password)
    
    if is_strong:
        print("Your password is strong.")
    else:
        print(f"Your password is weak. Please make sure it meets all the criteria \n\n{criteria}")
