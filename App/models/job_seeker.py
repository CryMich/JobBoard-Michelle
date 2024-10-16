from App.database import db

class JobSeeker(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20), nullable=False, unique=True)

  def __init__(self, name):
    self.name = name

  def get_json(self):
    return{
      'id': self.id,
      'name': self.name
    }