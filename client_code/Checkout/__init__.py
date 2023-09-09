from ._anvil_designer import CheckoutTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Checkout(CheckoutTemplate):
  def __init__(self, id_name, back_button_callback, **properties):
    # Set Form properties and Data Bindings.
   self.init_components(**properties)
   self.update_form(id_name)

  def update_form(self, id_name):
    menwears=anvil.server.call('get_shop_details', id_name)
    self.menwears=menwears
    self.name_label.text = menwears["name"] 
    self.decription_label.text = menwears["decription"]
    self.price_label.text = f"${menwears['price']}USD"
    self.image_content.source = menwears["image"]







    # Any code you write here will run before the form opens.

  def buy_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def back_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.back_button_callback()


