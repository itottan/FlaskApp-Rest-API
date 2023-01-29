from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import ItemModel

from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("Items", __name__, description="Operations on items")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item

    @blp.response(200, ItemSchema)
    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        raise NotImplementedError("アイテムの削除は実装されていません。")

    @blp.arguments(ItemUpdateSchema) # リクエストで受け取った値で型をチェック、Modelと関係ない
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id): # 引数渡す順番に注意
        item = ItemModel.query.get(item_id)
        if item:
            item.name = item_data["name"]
            item.price = item_data["price"]
        else:
            item = ItemModel(id=item_id, **item_data) # id=item_id 確実にReqから渡される指定のitem_idを作成するため
        
        db.session.add(item)
        db.session.commit()

        return item
        # raise NotImplementedError("アイテムの更新は実装されていません。")　# 未実装・実装途中に使える
    
    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        
        db.session.delete(item)
        db.session.commit()
        
        # todo 変更後のアイテム情報を戻したい場合の処理
        return {"message": "アイテムを削除しました。"}
        


@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True)) # many=True 複数データ対応Option
    def get(self):
        return ItemModel.query.all()
    
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        item = ItemModel(**item_data)

        try:
            db.session.add(item)
            db.session.commit()
        # for anything 
        except SQLAlchemyError:
            abort(500, message="アイテムの挿入中にエラーが発生しました")

        return item