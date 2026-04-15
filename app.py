from flask import Flask, jsonify, request
import random

#Instantiate flask app using current script name (app.py)
app = Flask(__name__)

#Item class to simulate a database model
class Item:
    
    def __init__(self,id,item_name,item_price=0,item_stock_level=0):
        self.id = id
        self.item_name = item_name
        self.item_price = item_price
        self.item_stock_level = item_stock_level
    
    #Convert object instance to dictionary format (for JSON response)
    def to_dict(self):
        return {
            "id":self.id,
            "item_name":self.item_name,
            "item_price":self.item_price,
            "item_stock_level":self.item_stock_level
            }

#In-memory list acting as a mock database
items = []

#Generate a random integer to act as a unique ID/code for the item
def generate_random_int():
    random_int = random.randint(10000,1000000000)
    return random_int

#CREATE: Add a new item -> POST /inventory
@app.route("/inventory", methods=["POST"])
def create_item():

    global items

    #Extract incoming JSON data
    incoming_data = request.get_json()

    #Generate unique ID for new item
    new_item_code = generate_random_int()

    #Create new item instance
    new_item = Item(id=new_item_code, item_name=incoming_data["item_name"])

    #Store item as dictionary in list
    items.append(new_item.to_dict())
    
    return jsonify(new_item.to_dict()),201

#READ: Retrieve all items -> GET /inventory
@app.route("/inventory", methods=["GET"])
def get_items():
    global items
    return jsonify(items), 200

# UPDATE: Modify item price and stock ->PATCH /inventory/<id> 
@app.route("/inventory/<id>", methods=["PATCH"])
def update_item(id):

    global items

    #Extract incoming JSON data
    incoming_data = request.get_json()

    #Extract updated values
    incoming_data_price = incoming_data["price"]
    incoming_data_stock_level = incoming_data["stock_level"]

    #Find matching item by id
    found_item = next((item for item in items if item["id"] == id),None)

    #If item is found, update the item's price and stock level
   
    if not found_item:
        return jsonify({"message": f"The item of id '{id}' cannot be found in the system"}),404
    else:
        found_item["item_price"] = incoming_data_price
        found_item["item_stock_level"] = incoming_data_stock_level

        return jsonify({"message": f"You have successfully updated item id {id}."})

# DELETE: Remove an item -> DELETE /inventory/<id>
@app.route("/inventory/<id>", methods=["DELETE"])
def remove_item(id):
    
    global items

    #Find item before attempting to delete 
    found_item = next((item for item in items if item["id"] == id),None)

    #If item is found, delete the item

    if not found_item:
        return jsonify({"message": f"Item id '{id}' cannot be found in the system."}),404
    else:
        items = [item for item in items if item["id"] != id]
        return jsonify({"message": f"Successfully deleted item id '{id}'."}),204

#Run the application on port 5555
if __name__ == "__main__":
    app.run(debug=True, port=5555)