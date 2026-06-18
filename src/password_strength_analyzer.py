import re
import random
import string
import hashlib
import sqlite3

# -----------------------------
# Database Setup
# -----------------------------
conn = sqlite3.connect("password_history.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS password_history (
    password_hash TEXT PRIMARY KEY
)
""")
conn.commit()

# -----------------------------
# Helper Functions
# -----------------------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def password_used_before(password):
    hashed = hash_password(password)
    cursor.execute(
        "SELECT * FROM password_history WHERE password_hash=?",
        (hashed,)
    )
    return cursor.fetchone() is not None

def save_password(password):
    hashed = hash_password(password)
    try:
        cursor.execute(
            "INSERT INTO password_history VALUES (?)",
            (hashed,)
        )
        conn.commit()
    except:
        pass

def generate_strong_password():
    words = ["River", "Tiger", "Cloud", "Moon", "Coffee", "Dragon"]
    return (
        random.choice(words)
        + random.choice("!@#$%^&*")
        + random.choice(words)
        + str(random.randint(10, 99))
    )

# -----------------------------
# Password Analyzer
# -----------------------------
def analyze_password(password):
    score = 0
    feedback = []

    common_passwords = [
        "123456",
        "password",
        "password123",
        "qwerty",
        "admin",
        "welcome"
    ]

    # Length Check
    if len(password) >= 16:
        score += 30
    elif len(password) >= 12:
        score += 25
    elif len(password) >= 8:
        score += 15
    else:
        feedback.append("Password should be at least 8 characters.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 15
    else:
        feedback.append("Add uppercase letters.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 15
    else:
        feedback.append("Add lowercase letters.")

    # Numbers
    if re.search(r"\d", password):
        score += 15
    else:
        feedback.append("Add numbers.")

    # Special Characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 15
    else:
        feedback.append("Add special characters.")

    # Common Password Check
    if password.lower() in common_passwords:
        feedback.append("This is a common password.")
    else:
        score += 10

    # Repeated Character Check
    if re.search(r"(.)\1{2,}", password):
        feedback.append("Avoid repeated characters.")
        score -= 10

    # Password Reuse Check
    reused = password_used_before(password)
    if reused:
        feedback.append("Password has been used before.")
        score -= 20

    score = max(0, min(score, 100))

    # Rating
    if score >= 90:
        rating = "Very Strong"
    elif score >= 70:
        rating = "Strong"
    elif score >= 40:
        rating = "Medium"
    else:
        rating = "Weak"

    return score, rating, feedback, reused

# -----------------------------
# Main Program
# -----------------------------
password = input("Enter a password: ")

score, rating, feedback, reused = analyze_password(password)

print("\n------ PASSWORD ANALYSIS ------")
print("Password Length :", len(password))
print("Score           :", score, "/100")
print("Strength        :", rating)

if feedback:
    print("\nSuggestions:")
    for item in feedback:
        print("-", item)

if rating in ["Weak", "Medium"]:
    print("\nSuggested Strong Password:")
    print(generate_strong_password())

if not reused:
    save_password(password)
    print("\nPassword hash saved securely.")
else:
    print("\nPassword not saved because it was already used.")

conn.close()
