#
# # name = input("What is your name ? \n")
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}")
#     print(f"Bye {name}")
#
# greet_with_name("Sean")
#

# def life_in_weeks(age):
#     weeks_left = (90 - age) * 52
#     print(f"You have {weeks_left} weeks left.")
#
# life_in_weeks(36)


def greet_with(name, location):
    print(f"Welcome {name} come from {location}")

greet_with("sean", "VietNam")


def stock_caculation(stock_quantity, unit_price):
    return stock_quantity * unit_price

print(stock_caculation(4500, 148))