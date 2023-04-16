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
    items = [
    {
      "name": "Chicken Pizza",
      "price": 10
    },
    {
      "name": "Cheese Pizza",
      "price": 15
    },
    {
      "name": "Chicken Burger",
      "price": 25
    },
    {
      "name": "Cheese Burger",
      "price": 20
    }
  ]
    return render_template('/mainPage/index.html', title = 'Home Page', appName = appName, data = data, menu_items = items)

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
    print(data)
    items = [
    {
      "name": "Chicken Pizza",
      "price": 10,
      "id" : 1
    },
    {
      "name": "Cheese Pizza",
      "price": 15,
      "id" : 2
    },
    {
      "name": "Suchi",
      "price": 25,
      "id": 3
    },
    {
      "name": "Pasta",
      "price": 20,
      "id": 4
    },
    {
      "name": "Mutton Soup",
      "price": 10,
      "id": 5
    },
    {
      "name": "Hyderabad Briyani",
      "price": 15,
      "id": 6
    },
    {
      "name": "Sweet Corn Soup",
      "price": 25,
      "id": 7
    },
    {
      "name": "Afghani Chicken",
      "price": 20,
      "id": 8
    },
     {
      "name": "Dragon Chicken",
      "price": 10,
      "id": 9
    },
    {
      "name": "Falooda",
      "price": 15,
      "id": 10
    },
    {
      "name": "Cheese cake",
      "price": 25,
      "id": 11
    },
    {
      "name": "Wine",
      "price": 20,
      "id": 12
    }
  ]
    return render_template('/Order/order.html', title = 'Home Page', appName = appName, data = data, menu_items = items)

if __name__ == '__main__':
    app.run(debug=True)