from .base_command import BaseCommannd
from ..models.blacklist import Email,EmailSchema
from ..session import Session
from sqlalchemy import or_

emailSchema = EmailSchema()
class GetEmail(BaseCommannd):
    def __init__(self,email):
         self.email = email
        
    def execute(self):
        session = Session()
        consulta = session.query(Email).filter_by(email = self.email).all()
        
        print(len(consulta))
        if len(consulta) == 0:
            return False
        else:
            return True
        