class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))  # 0.25
        dimes = int(input("How many dimes?: "))  # 0.10
        nickels = int(input("How many nickels?: "))  # 0.05
        pennies = int(input("How many pennies?: "))  # 0.01
        total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
        return round(total, 2)

    def transaction_result(self, coins, cost):
        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Change: ${change}")
            print("Payment accepted.")
            return True
        else:
            print("Not enough funds.")
            return False
