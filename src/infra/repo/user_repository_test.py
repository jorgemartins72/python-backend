from faker import Faker
from src.infra.config import DBConnectionHandler
from .user_repository import UserRepository

faker = Faker()
user = UserRepository()
db_conn = DBConnectionHandler()


def test_insert_user():

    name = faker.name()
    password = faker.word()
    engine = db_conn.get_engine()

    new_user = user.insert_user(name, password)
    query = engine.execute(
        "SELECT * FROM users WHERE id='{}'".format(new_user.id)
    ).fetchone()

    engine.execute("DELETE FROM users WHERE id='{}'".format(new_user.id))

    # print()
    # print(new_user)
    # print(query)

    assert new_user.id == query.id
    assert new_user.name == query.name
    assert new_user.password == query.password


def test_selec_user():
    name = faker.name()
    password = faker.word()
    engine = db_conn.get_engine()

    new_user = user.insert_user(name, password)

    query_user1 = user.select_user(user_id=new_user.id)
    query_user2 = user.select_user(name=new_user.name)
    query_user3 = user.select_user(user_id=new_user.id, name=new_user.name)

    assert new_user in query_user1
    assert new_user in query_user2
    assert new_user in query_user3

    engine.execute("DELETE FROM users WHERE id='{}'".format(new_user.id))
