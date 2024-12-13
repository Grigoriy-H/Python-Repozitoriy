import os
from sqlalchemy.orm import sessionmaker
import pytest
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, insert, select


@pytest.fixture(scope="module")
def engine():


    db_url = "postgresql://Aks:ks180@localhost:5432/QA"
    return create_engine(db_url)
   


@pytest.fixture
def connection(engine):
    conn = engine.connect()
    yield conn
    conn.close()


@pytest.fixture
def session(connection):
    Session = sessionmaker(bind=connection)
    sess = Session()
    try:
        yield sess
    finally:
        sess.close()


def test_add_subject(session):
    subject_table = Table(
        'subject',
        MetaData(),
        Column('subject_id', Integer, primary_key=True),
        Column('subject_title', String),
    )

    new_subject = {'subject_id': 16, 'subject_title': 'Art'}
    insert_stmt = subject_table.insert().values(**new_subject)
    session.execute(insert_stmt)
    session.commit()

    result = (
        session.query(subject_table)
        .filter_by(subject_id=new_subject['subject_id'])
        .first()
    )
    assert result.subject_title == new_subject['subject_title']

    delete_stmt = subject_table.delete().where(
        subject_table.c.subject_id == new_subject['subject_id']
    )
    session.execute(delete_stmt)
    session.commit()

def test_update_student(session):
    student_table = Table(
        'student',
        MetaData(),
        Column('user_id', Integer, primary_key=True),
        Column('level', String),
        Column('education_form', String),
        Column('subject_id', Integer),
    )
    new_student = {
        "user_id": 1,
        "level": "Undergraduate",
        "education_form": "Full-time",
        "subject_id": 101,
    }


    # Выполняем вставку данных
    insert_stmt = insert(student_table).values(new_student)
    session.execute(insert_stmt)

    # Проверяем, что данные успешно добавлены
    select_stmt = select(student_table).where(student_table.c.user_id == new_student["user_id"])
    result = session.execute(select_stmt).fetchone()

    # Ассерт: проверяем, что результат не None и данные совпадают
    assert result is not None, "Студент не был добавлен в таблицу."


    update_data = {'user_id': 11548, 'level': 'Advanced'}
    update_stmt = (
        student_table.update()
        .where(student_table.c.user_id == update_data['user_id'])
        .values(level=update_data['level'])
    )
    session.execute(update_stmt)
    session.commit()

    result = (
        session.query(student_table)
        .filter_by(user_id=update_data['user_id'])
        .first()
    )
    assert result.level == update_data['level']

    rollback_data = {'level': 'Upper-Intermediate'}
    rollback_stmt = (
        student_table.update()
        .where(student_table.c.user_id == update_data['user_id'])
        .values(**rollback_data)
    )
    session.execute(rollback_stmt)
    session.commit()


def test_delete_teacher(session):
        teacher_table = Table(
            'teacher',
            MetaData(),
            Column('teacher_id', Integer, primary_key=True),
            Column('email', String),
            Column('group_id', Integer),
        )

        new_teacher_data = {"email": "test_teacher@example.com", "group_id": 123}
        insert_stmt = insert(teacher_table).values(new_teacher_data)
        result = session.execute(insert_stmt)

        # Получаем ID созданного учителя
        created_teacher_id = result.scalar()

        delete_data = {"teacher_id": created_teacher_id}
        delete_stmt = teacher_table.delete().where(
            teacher_table.c.teacher_id == delete_data["teacher_id"])
        result = session.execute(delete_stmt)

        select_stmt = teacher_table.select().where(
            teacher_table.c.teacher_id == delete_data["teacher_id"]
        )
        result = session.execute(select_stmt).fetchone()

        # Ассерт: запись должна быть None
        assert result is None, f"Учитель с ID {delete_data['teacher_id']} все еще существует!"
        print("Учитель успешно удален.")