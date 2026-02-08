# Closure is a function having acces to the scope of its parent
# function after the parent function has returned

def parent_function(person, coins):
    # coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins.")
        
    return play_game

dzaky = parent_function("Dzaky", 3)
gladys = parent_function("Gladys", 5)

dzaky()
dzaky()

gladys()

dzaky()