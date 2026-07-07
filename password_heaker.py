import re

password = input("Enter your password: ")

score = 0

# Check password length
if len(password) >= 8:
    print("Password has at least 8 characters")
    score += 1
else:
    print("✗ Password should have at least 8 characters")

if re.search(r"[A-Z]", password):
    print("Contains uppercase letter")
    score += 1
else:
    print("✗ Missing uppercase letter")


if re.search(r"[a-z]", password):
    print(" Contains lowercase letter")
    score += 1
else:
    print("Missing lowercase letter")


if re.search(r"[0-9]", password):
    print("Contains number")
    score += 1
else:
    print("Missing number")

if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    print("Contains special character")
    score += 1
else:
    print("✗ Missing special character")

print("\nScore:", score, "/5")
if score == 5:
    print("Strength: Very Strong ")
elif score == 4:
    print("Strength: Strong")
elif score == 3:
    print("Strength: Medium")
elif score == 2:
    print("Strength: Weak")
else:
    print("Strength: Very Weak")