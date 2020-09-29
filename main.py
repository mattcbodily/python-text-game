class Hero:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.experience = 0
        self.health = 10
        self.attack = 3
        self.defense = 2
        self.gold = 0
        self.inventory = []

def base_game_play(player):
    print('You start your journey in the town of Wonderfeld. It is a small town located by a large forest.')
    print('What would you like to do?')
    print('1: Hunt monsters in the forest')
    print('2: Visit the town shop')
    print('3: Travel')
    print('4: View your stats')
    print('5: View your inventory')
    ans = input('Select an option: ')

    if ans == '1':
        print('Fight logic in progress')
    elif ans == '2':
        print('Shop logic in progress')
    elif ans == '3':
        print('Travel logic in progress')
    elif ans == '4':
        print('Here are your stats:')
        print('Level:', player.level)
        print('Experience:', player.experience)
        print('Health:', player.health)
        print('Attack:', player.attack)
        print('Defense:', player.defense)
    elif ans == '5':
        print('Here is your inventory')
        print('Gold:', player.gold)
        print('Inventory:', player.inventory)
        

print('Welcome adventurer!')
name = input('What is your name? ')
if name:
    player = Hero(name)
    print('Welcome,', name)
    print('Here are your stats:')
    print('Level:', player.level)
    print('Experience:', player.experience)
    print('Health:', player.health)
    print('Attack:', player.attack)
    print('Defense:', player.defense)
    print('Gold:', player.gold)
    base_game_play(player)

