from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


engine = create_engine('sqlite:///test.db', echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()

class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True)
    name = Column(String, primary_key=False)

    students = relationship('Student', back_populates='group')

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    groups_id_fn = Column(Integer, ForeignKey('groups.id'), nullable=False)

    group = relationship('Group', back_populates='students')
    marks = relationship('Mark', back_populates='student')

class Lector(Base):
    __tablename__ = 'lectors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    subjects = relationship('Subject', back_populates='lector')

class Subject(Base):
    __tablename__ = 'subjects'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    lector_id_fn = Column(Integer, ForeignKey('lectors.id'), nullable=False)

    lector = relationship('Lector', back_populates='subjects')
    marks = relationship('Mark', back_populates='subject')

class Mark(Base):
    __tablename__ = 'marks'
    
    id = Column(Integer, primary_key=True)
    value = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=True)
    student_id_fn = Column(Integer, ForeignKey('students.id'), nullable=False)
    subject_id_fn = Column(Integer, ForeignKey('subjects.id'), nullable=False)

    student = relationship('Student', back_populates='marks')
    subject = relationship('Subject', back_populates='marks')
              

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine