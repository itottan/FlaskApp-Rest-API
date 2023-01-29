from marshmallow import Schema, fields


"""
memo
在Web API的上下文中,序列化参数dump_only和反序列化参数load_only在概念上分别等同于只读和只写字段
1. The issue is that ItemSchema contains (nests) the StoreSchema and the StoreSchema contains (nests) the ItemSchema. Because of that two problems arise
    -> solves this problem using lambda functions
       This works because the contents of the lambda function only get evaluated when the function is called and not when the class is created, and at that moment both classes have already been defined.
2. The second problem is caused by recursion. This means that one class calls the other class en vice versa resulting in a neverending loop. Here is a simple example, starting with a store and one item, you can see that there is a reference to the items inside the store and a reference to the store inside the item
"""

class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)

class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()

class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()

class TagSchema(PlainTagSchema):
    store_id = fields.Int(load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)

class TagUpdateSchema(Schema):
    pass

class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)

class TagAndItemSchema(Schema):
    message = fields.Str()
    item = fields.Nested(ItemSchema)
    tag = fields.Nested(TagSchema)