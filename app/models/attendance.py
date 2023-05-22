from . import db
from sqlalchemy.sql import func


class Attendance(db.Model):
    #TODO: Add columns, etc, here
    
    __tablename__ = "attendance"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    rating = db.Column(db.String)
    comments = db.Column(db.String)
    presence = db.Column(db.models.BooleanField(_("Present")), default=False, nullable=False)
    classroom_id = db.Column(db.Integer, db.ForeignKey("classroom.id"), nullable=False)
    classroom = db.relationship("Classroom", backref="attendance", lazy=True)
    student_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    
       
    release_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())
    updated_at = db.Column(
        db.DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )

    def __repr__(self):
        return "<Attendance %r>" % self.id
