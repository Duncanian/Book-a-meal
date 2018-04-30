import os
import jwt
from flasgger import Swagger
from api import app, token_required
from functools import wraps
from flask import Flask, request, jsonify
from models.user import User

swagger = Swagger(app)

@app.route('/api/v1/auth/signup', methods=['POST'])
def sign_up():
    """ endpoint accepting register details.
    ---
    parameters:
      - name: username
        in: formData
        type: string
        required: true
      - name: password
        in: formData
        type: string
        required: true
      - name: user_id
        in: formData
        type: integer
        required: true
    """
@app.route('/api/v1/auth/login', methods=['POST'])
def log_in():
    """ endpoint accepting login details.
    ---
    parameters:
      - name: username
        in: formData
        type: string
        required: true
      - name: password
        in: formData
        type: string
        required: true
    """

@app.route('/api/v1/meals/', methods=['GET'])
@token_required
def getallmeals(active_user):
    """endpoint for  getting meals that have been added.
    ---
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
    """
@app.route('/api/v1/meals/', methods=['POST'])
@token_required
def addmeal(active_user):
    """endpoint adding a meal's details.
    ---
    parameters:
      - name: meal_id
        in: formData
        type: integer
        required: true
      - name: meal_name
        in: formData
        type: string
        required: true
      - name: price
        in: formData
        type: integer
        required: true
      - name: category
        in: formData
        type: string
        required: true
      - name: day
        in: formData
        type: string
        required: true
      - name: Authorization
        in: header
        type: string
        required: true
    """
@app.route('/api/v1/meals/<int:mealId>', methods=['PUT'])
@token_required
def editmeal(active_user, mealId):
    """endpoint editing a meal's details.
    ---
    parameters:
      - name: meal_id
        in: path
        type: integer
        required: true
      - name: meal_name
        in: formData
        type: string
        required: true
      - name: price
        in: formData
        type: integer
        required: true
      - name: category
        in: formData
        type: string
        required: true
      - name: day
        in: formData
        type: string
        required: true
      - name: Authorization
        in: header
        type: string
        required: true
    """

@app.route('/api/v1/meals/<int:mealId>', methods=['DELETE'])
@token_required
def deletemeals(active_user, mealId):
    """endpoint for deleting a meal.
    ---
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
      - name: mealId
        in: path
        type: integer
        required: true
    """
@app.route('/api/v1/menu/', methods=['POST'])
@token_required
def setupmenu(active_user):
    """endpoint adding a meal to the menu.
    ---
    parameters:
      - name: meal_id
        in: formData
        type: integer
        required: true
      - name: meal_name
        in: formData
        type: string
        required: true
      - name: price
        in: formData
        type: integer
        required: true
      - name: category
        in: formData
        type: string
        required: true
      - name: day
        in: formData
        type: string
        required: true
      - name: Authorization
        in: header
        type: string
        required: true
    """

@app.route('/api/v1/menu/', methods=['GET'])
@token_required
def menugetter(active_user):
    """endpoint returning meals in menu.
    ---
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
    """
@app.route('/api/v1/orders', methods=['POST'])
@token_required
def makeorders(active_user):
    """endpoint adding a meal in menu to your orders.
    ---
    parameters:
      - name: meal_id
        in: formData
        type: integer
        required: true
      - name: meal_name
        in: formData
        type: string
        required: true
      - name: price
        in: formData
        type: integer
        required: true
      - name: category
        in: formData
        type: string
        required: true
      - name: day
        in: formData
        type: string
        required: true
      - name: quantity
        in: formData
        type: integer
        required: true
      - name: username
        in: formData
        type: string
        required: true
      - name: Authorization
        in: header
        type: string
        required: true
    """
@app.route('/api/v1/orders/<int:orderId>', methods=['PUT'])
@token_required
def modifyorders(active_user, orderId):
    """endpoint for updating a meal in the orders list.
    ---
    parameters:
      - name: orderId
        in: path
        type: integer
        required: true
      - name: quantity
        in: formData
        type: integer
        required: true
      - name: Authorization
        in: header
        type: string
        required: true
    """
@app.route('/api/v1/orders/<int:orderId>', methods=['DELETE'])
@token_required
def deleteorders(active_user, orderId):
    """endpoint for deleting a meal order.
    ---
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
      - name: orderId
        in: path
        type: integer
        required: true
    """
@app.route('/api/v1/orders', methods=['GET'])
@token_required
def get_allorders(active_user):
    """endpoint for getting all orders made by users.
    ---
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
    """

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run('', port=port)