from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Contact(Base):

    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=True)


class Phone(Base):

    __tablename__ = 'phones'

    contact_id = Column(Integer, ForeignKey(
        'contacts.id', ondelete="CASCADE", onupdate="CASCADE"))
    phone = Column(String(15), primary_key=True)