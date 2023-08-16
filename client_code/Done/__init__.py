from ._anvil_designer import DoneTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Done(DoneTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.update_login_status()

    # Any code you write here will run before the form opens.

  def button_to_do_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('To_Do')

  def button_login_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.login_with_form()
    user = anvil.users.get_user()
    self.label_login_status.text= f"You are logged in as {user['email']}"

  def button_log_out_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_login_status.text = "You are logged out"
    anvil.users.logout()
    open_form('Done')
  
  def update_login_status(self):
    user = anvil.users.get_user()
    if user is None:
      self.label_login_status.text = "You are not logged in"
    else:
      self.label_login_status.text= f"You are logged in as {user['email']}"