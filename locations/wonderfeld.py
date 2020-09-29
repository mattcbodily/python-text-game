wonderfeld_monsters = (
    {'monster': 'Goblin', 'health': 5, 'attack': 2, 'defense': 1, 'experience': 3, 'gold_max': 5},
    {'monster': 'Warthog', 'health': 3, 'attack': 3, 'defense': 1, 'experience': 2, 'gold_max': 3}
)

def wonderfeld_shop(player, play_fn):
    print('Welcome to the Wonderfeld Shop! What would you like to buy?')
    print('1: Potion for 5 gold')
    print('2: Dagger for 10 gold')
    print('3: Armor for 15 gold')
    print('4: Leave Shop')
    ans = input('Select an option: ')

    if ans == '1':
        if player.gold >= 5:
            player.gold -= 5
            player.inventory.append({'Item': 'Potion', 'Qty': 1})
            print('Thank you for purchase!')
            wonderfeld_shop(player, play_fn)
        else:
            print("You don't have enough gold to buy this item...")
            wonderfeld_shop(player, play_fn)
    elif ans == '2':
        if player.gold >= 10:
            player.gold -= 10
            player.inventory.append({'Item': 'Dagger', 'Qty': 1})
            print('Thank you for your purchase!')
            wonderfeld_shop(player, play_fn)
        else:
            print("You don't have enough gold to buy this item...")
            wonderfeld_shop(player, play_fn)
    elif ans == '3':
        if player.gold >= 15:
            player.gold -= 15
            player.inventory.append({'Item': 'Armor', 'Qty': 1})
            print('Thank you for your purchase!')
            wonderfeld_shop(player, play_fn)
        else:
            print("You don't have enough gold to buy this item...")
            wonderfeld_shop(player, play_fn)
    elif ans == '4':
        print('See you soon!')
        play_fn(player)
