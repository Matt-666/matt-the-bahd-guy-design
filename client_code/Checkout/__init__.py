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
  def __init__(self, id_name, **properties):
    # Set Form properties and Data Bindings.
   self.init_components(**properties)
   self.update.form(id_name)

  def update_form(self, id_name):
    anvil.server.call('get_shop_details', id_name)
    self.name_label.text = menwears["name"] 
   







    # Any code you write here will run before the form opens.
