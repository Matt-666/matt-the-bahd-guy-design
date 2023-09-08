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
   shop = anvil.server.call("get_all_menwears").search()
   shop_panel = GridPanel()
   
   for i,  menwears in enumerate(shop):
     c = ShopItem(name= menwears["name"], button_text=f"Purchase for ${menwears['price']}", description= menwears["description"], image= menwears["Image"], button_callback=None)
     shop_panel.add_component(c, row = str(i//3), width_xs = 4)

   self.Content_panel.add_component(shop_panel)