from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import time


coffee_on = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while coffee_on:
    customer_choice = input('What do you want? \n1.)latte\n2.)espresso\n3.)cappuccino\n')




    if customer_choice == 'report':
        coffee_maker.report()
        money_machine.report()


    elif customer_choice == 'quit':
        coffee_on = False
    else:
        drink = menu.find_drink(customer_choice)
        if coffee_maker.is_resource_sufficient(drink) :
            if money_machine.make_payment(drink.cost) :
                coffee_maker.make_coffee(drink)

