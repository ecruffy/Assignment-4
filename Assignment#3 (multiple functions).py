def askUser():
    moneyF = int(input("Enter the amount of money you have:"))
    appleCostF = int(input("Enter the price of an apple: "))
    return moneyF, appleCostF

def calculate(moneyF, appleCostF):
    appleNumberF = moneyF // appleCostF
    changeF = moneyF % appleCostF
    return appleNumberF, changeF

def displayOutput(appleNumberF, changeF):
    print(f"You can buy {appleNumberF} apples and your change is {changeF} pesos.")

money, appleCost = askUser()
appleNumber, change = calculate(money, appleCost)
displayOutput(appleNumber, change)