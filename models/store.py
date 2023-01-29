from db import db

class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")
    tags = db.relationship("TagModel", back_populates="store", lazy="dynamic")
    
    """
    Remember that StoreModel and ItemModel have a one-to-many relationship, where each store can have multiple items, and each item belongs to a single store.

    The cascade="all,delete" argument in the relationship() call for the StoreModel.items attribute specifies that when a store is deleted, all of its related items should also be deleted.

    If you add a cascade on the relationship in the ItemModel, then when an item is deleted, its related store should also be deleted. This is not what we want, so we won't add a cascade to ItemModel.

    With this code in place, if you try to delete a store that still has items, the items will be deleted automatically along with the store. This will allow you to delete the store without having to delete the items individually.

    For more information, I strongly recommend reading the official documentation!(https://docs.sqlalchemy.org/en/20/orm/cascades.html#delete) There are also other cascade options you can pass in depending on what you want to happen to related models when the parent changes or is deleted.
    """