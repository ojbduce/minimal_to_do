import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def add_task(task):
  if anvil.users is not None:
    app_tables.tasks.add_row(task=task, done=False, owner=anvil.users.get_user())

@anvil.server.callable
def get_tasks():
  if anvil.users is not None:
    return app_tables.tasks.client_writable(owner=anvil.users.get_user()).search()