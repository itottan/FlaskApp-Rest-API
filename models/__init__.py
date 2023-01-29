# To make it easier to import and use the models, I'll also create a models/__init__.py file that imports the models from their files:

from models.store import StoreModel
from models.item import ItemModel
from models.tag import TagModel
from models.item_tag import ItemsTags