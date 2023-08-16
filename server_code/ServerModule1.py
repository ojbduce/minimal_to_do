import anvil.email
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import datetime

@anvil.server.callable
def add_task(task):
  if anvil.users is not None:
    app_tables.tasks.add_row(task=task, done=False, owner=anvil.users.get_user())

@anvil.server.callable
def get_tasks():
  if anvil.users is not None:
    return app_tables.tasks.client_writable(owner=anvil.users.get_user()).search()
    # we are getting checked items from this which should already be deleted from db.

@anvil.server.callable
def tasks_done(task):
  #task = str(task) # this is a live object
  date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
  app_tables.done.add_row(task=task, owner=anvil.users.get_user(),date=date)

@anvil.server.callable
def show_completed():
  return app_tables.done.client_readable(owner=anvil.users.get_user()).search()