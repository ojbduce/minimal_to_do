from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_tasks.items = anvil.server.call('get_tasks')
    

    # Any code you write here will run before the form opens.

  def button_add_click(self, **event_args):
    """This method is called when the button is clicked"""
    task = self.text_box_new_task.text
    anvil.server.call('add_to_do_item_to_data_table',task)
    self.text_box_new_task.text = ""
    

