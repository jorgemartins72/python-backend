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

    # engine.execute("DELETE FROM users WHERE id='{}'".format(new_user.id))

    # print()
    # print(new_user)
    # print(query)

    assert new_user.id == query.id
    assert new_user.name == query.name
    assert new_user.password == query.password
