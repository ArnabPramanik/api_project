from app import db

class Job(db.Model):
    __tablename__ = 'jobs'
    id = db.Column('id', db.Integer, primary_key = True, autoincrement=True)
    title = db.Column('job',db.Unicode)

    def __init__(self,id, data):
        self.id = id
        self.data = data

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
        }


class Skill(db.Model):
    __tablename__ = 'skills'
    id = db.Column('id', db.Integer, primary_key = True, autoincrement=True)
    title = db.Column('skill',db.Unicode)

    def __init__(self,id, title):
        self.id = id
        self.title = title

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
        }