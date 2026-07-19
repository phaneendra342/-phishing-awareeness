from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return '''<h1>Welcome</h1>
<p>Use <a href="/profile?name=Guest">/profile</a> or submit a POST to <code>/login</code>.</p>'''

# VULNERABILITY 1: SQL Injection (SQLi)
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # DANGEROUS: Direct string insertion allows SQL manipulation
    query = f"SELECT * FROM users WHERE username = '{username}' and password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    
    if user:
        return "Login Successful!"
    return "Invalid Credentials"

# VULNERABILITY 2: Reflected Cross-Site Scripting (XSS)
@app.route('/profile')
def profile():
    name = request.args.get('name', 'Guest')
    
    # DANGEROUS: Rendering raw user input allows malicious script execution
    html_content = f"<h1>Welcome to your profile, {name}!</h1>"
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)