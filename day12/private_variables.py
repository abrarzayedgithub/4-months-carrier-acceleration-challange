class user:
    def __init__(self,passward):
        self.__passward = passward #private passward
    def showPassward(self):
        print(self.__passward)
x = user('abrar111')
x.showPassward()