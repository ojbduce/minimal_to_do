import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def add_to_do_item_to_data_table(task):
  app_tables.tasks.add_row(task = task, done = False)

@anvil.server.callable
def get_tasks():
  return app_tables.tasks.client_writable().search()