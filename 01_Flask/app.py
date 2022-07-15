from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 16.00,
                'currency': 'USD'
            }
        ]
    }
]


# POST - used to receive data
# GET - used to send data back only

@app.route('/')
def home():
    return "Hello world!"

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):  
    store = next((store for store in stores if store['name'] == name), {'msg': 'Store not found'})
    return jsonify(store)
    
# GET /store
@app.route('/stores')
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price'],
                'curency': request_data['currency']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'msg': 'store not found or does not exists.'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['GET'])
def get_items_in_store(name):
    items = next((store['items'] for store in stores if store['name'] == name), {'msg': 'No items found.'})
    return jsonify({'items': items} )
 
app.run(port=5000)

