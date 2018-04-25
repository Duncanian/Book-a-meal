from flask import Flask, request, jsonify, session
from user import User
from caterer import Caterer

app = Flask(__name__)

app.config['SECRET_KEY'] = 'super secret'

@app.route('/api/v1/auth/signup', methods = ['POST'])
def signup():
	new_user = User().signup(request.json['username'], request.json['password'], request.json['user_id'])
	return jsonify({"user" : new_user})

@app.route('/api/v1/auth/login', methods = ['POST'])
def login():
	auth = request.authorization

	log = User().login(auth.username, auth.password)
	#log = Caterer().login(auth.username, auth.password)

	return jsonify({"message" : log})

@app.route('/api/v1/auth/logout', methods = ['POST'])
def logout_user():
	logouts = User().logout()
	jsonify({"message":logouts})

@app.route('/api/v1/meals', methods = ['GET'])
def get_all_meals():
	get_meals = Caterer().get_meals()
	jsonify({"messages":get_meals})

@app.route('/api/v1/meals', methods = ['POST'])
def add_meal():
	new_meal = Caterer().post_meal(request.json['meal_id'], request.json['meal_name'], request.json['price'], request.json['category'], request.json['day'])
	return jsonify({"message":new_meal})

@app.route('/api/v1/meals/<mealId>', methods = ['PUT'])
def edit_meal(mealId):
	new_meal = Caterer().modify_meal(mealId, request.json['meal_name'], request.json['price'], request.json['category'], request.json['day'])
	return jsonify({"message":new_meal})

@app.route('/api/v1/meals/<mealId>', methods = ['DELETE'])
def delete_meals(mealId):
	delete_meal = Caterer().delete_ml(mealId)
	return jsonify({"message" : delete_meal})

@app.route('/api/v1/menu', methods = ['POST'])
def setup_menu():
	pass

@app.route('/api/v1/menu', methods = ['GET'])
def get_menu():
	pass

@app.route('/api/v1/orders', methods = ['POST'])
def make_order():
	pass

@app.route('/api/v1/orders/<orderId>', methods = ['PUT'])
def modify_order():
	pass

@app.route('/api/v1/orders', methods = ['GET'])
def get_all_orders():
	pass

if __name__ == "__main__":
	app.run(debug = True)