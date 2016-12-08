from app import db

class Brew(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    start_date = db.Column(db.DateTime, index=True)
    temp_data = db.relationship('Temperature', backref='brewID', lazy='dynamic')

    def __repr__(self):
        return '<Brew %r>' % (self.name)

class Temperature(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    temp_reading = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)
    brew_id = db.Column(db.Integer, db.ForeignKey('brew.id'))

    def __repr__(self):
        return '<Temperature %r>' % (self.temp_reading)