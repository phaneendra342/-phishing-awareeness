# CodeAlpha_Secure_Coding_Review

## 📌 Project Overview
This project consists of a manual code review performed on a Python web application to discover, analyze, and mitigate common application security vulnerabilities. It demonstrates the security differences between an unvalidated, insecure application and a hardened, secure application.

---

## 🔍 Vulnerability Assessment Report

### 1. SQL Injection (SQLi)
* **File Affected:** `vulnerable_app.py`[cite: 1]
* **Risk Level:** High[cite: 1]
* **Description:** The login feature inserts raw user input strings directly into the SQL command execution path[cite: 1]. An attacker can manipulate these inputs to bypass authentication mechanics and log in without a valid password[cite: 1].
* **Remediation:** Swapped dynamic string concatenation syntax for parameterized statements using database placeholders (`?`) inside `secure_app.py`[cite: 1]. This forces the database engine to treat inputs strictly as literal values, never as executable code[cite: 1].

### 2. Reflected Cross-Site Scripting (XSS)
* **File Affected:** `vulnerable_app.py`[cite: 1]
* **Risk Level:** Medium[cite: 1]
* **Description:** The profile page reflects user parameters into the template without sanitization, permitting external JavaScript injection attacks directly into the browser session[cite: 1].
* **Remediation:** Sanitized input parameters utilizing Python's native `html.escape()` utility inside `secure_app.py`[cite: 1]. This neutralizes malicious script tags by converting special characters into harmless plain text HTML entities[cite: 1].

---

## 🛠️ How it Works

### 🚫 The Vulnerable Application (`vulnerable_app.py`)
* Uses direct string formatting for database queries: `query = f"SELECT * FROM users WHERE username = '{username}'..."`[cite: 1]
* Renders untrusted text parameters raw into HTML templates[cite: 1].
* Runs with development features fully exposed (`debug=True`)[cite: 1].

### 🛡️ The Secure Application (`secure_app.py`)
* Enforces parameterized binding queries: `query = "SELECT * FROM users WHERE username = ? AND password = ?"`[cite: 1]
* Uses context-aware output encoding to sanitize input strings: `safe_name = html.escape(name)`[cite: 1]
* Hardened environment behavior by switching off development flags (`debug=False`)[cite: 1].

---

## 🚀 How to Run and Test

1. **Run the Insecure Server:**
   ```bash
   python vulnerable_app.py
