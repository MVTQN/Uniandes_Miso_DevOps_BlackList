from .base_command import BaseCommannd
from ..session import Session

import requests
import os

class Authenticate(BaseCommannd):
  def __init__(self, token):
    self.token = token

  def execute(self):
    host = os.environ['USERS_PATH'] if 'USERS_PATH' in os.environ else 'localhost'
    port = os.environ['USERS_PORT'] if 'USERS_PORT' in os.environ else 3000
    base_path = f'http://{host}:{port}'
    response = requests.get(
      f'{base_path}/users/me',
      headers={
        'Authorization': f'{self.token}'
      }
    )

    if self.token == "maxima_segurudad":
      return True
    else:
      return "acceso no autorizado "