from ._anvil_designer import Completed_TasksTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Completed_Tasks(Completed_TasksTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def data_grid_1_show(self, **event_args):
    """This method is called when the data grid is shown on the screen"""
    self.repeating_panel_1.items = anvil.server.call('show_completed')

