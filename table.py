import faker
from datetime import date
from random import randint
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


engine = create_engine('sqlite:///test.db', echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()

fake_data = faker.Faker()


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



Base.metadata.create_all(engine)
Base.metadata.bind = engine

def create_groups():
    group_names=["11СОТ","12СОТ","13СОТ"]
    for group_name in group_names:
        new_group = Group(name=group_name)
        session.add(new_group)
    session.commit()

def create_students():
    for group in session.query(Group).all():
        for _ in range(10):
            new_student = Student(name=fake_data.name(), groups_id_fn=group.id)
            session.add(new_student)
    session.commit()

def create_lectors():
    for _ in range(5):
        new_lector = Lector(name=fake_data.name())
        session.add(new_lector)
    session.commit()

def create_subjects():    
    subjects_name_list = ["Філософія", "Вища математика", "Психологія", "Педагогіка", "Технології"]
    for lector in session.query(Lector).all():
        new_subject = Subject(name=subjects_name_list[lector.id-1], lector_id_fn=lector.id)
        session.add(new_subject)
    session.commit()

def create_marks():
    for student in session.query(Student).all():
        for subject in session.query(Subject).all():
            for _ in range(4):
                new_mark = Mark(value=str(randint(15,25)), timestamp=date(2023,randint(1,3),randint(1,28)), student_id_fn=student.id, subject_id_fn=subject.id)
                session.add(new_mark)
    session.commit()
                    

if __name__ == '__main__':
    # create_groups()
    # create_students()
    # create_lectors()
    # create_subjects()
    create_marks()