from ._anvil_designer import To_DoTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class To_Do(To_DoTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #anvil.users.logout()
    anvil.users.login_with_form()
    self.refresh()
    self.update_login_status()
    
  def refresh(self):
    self.repeating_panel_tasks.items = anvil.server.call('get_tasks')

  def update_login_status(self):
    user = anvil.users.get_user()
    if user is None:
      self.label_login_status.text = "You are not logged in"
    else:
      self.label_login_status.text= f"You are logged in as {user['email']}"

  def button_add_click(self, **event_args):
    """This method is called when the button is clicked"""
    task = self.text_box_new_task.text
    anvil.server.call('add_task',task)
    self.text_box_new_task.text = ""
    self.refresh()

  def button_done_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Done')
    

    

