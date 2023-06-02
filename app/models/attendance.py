from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin


class Attendance(db.Model):
    #TODO: Add columns, etc, here
    
    __tablename__ = "attendance"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    rating = db.Column(db.String)
    comments = db.Column(db.String)

    lesson_id = db.Column(db.Integer, db.ForeignKey("lesson.id"), nullable=False)
    #lesson = db.relationship("lesson.name", backref="attendance", lazy=True)
    student_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    #student = db.relationship("User.username", backref="attendance", lazy=True)
    presence = db.Column(db.Boolean(("Present")), default=False, nullable=False)    
       
    release_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())
    updated_at = db.Column(
        db.DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )

    def __repr__(self):
        return "<Attendance %r>" % self.id
