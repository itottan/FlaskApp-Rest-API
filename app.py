# rest api
# use POSTMAN to test API
from flask import Flask, request


app = Flask(__name__)
 
stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chari",
                "price": "15.99"
            }
        ]
    }
]

@app.get("/store")
def get_stores():
    return {"stores": stores}

@app.post("/store")
def creat_store():
    req_data = request.get_json()
    new_store = {"name": req_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201

@app.post("/store/<string:name>/item") # Todo: 多个参数时如何处理
def create_item(name):
    req_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item ={"name": req_data["name"],"price": req_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404

@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404

@app.get("/store/<string:name>/item")
def get_items_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404


if __name__ == "__main__":
    app.run(debug=True)