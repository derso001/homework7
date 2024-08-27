import faker
from datetime import date
from random import randint
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from table import *

engine = create_engine('sqlite:///test.db', echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()

fake_data = faker.Faker()

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

if __name__ == "__main__":
    create_groups()
    create_lectors()
    create_students()
    create_subjects()
    create_marks()