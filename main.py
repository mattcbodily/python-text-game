import random
import locations.wonderfeld

class Hero:
    def __init__(self, name):
        self.name = name
        self.location = 'Wonderfeld'
        self.level = 1
        self.experience = 0
        self.health = 10
        self.attack = 3
        self.defense = 2
        self.gold = 0
        self.inventory = []

def base_game_play(player):
    print('What would you like to do?')
    print('1: Hunt monsters in the forest')
    print('2: Visit the town shop')
    print('3: Travel')
    print('4: View your stats')
    print('5: View your inventory')
    ans = input('Select an option: ')

    if ans == '1':
        start_fight(player)
    elif ans == '2':
        shop_logic(player)
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

def fight_logic(player, monster):
    print('What would you like to do?')
    print('1: Attack')
    print('2: Use Item')
    print('3: Run Away')
    ans = input('Select an option: ')

    if ans == '1':
        monster["health"] -= player.attack

        if monster["health"] <= 0:
            print('You defeated the', monster["monster"])
            print('You gained', monster["experience"], 'experience')
            gold = random.randint(0, monster["gold_max"])
            print('You found', gold, 'gold!')

            player.experience += monster["experience"]
            player.gold += gold
            base_game_play(player)
        else:
            fight_logic(player, monster)
    elif ans == '2':
        print('Inventory logic in progress')
    elif ans == '3':
        print('You ran away!')
        base_game_play(player)

def start_fight(player):
    if player.location == 'Wonderfeld':
        monster = random.choice(locations.wonderfeld.wonderfeld_monsters)
    
    print('You come across a', monster["monster"])
    fight_logic(player, monster)

def shop_logic(player):
    if player.location == 'Wonderfeld':
        locations.wonderfeld.wonderfeld_shop(player, base_game_play)  

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
    print('You start your journey in the town of Wonderfeld. It is a small town located by a large forest.')
    base_game_play(player)