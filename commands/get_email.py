from .base_command import BaseCommannd
from models.blacklist import Email, EmailSchema
from session import Session
from sqlalchemy import or_

emailSchema = EmailSchema()
class GetEmail(BaseCommannd):
    def __init__(self,email):
         self.email = email
        
    def execute(self):
        session = Session()
        consulta = session.query(Email).filter_by(email = self.email).all()
        consulta2 = session.query(Email).filter_by(email = self.email).first()        
        consultaSerialized = emailSchema.dump(consulta2)      
        if len(consulta) == 0:
            return {
                    "EmailIsInGlobalBlackList": False,
                    "BlockedReason": ''
                }   
        else:
            # response.EmailIsInGlobalBlackList = True
            # return response
            return {
                    "EmailIsInGlobalBlackList": True,
                    "BlockedReason": consultaSerialized['blocked_reason']
                }