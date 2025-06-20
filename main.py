import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    while True:
        user_input = input("What size sandwich would you like? (small/medium/large/report/off): ").lower()

        if user_input == "off":
            print("Turning off...")
            break
        elif user_input == "report":
            print("Resources available:")
            for item, amount in sandwich_maker_instance.machine_resources.items():
                print(f"{item.title()}: {amount}")
        elif user_input in recipes:
            sandwich = recipes[user_input]
            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                print(f"Cost: ${sandwich['cost']}")
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, sandwich['cost']):
                    sandwich_maker_instance.make_sandwich(user_input, sandwich["ingredients"])
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
