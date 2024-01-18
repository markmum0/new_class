class Character:
    power_boost = 1.50
    depleted = 0

    def __init__(self, name, power, health, catchphrase):
        self.name = name
        self.power = power
        self.health = int(health)
        self.catchphrase = catchphrase

    def intro(self):
        return '{} : {}'.format(self.name.capitalize(), self.catchphrase.upper())

    def power_up(self):
        self.health = int(self.health * self.power_boost)
        return '{} : {} : {}'.format(self.name, self.health, 'Check out the new new')


player1 = Character('Kang', 'pruning', '100', 'I am your doom')
player2 = Character('Bruce Wayne', 'Batman', '200', 'I AM VENGEANCE')

# import time

# print(Character.intro(player1))
# time.sleep(2)
# print(Character.intro(player2))

print(player1.power_boost)
print(Character.defeat(player2))
