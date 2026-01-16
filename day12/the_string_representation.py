class user:
    def __init__(self):
        self.name = "DATA SCIENCE"
    def __str__(self):
        return f"user: {self.name}"
    def __repr__(self):
        return f"user: {self.name} repr"
x = user()
print(x)
print(repr(x))