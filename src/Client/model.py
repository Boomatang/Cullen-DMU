from pony.orm import *

db = Database()


class Client(db.Entity):
    name = Required(str)
    logo = Optional(str)

    @staticmethod
    def add_client(name, logo):
        with db_session:
            if logo is not None:
                Client(name=name, logo=logo)
            else:
                Client(name=name)

    @staticmethod
    def select_clients():
        with db_session:
            return select(c for c in Client).order_by(Client.name)[:]

    @staticmethod
    @db_session
    def get_client_by_name(name):
        return Client.get(name=name)

    def __repr__(self):
        return "<Client : {}>".format(self.name)

    def __lt__(self, other):
        return self.name < other.name

db.bind('sqlite', 'client_db.sqlite', create_db=False)
db.generate_mapping(create_tables=True)


def create_model():
    db.bind('sqlite', 'client_db.sqlite', create_db=True)
    db.generate_mapping(create_tables=True)

if __name__ == "__main__":
    create_model()