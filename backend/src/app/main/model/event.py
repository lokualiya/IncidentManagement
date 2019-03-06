from .. import db
import datetime
import enum
from sqlalchemy import Enum

class EventAction(enum.Enum):
    CREATED = 1  
    ATTRIBUTE_CHANGE_REQUESTED = 2
    ATTRIBUTE_CHANGED = 3
    ATTRIBUTE_CHANGE_REJECTED = 4
    COMMENTED = 5
    MEDIA_ATTACHED = 6

class Event(db.Model):
    """ Event model represents an auditable action done by a system user """
    __tablename__ = "event"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # action type for the event, refer enums
    action = db.Column(db.Enum(EventAction))

    # refers to an external entity, ex: comment, media, outcome
    reference_id = db.Column(db.Integer)
    
    # refers to an event linked to the current event i.e for an ATTRIBUTE_CHANGED 
    # event or an ATTRIBUTE_CHANGE_REJECTED event previously occured 
    # ATTRIBUTE_CHANGE_REQUESTED event's id
    linked_event_id = db.Column(db.Integer)

    # specifies additional details
    description = db.Column(db.String(1024))

    # event intiator - should be a user
    intiator = db.Column(db.String(1024))

    # incident related to the event
    incident_id = db.Column(db.Integer, db.ForeignKey('incident.id'))

    # attribute changed by the current event action
    affected_attribute = db.Column(db.String(1024))

    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    approved_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
    def __repr__(self):
        return "<Event '{}'>".format(self.id)