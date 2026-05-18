from . import db
from datetime import datetime, timezone

class Task(db.Model):
    __tablename__ = 'tasks'

    id         = db.Column(db.Integer, primary_key=True)
    title      = db.Column(db.String(300), nullable=False)
    is_done    = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc),
                           onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    def to_dict(self):
        return {
            'id':         self.id,
            'title':      self.title,
            'is_done':    self.is_done,
            'created_at': self.created_at.strftime('%d %b %Y, %H:%M'),
            'updated_at': self.updated_at.strftime('%d %b %Y, %H:%M'),
        }
