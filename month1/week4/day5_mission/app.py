from flask import Flask, jsonify, request

app= Flask(__name__)

weapons= []

@app.route('/')
def hello_flask():
    return 'Hello World!'

@app.route('/whoami')
def whoami():
    # return jsonify({"name": "suyong2"})
    return {"name": "suyong2"}

@app.route('/echo')
def echo():        
    echo = request.args.get("string")
    # return jsonify({"value": echo})
    return {"value": echo}

@app.route('/weapons', methods=['POST'])
def create_weapon():
    request_data= request.get_json()
    if len(weapons)==0:
        id=1
    else:
        id=weapons[-1]['id']+1
    new_weapon = {
        "id": id,
        "name": request_data['name'],
        "stock": request_data['stock'],
    }
    weapons.append(new_weapon)
    return {"weapons": weapons}

@app.route('/weapons')
def get_weapons():
    return {"weapons": weapons}

@app.route('/weapons/<int:id>', methods=['PUT'])
def update_weapon(id):
    request_data= request.get_json()
    found_dict = None
    for item in weapons:
        if item.get('id') == id:
            found_dict = item
            break
    if found_dict:
        found_dict["name"] = request_data['name']
        found_dict["stock"] = request_data['stock']

    return {"weapons": weapons}

@app.route('/weapons/<int:id>', methods=['DELETE'])
def delete_weapon(id):
    index = -1
    for i, item in enumerate(weapons):
        if item.get('id') == id:
            index = i
            break
    if index != -1:
        del weapons[index]

    return {"weapons": weapons}

if __name__=='__main__':
    app.run()