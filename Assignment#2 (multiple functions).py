print("The apple = 20 pesos orange = 25 pesos")

appleCost = 20
orangeCost = 25

def order():
    orderedApples = int(input("How many apples do you want to buy?: "))
    orderedOranges = int(input("How many oranges do you want to buy?: "))
    return orderedApples, orderedOranges,

def calculate(appleCost, appleF, orangeCost, orangeF):
    totalF = (appleCost*appleF) + (orangeCost*orangeF)
    return totalF

def display(totalF):
    print(f"The total amount is {totalF}.")

apple, orange, = order()
total = calculate(appleCost, apple, orangeCost, orange)
display(total)