from app import db, app
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from user_policy import UserPolicy
import os
from flask import url_for


class User(db.Model, UserMixin):
    
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50))
    form = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Integer, nullable=False)
    group = db.Column(db.String(50))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id', ondelete='CASCADE'), nullable=False)

    def __repr__(self):
        name = self.last_name + ' ' + self.first_name + ' ' + self.middle_name
        return '%s' % {'name': name,
                'year': self.date,
                'format': self.form,
                'group': self.group}

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def is_admin(self):
        return self.role_id == 1
    
    @property
    def is_moder(self):
        return self.role_id == 2

    def can(self, action):
        users_policy = UserPolicy()
        method = getattr(users_policy, action, None)
        if method is not None:
            return method()
        return False


class Role(db.Model):
    
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(100))

    def __repr__(self):
        return '<role: %r>' % self.role_name

class Plan(db.Model):
    __tablename__ = 'plan'
    id = db.Column(db.Integer, primary_key=True)
    spec_name = db.Column(db.String(200), nullable=False)
    disc_name = db.Column(db.String(200), nullable=False)
    sem = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    exam = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<discipline: %r>' % self.disc_name

class Goals(db.Model):
    __tablename__ = 'goals'
    id = db.Column(db.Integer, primary_key=True)
    sem = db.Column(db.Integer, nullable=False)
    student = db.Column(db.Integer, nullable=False)
    disc_name = db.Column(db.Integer, nullable=False)
    goal = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return '<goal: %r>' % self.id