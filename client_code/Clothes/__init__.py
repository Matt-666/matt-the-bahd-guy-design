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
    
  
  def load_shop(self):
   shop = anvil.server.call("get_shop_details").search()
   
   for menwears in shop:
     c = ShopItem(name=menwears["name"], button_text=f"Purchase for ${menwears["Price"]}", description=menwears["description"], image=menwears["image"], button_callback=None)
     self.Content_panel.add_component(c)