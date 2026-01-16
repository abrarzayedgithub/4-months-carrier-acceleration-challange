from datetime import date
class user:
    def __init__(self):
        self.__birthyear = 2001

    @property
    def fake(self):
        return date.today().year - self.__birthyear
x = user()
y = x.fake
print(y)
