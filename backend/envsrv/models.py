from . import db

class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return '<Region: {}>'.format(self.name)