from flask import Flask, render_template
import requests

app = Flask(__name__,template_folder='template')

appName = "Retro Cafe"

@app.route('/')
def home():
    return render_template('/auth/index.html', title = 'Auth Page', appName = appName)

@app.route('/mainPage')
def order_page():
    response = requests.get('http://127.0.0.1:8000/get_store_details')
    data = response.json()
    print(data)
    return render_template('/mainPage/index.html', title = 'Home Page', appName = appName, data = data)

@app.route('/Profile/profile.html')
def profile_content():
  return render_template('/Profile/profile.html', title = 'Profile Page', appName = appName)

@app.route('/Dashboard/dashboard.html')
def dashboard_content():
  return render_template('/Dashboard/dashboard.html', title = 'Dashboard Page', appName = appName)

@app.route('/Order/order.html')
def order_content():
    response = requests.get('http://127.0.0.1:8000/get_store_details')
    data = response.json()
    return render_template('/Order/order.html', title = 'Home Page', appName = appName, data = data)

if __name__ == '__main__':
    app.run(debug=True)