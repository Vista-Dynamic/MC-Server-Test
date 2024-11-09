from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import time
from . import Module1


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.
    
  def button_1_click(self, **event_args):
    file = anvil.server.call("get_file")
    print(file.get_bytes())
    download(file)

  def button_2_click(self, **event_args):
    file = anvil.server.call('get_file')
    cont = file.get_bytes()
    self.rich_text_1.content = cont