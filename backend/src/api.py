import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
!! Running this funciton will add one
'''
#db_drop_and_create_all()

# ROUTES
'''
@TODO implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
#get all the drinks
@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    drinks_dict = []
    for drink in drinks:
        get=drink.short()
        drinks_dict.append(get)

    return jsonify({
      'success':True,
      'drinks':drinks_dict
      })


'''
@TODO implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks-detail')
@requires_auth('get:drinks-detail')
def get_drinks_detail(token):
    drinks = Drink.query.all()
    drinks_dict = []
    for drink in drinks:
        get=drink.long()
        drinks_dict.append(get)

    return jsonify({
        'success': True,
        'drinks': drinks_dict
    })

'''
@TODO implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def add_drink(token):
    body = request.get_json()
    title = body.get('title',None)
    recipe = body.get('recipe')
    if ((title is None) or (recipe is None)):
        abort(404)
    try:
        drink = Drink(title=title, recipe=json.dumps(recipe))
        drink.insert()
        return jsonify({
            'success': True,
            'drinks': [drink.long()]
    })
    except:
        abort(422)
    
'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks/<int:id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def edit_drink_by_id(*args, **kwargs):
    body = request.get_json()
    title = body.get('title',None)
    recipe = body.get('recipe')
    try:
        get_id = kwargs['id']
        drink = Drink.query.filter_by(id=get_id).one_or_none()

        if (title is None):
            abort(400)
        else:
            drink.title = title

        if 'recipe' in body:
            drink.recipe = json.dumps(recipe)

        drink.update()
        get_drink=Drink.query.filter_by(id=get_id).first()
        return jsonify({
            'success': True,
            'drinks': [get_drink.long()]
    })
    except:
        abort(422)

    
'''
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''

@app.route('/drinks/<int:id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(*args, **kwargs):
    try:
        get_id = kwargs['id']
        drink = Drink.query.filter_by(id=get_id).one_or_none()

        if drink is None:
            abort(404)
        drink.delete()

        return jsonify({
            'success': True,
            'delete': get_id
    })
    except:
        abort(422)
# Error Handling
'''
Example error handling for unprocessable entity
'''

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        'success':False,
        'error':422,
        'message':'Unable to Process this Request'
        }),422

'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''
@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        'success':False,
        'error':400,
        'message':'Bad Request'
        }),400



'''
@TODO implement error handler for 404
    error handler should conform to general task above
'''
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success':False,
        'error':404,
        'message':'resource not found'
        }),404

'''
@TODO implement error handler for AuthError
    error handler should conform to general task above
'''
@app.errorhandler(AuthError)
def handle_auth_error(ex):
    res = jsonify(ex.error)
    res.status_code = ex.status_code
    return res
