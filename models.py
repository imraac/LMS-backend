
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates, relationship
import json
import re

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(129), nullable=False)
    role = db.Column(db.String(50), default='user')
    created_at = db.Column(db.DateTime, default=db.func.now())

    subscriptions = db.relationship('Subscription', back_populates='user')
    payments = db.relationship('Payment', back_populates='user')

    @validates('email')
    def validate_email(self, key, email):
        regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.match(regex, email):
            raise ValueError("Invalid email address")
        return email

    def __repr__(self):
        return f"<User {self.id}: {self.username}>"

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role,
            "created_at": str(self.created_at),
        }
class QuizResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    total_questions = db.Column(db.Integer, nullable=False)
    answers = db.Column(db.JSON, nullable=False)  # Store answers as JSON
    date_taken = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def as_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "category": self.category,
            "score": self.score,
            "total_questions": self.total_questions,
            "answers": self.answers,
            "date_taken": self.date_taken
        }

class Subscription(db.Model):
   __tablename__ = 'subscriptions'
   id = db.Column(db.Integer, primary_key=True)
   user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  
   course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=True)  
   amount = db.Column(db.Float, nullable=False)
   created_at = db.Column(db.DateTime, default=datetime.utcnow)
   
   user = db.relationship('User', back_populates='subscriptions')  
   course = db.relationship('Course', back_populates='subscriptions')

   def __repr__(self):
    return f'<Subscription id={self.id} user_id={self.user_id} amount={self.amount}>'

   
  
class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    transaction_id = db.Column(db.String(50))
    status = db.Column(db.String(20), default='pending')
    result_desc = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime)
    mpesa_receipt_number = db.Column(db.String(100), nullable=True)  # transaction mpesa number
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', back_populates='payments')

    def as_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'amount': self.amount,
            'phone_number': self.phone_number,
            'transaction_id': self.transaction_id,
            'status': self.status,
            'result_desc': self.result_desc,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }


class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image = db.Column(db.String(255), nullable=True)
    video = db.Column(db.String(255), nullable=True)
    tech_stack = db.Column(db.String(255), nullable=True)
    what_you_will_learn = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, default=True, nullable=False)  # New field
    requires_subscription = db.Column(db.Boolean, default=False)  # New field

    subscriptions = db.relationship('Subscription', back_populates='course')

    def as_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.truncate_description(self.description),
            'image': self.image,
            'video': self.video,
            'techStack': self.tech_stack.split(',') if self.tech_stack else [],
            'whatYouWillLearn': json.loads(self.what_you_will_learn) if self.what_you_will_learn else [],
            'is_active': self.is_active , # Include is_active in the dictionary
            'requires_subscription': self.requires_subscription  # Include in the dictionary
        }

    def truncate_description(self, description, max_length=200):
        """Truncate description to a maximum length and add ellipsis."""
        if description and len(description) > max_length:
            return description[:max_length] + '...'
        return description

    def archive(self):
        """Archive the course by setting is_active to False."""
        self.is_active = False
        db.session.commit()

    def unarchive(self):
        """Unarchive the course by setting is_active to True."""
        self.is_active = True
        db.session.commit()

class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_text = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)  
    options = db.Column(db.JSON, nullable=False)  
    correct_answer = db.Column(db.String(255), nullable=False)

    def as_dict(self):
        return {
            'id': self.id,
            'questionText': self.question_text,
            'category': self.category,
            'options': self.options,  
            'correctAnswer': self.correct_answer
        }

    def __repr__(self):
        return f"<Question {self.id}: {self.question_text}>"
    

