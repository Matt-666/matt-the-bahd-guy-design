from ._anvil_designer import ClothesTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..ShopItem import ShopItem

class Clothes(ClothesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.load_shop()
    c = ShopItem(nameo="Trousers", button_text="Buy For 19299.99", description="Suits your taste")
    self.Content_panel.add_component(c)
  
  def load_shop(self):
   shop = anvil.server.call("get_shop_details").search()
   
   for menwears in shop:
     print(menwears["name"])