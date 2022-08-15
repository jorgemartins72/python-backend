from faker import Faker
from .pet_repository import PetRepository
from src.infra.config import DBConnectionHandler
from src.infra.entities import Pets
from src.infra.entities.pets import AnimalTypes

faker = Faker()
pet = PetRepository()
db_conn = DBConnectionHandler()


def test_insert_pet():

    name = faker.name()
    specie = "fish"
    age = faker.random_number(digits=1)
    user_id = faker.random_number(digits=2)

    new_pet = pet.insert_pet(name, specie, age, user_id)
    engine = db_conn.get_engine()
    query_user = engine.execute(
        "SELECT * FROM pets WHERE id='{}'".format(new_pet.id)
    ).fetchone()

    assert new_pet.id == query_user.id
    assert new_pet.name == query_user.name
    assert new_pet.specie == query_user.specie
    assert new_pet.age == query_user.age
    assert new_pet.user_id == query_user.user_id

    engine.execute("DELETE FROM pets WHERE id='{}'".format(new_pet.id))


def test_select_pet():

    pet_id = faker.random_number(digits=3)
    name = faker.name()
    specie = "fish"
    age = faker.random_number(digits=1)
    user_id = faker.random_number(digits=2)

    specie_mock = AnimalTypes("fish")
    data = Pets(id=pet_id, name=name, specie=specie_mock, age=age, user_id=user_id)

    engine = db_conn.get_engine()
    engine.execute(
        "INSERT INTO pets (id, name, specie, age, user_id) VALUES ('{}','{}','{}','{}','{}')".format(
            pet_id, name, specie, age, user_id
        )
    )

    query_pet1 = pet.select_pet(pet_id=pet_id)
    query_pet2 = pet.select_pet(user_id=user_id)
    query_pet3 = pet.select_pet(pet_id=pet_id, user_id=user_id)

    assert data in query_pet1
    assert data in query_pet2
    assert data in query_pet3
