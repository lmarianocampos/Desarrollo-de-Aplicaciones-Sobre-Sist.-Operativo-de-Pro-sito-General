from flask import Flask, json, request
app = Flask(__name__)

@app.route('/test')
def hello_world():
    return 'Flask is online'

@app.route('/users', methods=['GET', 'POST'])
def get_users():
    allData = [ 
        {
            "id": 1,
            "firstName":"John", 
            "lastName":"Snow" 
        },
        {
            "id": 2,
            "firstName":"Arya",
            "lastName":"Stark"
        }
    ]
    newData = {
            "id": 3,
            "firstName":"Alan",
            "lastName":"Turing"
        }
    
    if request.method == 'GET':
        response = app.response_class(
            response=json.dumps(alldData),
            status=200,
            mimetype='application/json'
        )
        return response
    else:
        response = app.response_class(
            response=json.dumps(newData),
            status=201,
            mimetype='application/json'
        )
        return response

@app.route('/users/<userId>', methods=['GET'])
def get_user(userId):
    data = { 
        "id": 1,
        "firstName":"John", 
        "lastName":"Snow" 
    }
    if request.method == 'GET':
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
    else:
        response = app.response_class(
            status=405,
            mimetype='application/json'
        )
        return response

@app.route('/users/<userId>/adresses')
def get_user_adresses(userId):
    data = [ 
        {
            "street":"Alem 1000",
            "city":"Buenos Aires"
        },
        {
            "street":"Alem 1000",
            "city":"Buenos Aires"
        }
    ]
    
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
	app.debug = True
	app.run()
