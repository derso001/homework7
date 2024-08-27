from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from table import Base, Student, Group, Lector, Subject, Mark  

# Створення двигуна для підключення до бази даних
engine = create_engine('sqlite:///test.db')
Base.metadata.bind = engine

# Створення сесії
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Функція 1: Знайти 5 студентів із найбільшим середнім балом з усіх предметів
def select_1():
    return session.query(Student.name, func.avg(Mark.value).label('average_grade'))\
        .join(Mark)\
        .group_by(Student.id)\
        .order_by(func.avg(Mark.value).desc())\
        .limit(5).all()

# Функція 2: Знайти студента із найвищим середнім балом з певного предмета
def select_2(subject_name):
    return session.query(Student.name, func.avg(Mark.value).label('average_grade'))\
        .join(Mark)\
        .join(Subject)\
        .filter(Subject.name == subject_name)\
        .group_by(Student.id)\
        .order_by(func.avg(Mark.value).desc())\
        .first()

# Функція 3: Знайти середній бал у групах з певного предмета
def select_3(subject_name):
    return session.query(Group.name, func.avg(Mark.value).label('average_grade'))\
        .join(Student)\
        .join(Mark)\
        .join(Subject)\
        .filter(Subject.name == subject_name)\
        .group_by(Group.id)\
        .all()

# Функція 4: Знайти середній бал на потоці (по всій таблиці оцінок)
def select_4():
    return session.query(func.avg(Mark.value).label('average_grade')).scalar()

# Функція 5: Знайти які курси читає певний викладач
def select_5(lector_name):
    return session.query(Subject.name)\
        .join(Lector)\
        .filter(Lector.name == lector_name)\
        .all()

# Функція 6: Знайти список студентів у певній групі
def select_6(group_name):
    return session.query(Student.name)\
        .join(Group)\
        .filter(Group.name == group_name)\
        .all()

# Функція 7: Знайти оцінки студентів у окремій групі з певного предмета
def select_7(group_name, subject_name):
    return session.query(Student.name, Mark.value, Mark.timestamp)\
        .join(Group)\
        .join(Mark)\
        .join(Subject)\
        .filter(Group.name == group_name, Subject.name == subject_name)\
        .all()

# Функція 8: Знайти середній бал, який ставить певний викладач зі своїх предметів
def select_8(lector_name):
    return session.query(func.avg(Mark.value).label('average_grade'))\
        .join(Subject)\
        .join(Lector)\
        .filter(Lector.name == lector_name)\
        .scalar()

# Функція 9: Знайти список курсів, які відвідує певний студент
def select_9(student_name):
    return session.query(Subject.name)\
        .join(Mark)\
        .join(Student)\
        .filter(Student.name == student_name)\
        .distinct()\
        .all()

# Функція 10: Список курсів, які певному студенту читає певний викладач
def select_10(student_name, lector_name):
    return session.query(Subject.name)\
        .join(Mark)\
        .join(Student)\
        .join(Lector)\
        .filter(Student.name == student_name, Lector.name == lector_name)\
        .all()

if __name__ == "__main__":
    pass