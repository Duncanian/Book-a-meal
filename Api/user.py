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
		return 'You were not logged in'

	def get_menu(self):
		pass

	def make_order(self):
		pass

	def modify_order(self):
		pass