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

@app.route('/Dashboard/create_user.html')
def create_user_content():
  return render_template('/Dashboard/create_user.html', title = 'Create user Page', appName = appName)

@app.route('/Dashboard/sales_report.html')
def sales_report_content():
  response = requests.get('http://127.0.0.1:8000/get_sales_report')
  data = response.json()
  return render_template('/Dashboard/sales_report.html', title = 'Sales Report Page', sales_report = data)

@app.route('/Dashboard/inventory_management.html')
def inventory_management_content():
  return render_template('/Dashboard/inventory_management.html', title = 'Inventory Management Page', appName = appName)

if __name__ == '__main__':
    app.run(debug=True)