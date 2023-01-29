from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import StoreModel

from schemas import StoreSchema

# Operations: 運転，操作
blp = Blueprint("stores", __name__, description="Operations on stores") # todo ここの設定は何のため？

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        stroe = StoreModel.query.get_or_404(store_id)
        return stroe
    def delete(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        
        db.session.delete(store)
        db.session.commit()

        # todo 変更後のストア情報を戻したい場合の処理
        return {"message": "ストアを削除しました。"}

@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        # return {"stores": list(stores.values())} # dict to list for json format
        return StoreModel.query.all()

    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, store_data):
        store = StoreModel(**store_data)

        try:
            db.session.add(store)
            db.session.commit()
        # when a client attempts to create a store with a name that already exists
        except IntegrityError:
            abort(400, message="ストアは既に存在します。")
        # for anything else
        except SQLAlchemyError:
            abort(500, message="ストアの作成中にエラーが発生しました。")
    

        return store