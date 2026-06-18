# 🔐 Password Strength Analyzer

A Python-based Password Strength Analyzer developed as part of a Cyber Security Internship. This project evaluates the strength of user passwords based on security rules, provides suggestions to improve weak passwords, securely stores password hashes using SQLite, and detects password reuse.

---

## 📌 Features

- Analyze password strength
- Score passwords out of 100
- Classify passwords as Weak, Medium, Strong, or Very Strong
- Detect common passwords
- Suggest improvements for weak passwords
- Generate strong password suggestions
- Securely store password hashes using SQLite
- Detect previously used passwords

---

## 🛠️ Technologies Used

- Python 3
- SQLite
- hashlib
- random
- string
- re

---

## 📂 Project Structure

```
Password-Strength-Analyzer/
│
├── src/
│   ├── password_strength_analyzer.py
│   └── password_history.db
│
├── README.md
└── requirements.txt
```

---

## ▶️ How to Run

1. Open the project in VS Code.
2. Open the terminal.
3. Navigate to the source folder:

```bash
cd src
```

4. Run the program:

```bash
python password_strength_analyzer.py
```

5. Enter a password when prompted.

---

## 📊 Sample Output

```
Enter a password: MySecure@Password2025

Password Length : 21
Score           : 100/100
Strength        : Very Strong

Password hash saved securely.
```

---

## 🎯 Learning Outcomes

- Password security analysis
- Password hashing using SHA-256
- SQLite database integration
- Regular expressions for password validation
- Secure coding practices
- Python programming fundamentals

---

## 🚀 Future Improvements

- Graphical User Interface (GUI)
- Password breach detection
- Password entropy calculation
- Password history management
- Export security reports

---

## 👩‍💻 Author

**Bhumika Patil**

Developed as part of the **Cyber Security Internship**.

