from sqlalchemy import Column, Integer, String
from api_demo.database import Base


class Books(Base):

    __tablename__ = 'BOOKS'

    id = Column(String(100), primary_key=True)
    title = Column(String(300), unique=True)
    image_url = Column(String(200))
    image = Column(String(200))
    author = Column(String(200))
    book_type = Column(Integer)
    section = Column(String(200))

    def __init__(self, id=None, title=None, image=None, image_url=None, author=None, book_type=None, section=None):
        self.id = id
        self.title = title
        self.image = image
        self.image_url = image_url
        self.author = author
        self.book_type = book_type
        self.section = section

    def __repr__(self):
        return f"<book {self.id} title: '{self.title}'"
