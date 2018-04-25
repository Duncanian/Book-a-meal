from flask import session
from caterer import Caterer

class User(object):
	"""docstring for Caterer"""
	users = [{'username' : 'user', 'password' : '12345', 'user_id' : 123, 'admin' : False}]
	def __init__(self):
		self.output = {}

	def signup(self, username, password, user_id):
		#Introduce a type check
		#Here
		if username == '' or password == '' or user_id == '':
			return 'Please enter all the details'

		if not isinstance(username, str) or not isinstance(password, str):
			return 'Please enter a string value for username and password'
		if not isinstance(user_id, int):
			return 'User Id should be an integer!'

		#Should validate the input data types

		userz = [user1 for user1 in User().users if user1["username"] == username and user1['user_id'] == user_id]
		if userz:
			return 'User exists!'

		self.output['username'] = username
		self.output['password'] = password
		self.output['user_id'] = user_id
		self.output['admin'] = False
		User.users.append(self.output)
		return 'User successfully created'

	def login(self, username, password):
		if username == '' or password == '':
			return 'Enter both username and password'

		if not isinstance(username, str) or not isinstance(password, str):
			return 'Please enter a string value for username and password'

		userz = [user1 for user1 in User().users if user1["username"] == username and user1["admin"] == False]
		caters = [cater for cater in Caterer().caterer if cater["username"] == username and cater["admin"] == True]

		if not userz and not caters:
			return 'No such user! Please create an account'

		if userz:
			session["logged_in"] = True
			return "Loggin successful"
		else:
			session["logged_in"] = True
			return "Loggin successful, Welcome Admin"

	def logout(self):
		session['logged_in'] = False
		if session['logged_in'] == False:
			return 'Log out successful'

	def get_menu(self):
		return Caterer().menu_list

	def make_order(self, meal_id, meal_name, price, category, day, quantity, username):
		if meal_id == '' or meal_name == '' or price == '' or category == '' or day == '' or quantity == '' or username == '':
			return 'Please enter all the details'

		#Should validate the input data types
		menus = [menu for menu in Caterer().menu_list if menu["meal_id"] == meal_id and menu['meal_name'] == meal_name]
		if not menus:
			return 'Meal doesn\'t exists in menu!'

		self.output['meal_id'] = meal_id
		self.output['meal_name'] = meal_name
		self.output['price'] = price
		self.output['category'] = category
		self.output['day'] = day
		self.output['quantity'] = quantity
		self.output['username'] = username
		Caterer.order_list.append(self.output)
		return 'Meal successfully added to your orders'

	def modify_order(self, meal_id, quantity):
	    #Should validate the input data types
	    orders = [order for order in Caterer().order_list if order["meal_id"] == meal_id]
	    if not orders:
	    	return 'Meal doesn\'t exists in orders!'

	    orde = orders[0]
	    price = orde["price"]

	    self.output['quantity'] = quantity
	    self.output['price'] = price * quantity
	    return 'Order successfully modified'

	def remove_order(self, meal_id):
		orders = [order for order in Caterer().order_list if order["meal_id"] == meal_id]
		if not orders:
			return 'Meal doesn\'t exists in orders!'

		Caterer.order_list.remove(orders[0])
		return 'Order removed successfully'