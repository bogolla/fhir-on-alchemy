from sqlalchemy.dialects.postgresql import JSON

from app import db
from sqlalchemy import Column, String, Integer


class Result(db.Model):
    __tablename__ = 'results'
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    url = Column(String)
    result_all = Column(JSON)
    result_no_stop_words = Column(JSON)

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)
