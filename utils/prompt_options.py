from constants.strings import MENU_PROMPT
from database import operations
from utils.utils import restart

connection = operations.connect()
operations.create_tables(connection)


def add_new_coffee_bean():
    name = input("Enter the name of the coffee bean: ")
    method = input("Enter the method of preparation: ")
    rating = int(input("Enter the rating of the coffee bean: "))
    operations.add_bean(connection, name, method, rating)
    print("\nCoffee bean added successfully!")


def view_all_coffee_beans():
    beans = operations.get_all_beans(connection)
    columns = operations.get_column_names(connection)
    print(columns[1:])
    for bean in beans:
        print(f"\n{bean[1]} ({bean[2]}) - {bean[3]}/100")


def find_coffee_bean_by_name():
    name = input("Enter the name of the coffee bean: ")
    beans = operations.get_beans_by_name(connection, name)
    for bean in beans:
        print(f"\n{bean[1]} ({bean[2]}) - {bean[3]}/100")


def best_preperation_method():
    name = input("Enter the name of the coffee bean: ")
    best_method = operations.get_best_preparation_for_bean(
        connection, name)
    print(
        f"The best preparation method for {name} is : {best_method[2]}")


def worst_preperation_method():
    name = input("Enter the name of the coffee bean: ")
    worst_method = operations.get_worst_preparation_for_bean(
        connection, name)
    print(
        f"The worst preparation method for {name} is : {worst_method[2]}")


def get_all_preperation_methods():
    methods = operations.get_all_preparation_methods(connection)
    for method in methods:
        print(method)


def export_csv():
    operations.export_database_to_csv(connection)
    print("\nDatabase exported successfully!")


def import_csv():
    new_additions = operations.import_database_from_csv(connection)
    if (new_additions == 0):
        print("\nDatabase already up to date!")
    else:
        print(f"\n{new_additions} new entries added to the database!")


def restart_app():
    restart
