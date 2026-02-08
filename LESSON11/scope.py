name = "Dzaky"
count = 1

def another():
    color = "green"
    global count
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "grey"
        print(color)
        print(name)

    greeting("Dzaky")

another()