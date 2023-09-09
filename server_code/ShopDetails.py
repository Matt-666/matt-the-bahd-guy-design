import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_shop_details(product_name):
  return app_tables.menwears.get(name=product_name)


@anvil.server.callable
def get_all_menwears():
  return app_tables.menwears.client_readable()
   
#
