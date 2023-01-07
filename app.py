# rest api
# use POSTMAN to test API
from flask import Flask
from flask_smorest import Api

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint


app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)
 
# ストア一覧取得
# @app.get("/store")
# def get_stores():
#     # stores<dict> must change type to list for return JSON
#     return {"stores": list(stores.values())}

# ストア取得
# @app.get("/store/<string:store_id>") #uuid
# def get_store(store_id):
#     try:
#         return stores[store_id] # API return dict, Flask will change it to JSON TODO get StoreItems
#     except KeyError:
#         abort(404, message= "Store not found")

# ストア作成
# @app.post("/store")
# def creat_store():
#     store_data = request.get_json()
#     # creat uuid to make mock
#     store_id = uuid.uid4().hex
#     store = {**store_data, "id": store_id}
#     stores[store_id] = store
#     return store, 201

# ストア削除

# アイテム一覧取得
# @app.get("/item")
# def get_all_items():
#     return "hello world"
#     # return {"items": list(items.values())}

# アイテム取得
# @app.get("/item/<string:item_id>")
# def get_item(item_id):
#     try:
#         return items[item_id]
#     except KeyError:
#         abort(404, message= "item not found")

# アイテム作成
# @app.post("/item") # Todo: 多个参数时如何处理
# def create_item(name):
#     item_data = request.get_json()
#     # TODO check key value & if item already exists
#     # check store is registed
#     if item_data["store_id"] not in stores:
#         abort(404, message= "Store not found")

#     item_id = uuid.uuid4().hex
#     item = { **item_data, "id": item_id }
#     items[item_id] = item
#     return item, 201

# アイテム更新
# @app.put("/item/<string:item_id>")
# def update_item(item_id):
#     item_data = request.get_json()
#     # TODO if no price or no name
#     try:
#         item = items[item_id]
#         # item.update(item_data) can be able to use under v3.9+
#         # pipe operator merge works for only 3.9+
#         item |= item_data #merge dict "item_data" will change item value  `|=`字典运算符|字典更新操作符 https://blog.teclado.com/python-dictionary-merge-update-operators/
#         return item
#     except KeyError:
#         abort(404, message= "item not found")

# アイテム削除
# @app.delete("/item/<string:item_id>")
# def delete_item(item_id):
#     try:
#         del items[item_id]
#         return {"message": f"Item {item_id} deleted"}
#     except KeyError:
#         abort(404, message= "item not found")