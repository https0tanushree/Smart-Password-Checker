import re

def check_password(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Include at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    return score, suggestions


password = input("Enter your password: ")

score, suggestions = check_password(password)

print("\nPassword Strength Score:", score, "/ 5")

if score <= 2:
    print("Strength: Weak")
elif score in [3, 4]:
    print("Strength: Moderate")
else:
    print("Strength: Strong")

if suggestions:
    print("\nSuggestions to improve:")
    for s in suggestions:
        print("-", s)
