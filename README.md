\# Task 3: Secure Coding Review Assessment



\## Project Overview

This project consists of a manual code review performed on a Python web application to discover, analyze, and mitigate common application security vulnerabilities.



\## Vulnerability Assessment Report



\### 1. SQL Injection (SQLi)

\- \*\*File Affected:\*\* `vulnerable\_app.py`

\- \*\*Risk Level:\*\* High

\- \*\*Description:\*\* The login feature inserts raw strings directly into the SQL command. An attacker can manipulate inputs to log in without a valid password.

\- \*\*Remediation:\*\* Swapped dynamic string syntax for parameterized statements using database placeholders (`?`) in `secure\_app.py`.



\### 2. Reflected Cross-Site Scripting (XSS)

\- \*\*File Affected:\*\* `vulnerable\_app.py`

\- \*\*Risk Level:\*\* Medium

\- \*\*Description:\*\* The profile page reflects user parameters into the template without sanitization, permitting external JavaScript injection attacks.

\- \*\*Remediation:\*\* Sanitized input parameters utilizing Python's native `html.escape()` utility in `secure\_app.py`.

