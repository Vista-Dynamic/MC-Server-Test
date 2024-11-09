import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import time
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#


def say_hello():
  print("Hello, world")

def UploadFiles():
  while True:
    file = anvil.server.call('get_file')
    app_tables.file.add_row(File=file,Name="Latest")
    time.sleep(300)
