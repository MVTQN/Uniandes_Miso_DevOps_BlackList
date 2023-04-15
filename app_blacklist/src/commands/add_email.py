from .base_command import BaseCommannd
from ..models.blacklist import Email,EmailSchema
from ..session import Session
from sqlalchemy import or_

emailSchema = EmailSchema()
class AddEmail(BaseCommannd):
    def __init__(self,data,ip):
        self.data = data
        self.ip = ip 
        
    def execute(self):
        email = self.data["email"]
        blocked_reason = self.data["blocked_reason"]
        app_uuid1 = self.data['app_uuid']
        
        newEmail = Email(self.ip,email,app_uuid1,blocked_reason)
        session = Session()
        consulta = session.query(Email).filter_by(app_uuid = app_uuid1).all()
        
        print(len(consulta))
        if len(consulta) == 0:
            session.add(newEmail)
            session.commit()
        else:
            return 'el app_uuid  ya es encuentra registrado'
        return emailSchema.dump(newEmail)
        