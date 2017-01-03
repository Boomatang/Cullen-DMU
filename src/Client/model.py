from pony.orm import *

db = Database()


class Client(db.Entity):
    name = Required(str)
    logo = Optional(str)


def create_model():
    db.bind('sqlite', 'client_db.sqlite', create_db=True)
    db.generate_mapping(create_tables=True)

if __name__ == "__main__":
    create_model()