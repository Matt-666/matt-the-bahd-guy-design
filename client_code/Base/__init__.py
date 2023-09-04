from ._anvil_designer import BaseTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Home import Home

class Base(BaseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.content_panel.add_component(Home())

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
   """This method is called when the link is clicked"""
   self.content_panel.clear()
   self.content_panel.add_component(Home())

  def My_designs_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Clothes())
    


