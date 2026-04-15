import requests

try:

    #Option 1: Search for a specific product using its product code (barcode)
    """ 
    
    product_code = input("Enter the product code to search: ")
    
    #Send GET request to Open Food Facts API for a single product
    response = requests.get(f"https://world.openfoodfacts.net/api/v2/product/{product_code}")
    data = response.json()
    print(response.status_code)
    print(data["product"]["product_name"]) 
    
    """
    #Option 2: Retrieve a list of products using the search endpoint
    #Fetches paginated results with selected fields (code and product_name)

    response = requests.get(f"https://world.openfoodfacts.net/api/v2/search?page=1&page_size=20&fields=code,product_name")
    #Convert response to JSON format
    data = response.json()

    #Display HTTP status code
    print(response.status_code)

    #Display full response data(list of products)
    print(data)
    
except Exception as e:
    #Handle any errors related to network connection or request failure
    print(f"Error connecting to the server:{e}")