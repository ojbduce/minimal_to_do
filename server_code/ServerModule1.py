import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

def add_to_do_item_to_data_table(item):
  app_tables.to_do_items.
