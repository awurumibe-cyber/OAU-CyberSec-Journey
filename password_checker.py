def check_password(pwd):
    # Check if password meets basic strength metrics
    has_len = len(pwd) >= 8
    has_digit = any(c.isdigit() for c in pwd)
    has_upper = any(c.isupper() for c in pwd)
    
    if has_len and has_digit and has_upper:
        return "STRONG PASSWORD"
    else:
        return "WEAK PASSWORD (Must be 8+ chars, have a number, and an uppercase letter)"

# Prompt the user for input
user_input = input("Enter a password to test for compliance: ")
print(check_password(user_input))