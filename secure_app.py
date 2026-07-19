from flask import Flask, request, render_template_string
import sqlite3
import html

app = Flask(__name__)

@app.route('/')
def index():
    return '''<h1>Welcome</h1>
<p>Use <a href="/profile?name=Guest">/profile</a> or submit a POST to <code>/login</code>.</p>'''

# REMEDIATION 1: Parameterized Queries (Fixes SQL Injection)
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # SECURE: Placeholders (?) treat input strictly as literal values, never code
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    
    if user:
        return "Login Successful!"
    return "Invalid Credentials"

# REMEDIATION 2: HTML Output Encoding (Fixes XSS)
@app.route('/profile')
def profile():
    name = request.args.get('name', 'Guest')
    
    # SECURE: html.escape neutralizes malicious script tags
    safe_name = html.escape(name)
    
    html_content = f"<h1>Welcome to your profile, {safe_name}!</h1>"
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=False) # SECURE: Turned off debug mode