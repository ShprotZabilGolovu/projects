class Ball:

    def __init__(self, mass):

        self.mass = mass
        self.image = 'hexagone'
        self.x = 0
        self.y = 0

    # Методы, реализующие поведение экземпляров
    # self – подразумеваемый экземпляр
    def drop(self):
        print('Я подбросился')
        self.y = 2
        self.kick()

    def kick(self):
        print('Я пнулся')
        self.x += 1

    def fail(self):
        self.mass = self.mass - 0.1

if __name__ == '__main__':
    ball = Ball(0.5)
    ball.drop()
    ball.kick()
    ball.fail()
    print(ball.x)
    print(ball.mass)

