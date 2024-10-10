from App.database import db

class Job(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(120), nullable=False)
  description = db.Column(db.String(120), nullable=False)
  company = db.Column(db.String(120), nullable=False)
  salary = db.Column(db.String(120), nullable=False)
  status = db.Column(db.String(120), nullable=False)

  def __init__(self, title, description, company, salary, status):
    self.title = title
    self.description = description
    self.company = company
    self.salary = salary
    self.status = status

  def get_json(self):
    return{
      'id': self.id,
      'title': self.title,
      'description': self.description,
      'company': self.company,
      'salary': self.salary,
      'status': self.status
    }