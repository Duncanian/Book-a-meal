'''test_api endpoints'''
import unittest
import json
from api import app

class TestApiEndpoints(unittest.TestCase):
    '''class to tests app.py'''
  def setUp(self):
    '''create a test client'''
    tester = app.test_client(self)

    #User activities
  def test_user_registration(self):
    '''Test user registration(POST)'''
    reg_data = json.dumps({"user_id":1, "username": "Queer", "password":"#12345", "admin":False})
    response = tester.post('/api/v1/auth/signup', data=reg_data, content_type='application/json')
    self.assertEqual(response.status_code, 200)

  def test_user_login(self):
    #Test the user login functionality
    #register user first
    reg_data = json.dumps({"user_id":1, "username": "Queer", "password":"#12345", "admin":False})
    response = tester.post('/api/v1/auth/signup', data=reg_data, content_type='application/json')
    self.assertEqual(response.status_code, 200)
    #Login the user
    reg_data = json.dumps({"username": "Queer", "password":"#12345"})
    response = tester.post('/api/v1/auth/login', data=reg_data, content_type='application/json')
    self.assertEqual(response.status_code, 200)

  def test_user_can_get_menu(self):
    #Test user access to the menu
    response = self.client().get('/api/v1/menu/', content_type = 'application/json')
    self.assertEqual(response.status_code, 200)

  def test_user_can_make_an_order(self):
    #Test the user's order capability
    meal_data = json.dumps({"meal_id":1, "meal_name": "Rice", "price":200, "category":"dinner", "day":"none", "order":False})
    response = tester.post('/api/v1/meal/', data=meal_data, content_type='application/json')
    self.assertEqual(response.status_code, 200)

    setup = tester.post('/api/v1/menu/', data=json.dumps(response.data), content_type='application/json')
    self.assertEqual(response.status_code, 200)

    get_menu = tester.get('/api/v1/menu/', content_type = 'application/json')
    self.assertEqual(response.status_code, 200)

    get_menu["order"] = True

    make_order = tester.post('/api/v1/orders', data=json.dumps(get_menu.data), content_type = 'application/json')
    self.assertEqual(make_order.status_code, 200)

  def test_user_can_modify_an_order(self):
    #Test the edit order ability
    meal_data = json.dumps({"meal_id":1, "meal_name": "Rice", "price":200, "category":"dinner", "day":"none", "order":False})
    response = tester.post('/api/v1/meal/', data=meal_data, content_type='application/json')
    self.assertEqual(response.status_code, 200)

    setup = tester.post('/api/v1/menu/', data=json.dumps(response.data), content_type='application/json')
    self.assertEqual(response.status_code, 200)

    get_menu = tester.get('/api/v1/menu/', content_type = 'application/json')
    self.assertEqual(response.status_code, 200)

    get_menu["order"] = True
    get_menu["order_id"] = 123

    make_order = tester.post('/api/v1/orders', data=json.dumps(get_menu.data), content_type = 'application/json')
    self.assertEqual(make_order.status_code, 200)

    update_order = {"meal_name": "Meat", "price":210, "category":"lunch", "day":"Monday"}
    res = tester.put('/api/v1/orders/123', data=update_order, content_type='application/json')
    self.assertEqual(res.status_code, 200)

  def test_caterer_get_all_meal options(self):
    '''test that api can get all books (GET request)'''
    meal_data = json.dumps({"meal_id":1, "meal_name": "Rice", "price":200, "category":"dinner", "day":"none"})
    response = tester.post('/api/v1/meal/', data=meal_data, content_type='application/json')
    self.assertEqual(response.status_code, 200)

    response = tester.get('/api/v1/meals/', content_type='application/json')
    self.assertEqual(response.status_code, 200)

  def test_caterer_can_add_a_meal_option(self):
    meal_data = json.dumps({"meal_id":1, "meal_name": "Rice", "price":200, "category":"dinner", "day":"none"})
    response = tester.post('/api/v1/meal/', data=meal_data, content_type='application/json')
    self.assertEqual(response.status_code, 200)

  def test_caterer_can_update_meal_option_by_id(self):
    meal_data = json.dumps({"meal_id":1, "meal_name": "Rice", "price":200, "category":"dinner", "day":"none"})
    response = tester.post('/api/v1/meal/', data=meal_data, content_type='application/json')
    self.assertEqual(response.status_code, 200)

    update_data = {"meal_name": "Meat", "price":210, "category":"lunch", "day":"Monday"}
    res = tester.put('/api/v1/meals/1', data=update_data, content_type='application/json')
    self.assertEqual(res.status_code, 200)

  def test_caterer_can_delete_meal_option_by_id(self):
    meal_data = json.dumps({"meal_id":1, "meal_name": "Rice", "price":200, "category":"dinner", "day":"none"})
    response = tester.post('/api/v1/meal/', data=meal_data, content_type='application/json')
    self.assertEqual(response.status_code, 200)

    res = tester.delete('/api/v1/meals/1', content_type='application/json')
    self.assertEqual(res.status_code, 200)

  def test_caterer_can_setup_menu(self):
    meal_data = json.dumps({"meal_id":1, "meal_name": "Rice", "price":200, "category":"dinner", "day":"none"})
    response = tester.post('/api/v1/meal/', data=meal_data, content_type='application/json')
    self.assertEqual(response.status_code, 200)

    setup = tester.post('/api/v1/menu/', data=json.dumps(response.data), content_type='application/json')
    self.assertEqual(response.status_code, 200)

  def test_caterer_can_get_orders(self):
    meal_data = json.dumps({"meal_id":1, "meal_name": "Rice", "price":200, "category":"dinner", "day":"none", "order":False})
    response = tester.post('/api/v1/meal/', data=meal_data, content_type='application/json')
    self.assertEqual(response.status_code, 200)

    setup = tester.post('/api/v1/menu/', data=json.dumps(response.data), content_type='application/json')
    self.assertEqual(response.status_code, 200)

    get_menu = tester.get('/api/v1/menu/', content_type = 'application/json')
    self.assertEqual(response.status_code, 200)

    get_menu["order"] = True
    get_menu["order_id"] = 123

    make_order = tester.post('/api/v1/orders', data=json.dumps(get_menu.data), content_type = 'application/json')
    self.assertEqual(make_order.status_code, 200)

    res = tester.get('/api/v1/orders', content_type='application/json')
    self.assertEqual(res.status_code, 200)

if __name__ == "__main__":
    unittest.main()
