from App.database import db

class Employer(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20), nullable=False, unique=True)
  company = db.Column(db.String(120), nullable=False)

  def __init__(self, name, company):
    self.name = name
    self.company = company

  def get_json(self):
    return{
      'id': self.id,
      'name': self.name,
      'company': self.company
    }