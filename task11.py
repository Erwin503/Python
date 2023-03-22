class human:
    def __init__(self):
        self.height = 0
        self.name = ("Default")
        self.position = 0
    def walk(self, dist):
        self.position += dist
    def grow(self):
        self.height += 1

class student(human):
    def __init__(self):
        self.name = "Default"
        self.position = 0
        self.height = 0
        self.isStudying = False
    def enter(self):
        self.isStudying = True
    def graduate(self):
        self.isStudying = False
    def leave(self):
        self.isStudying = False

Ervin = human()
print(Ervin.position)
Ervin.walk(900)
print(Ervin.position)
Ivan = student()
print(Ivan.position)
Ivan.walk(90)
print(Ivan.position)
Ivan.enter()
print(Ivan.isStudying)