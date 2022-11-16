
class User:
    def __init__(self, username, name, email) -> None:
        self.username = username
        self.name = name
        self.email = email
        print("User created")

    def __repr__(self) -> str:
        return f"User(username={self.username}, name={self.name}, email={self.email}"

    def __str__(self) -> str:
        return self.__repr__()

class UserDatabase:
    def __init__(self) -> None:
        self.users = []

    def insert(self, user):
        pass

    def search(self, username):
        pass

    def update(self, username):
        pass

    def list_all(self):
        pass


abayomiganiy = User("abayomiganiy", "Ganiu Aderibigbe", "aderibigbeganiu@@gmail.com")
akinmiday = User("akinmiday", "Hakeem Akinola", "akinolaolamide@@gmail.com")
youngsaint = User("youngsaint", "Somod Aderibigbe", "aderibigbesomod@@gmail.com")
bob = User("bob", "Adeniyi Aderibigbe", "aderibigbeadeniyi@@gmail.com")

users = [abayomiganiy, akinmiday, youngsaint, bob]

