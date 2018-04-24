from flask import Flask

app = Flask(__name__)

@app.route('api/v1/auth/signup', methods = ['POST'])
def signup():
	pass

@app.route('api/v1/auth/login', methods = ['POST'])
def login():
	pass

@app.route('api/v1/meals', methods = ['GET'])
def get_all_meals():
	pass

@app.route('api/v1/meals', methods = ['POST'])
def add_meal():
	pass

@app.route('api/v1/meals/<mealId>', methods = ['PUT'])
def modify_meal():
	pass

@app.route('api/v1/meals/<mealId>', methods = ['DELETE'])
def delete_meals():
	pass

@app.route('api/v1/menu', methods = ['POST'])
def setup_menu():
	pass

@app.route('api/v1/menu', methods = ['GET'])
def get_menu():
	pass

@app.route('api/v1/orders', methods = ['POST'])
def make_order():
	pass

@app.route('api/v1/orders/<orderId>', methods = ['PUT'])
def modify_order():
	pass

@app.route('api/v1/orders', methods = ['GET'])
def get_all_orders():
	pass

if __name__ == "__main__":
	app.run(debug = True)