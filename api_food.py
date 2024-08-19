
import requests
#json
import json

def get_recipes():
    API_KEY ="2317300746504cb3bf960b78eb6bf1e0" 
    url =  "https://api.spoonacular.com/recipes/search?diet=gluten%20free&apiKey=" + API_KEY

    response = requests.get(url)
    #print(response.text)
    
    #json
    json_body = response.json()
    #all result
    #print(json.dumps(json_body, indent=2))
    
    #using the index to get the specify json answer
    #print(json_body["results"][0]["title"])
    
    # Returning the results from the API
    return json_body["results"]




