from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Change this key for security

# User credentials for demo purposes
users = {
    "admin": "password",
    "user1": "password1"
}

@app.route('/')
def home():
    if 'username' in session:
        return render_template("dashboard.html", username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        return "Invalid credentials. Please try again."
    return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/scale', methods=['POST'])
def scale():
    if 'username' not in session:
        return redirect(url_for('login'))
    replicas = request.form['replicas']
    os.system(f"kubectl scale deployment cpu-cluster --replicas={replicas}")
    return f"Scaled CPU cluster to {replicas} replicas. <br><a href='/'>Back to Dashboard</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
