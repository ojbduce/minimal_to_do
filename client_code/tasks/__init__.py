from ._anvil_designer import tasksTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class tasks(tasksTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.refresh()
  def refresh(self):
    self.repeating_panel_tasks.items = anvil.server.call('get_tasks')
    
    

    # Any code you write here will run before the form opens.

  def button_add_click(self, **event_args):
    """This method is called when the button is clicked"""
    task = self.text_box_new_task.text
    anvil.server.call('add_to_do_item_to_data_table',task)
    self.text_box_new_task.text = ""
    self.refresh()
    

