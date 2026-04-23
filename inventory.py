from flask import Flask
import requests

#Initialize Flask app(used to structure the client-side script)
app = Flask(__name__)

#Inventory class to interact with the local flask API and external API
class Inventory:

	def __init__(self):
		
		#Base URL for the local inventory API
		self.URL = "http://127.0.0.1:5555/inventory"

	#CREATE: Send a POST request to add a new inventory item
	def add_new_item(self):

		#Collect item name from user input
		new_item = input("Add new item: ")

		#Prepare request payload
		payload = {
			"item_name":new_item
		}

		try:
			#Send a POST request to API
			response = requests.post(self.URL,json=payload)
			print(f"New item added: {response.json()}")
		
		except Exception as e:
			#Handle connection or request errors
			print(f"Error connecting to the server:{e}")

	#READ: Send a GET request to retrive all inventory items
	def view_inventory_details(self):

		try:
			#Fetch all items from API
			response = requests.get(self.URL).json()
			print(f"{response}")

		except Exception as e:
			print(f"Error connecting to the server:{e}")

	#UPDATE: Send a PATCH request to modify item price and stock level
	def price_stock_update(self):

		#Collect update details from user
		product_id = input("Enter the item product code: ")
		new_price = input("Update the price of the item: ")
		new_stock_level = input("Update the stock level of the item: ")

		#Prepare request payload
		payload = {
			"id": product_id,
			"price": new_price,
			"stock_level": new_stock_level
		}

		try:
			#Send PATCH request to update specific item
			response = requests.patch(self.URL+'/'+ product_id,json=payload).json()
			print(f"{response}")

		except Exception as e:
			print(f"Error connecting to the server:{e}")

	#DELETE: Send a DELETE request to remove an item from inventory
	def delete_item(self):

		# Collect item ID to delete
		product_id = input("Enter the item product code to delete: ")

		payload = {
			"id": product_id
		}

		try:
			# Send DELETE request to API
			response = requests.delete(self.URL+'/'+ product_id,json=payload).json()
			print(f"{response}")

		except Exception as e:
			print(f"Error connecting to the server:{e}")

	#EXTERNAL API: Retrieve produdct details from Open Food Facts API
	#The user provides a barcode, which is used to query the API
	def get_remote_item(self):
		
		#Collect product barcode from user
		product_code = input("Enter the product code to search: ")

		try:
			#Send GET request to Open Food Facts API
			response = requests.get(f"https://world.openfoodfacts.net/api/v2/product/{product_code}")
			data = response.json()
			print(response.status_code)
			print(data["product"]["product_name"])

		except Exception as e:
			print(f"Error connecting to the server:{e}")
