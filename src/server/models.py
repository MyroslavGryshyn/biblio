# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
#
# from run import app
# import settings
#
# app.config.from_object(settings.SQLALCHEMY_DATABASE_URI)
#
# db = SQLAlchemy(app)
#
# class Book(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     book_name = db.Column(db.String(80), unique=True)
#     book_author = db.Column(db.String(120), unique=True)
#     book_status = db.Column(db.Boolean, unique=False, default=True)
#
#     def __init__(self, book_name, book_author, book_status):
#         self.book_name = book_name
#         self.book_author = book_author
#         self.book_status = book_status
#
#     def __repr__(self):
#         return '<Book %s>' % self.book_name
