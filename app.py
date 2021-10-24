import database
import sys
import os

MENU_PROMPT = """-- Coffee Bean App --

Please choose one of these options:

1.  Add a new coffee bean
2.  View all coffee beans
3.  Find a coffee bean by name
4.  See which preparation method is best for a coffee bean
5.  See which preparation method is worst for a coffee bean
6.  Get all preparation methods
7.  Export Database to CSV
8.  Import Database from CSV
9.  Restart Application
10. Quit

Your selection is: """


def restart():
    print("\nRestarting application...")
    filename = __file__.split("\\")
    os.system("python "+filename[-1])
    sys.exit()


def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (True):
        user_input = input('\n'+MENU_PROMPT)

        # Add a new coffee bean
        if user_input == '1':
            name = input("Enter the name of the coffee bean: ")
            method = input("Enter the method of preparation: ")
            rating = int(input("Enter the rating of the coffee bean: "))
            database.add_bean(connection, name, method, rating)
            print("\nCoffee bean added successfully!")

        # View all coffee beans
        elif user_input == '2':
            beans = database.get_all_beans(connection)
            columns = database.get_column_names(connection)
            print(columns[1:])
            for bean in beans:
                print(f"\n{bean[1]} ({bean[2]}) - {bean[3]}/100")

        # Find a coffee bean by name
        elif user_input == '3':
            name = input("Enter the name of the coffee bean: ")
            beans = database.get_beans_by_name(connection, name)
            for bean in beans:
                print(f"\n{bean[1]} ({bean[2]}) - {bean[3]}/100")

        # See which preparation method is best for a coffee bean
        elif user_input == '4':
            name = input("Enter the name of the coffee bean: ")
            best_method = database.get_best_preparation_for_bean(
                connection, name)
            print(
                f"The best preparation method for {name} is : {best_method[2]}")

        # See which preparation method is worst for a coffee bean
        elif user_input == '5':
            name = input("Enter the name of the coffee bean: ")
            worst_method = database.get_worst_preparation_for_bean(
                connection, name)
            print(
                f"The worst preparation method for {name} is : {worst_method[2]}")

        # Get All Preperation Methods
        elif user_input == '6':
            methods = database.get_all_preparation_methods(connection)
            for method in methods:
                print(method)

        # Export Database to CSV
        elif user_input == '7':
            database.export_database_to_csv(connection)
            print("\nDatabase exported successfully!")

        # Import Database from CSV
        elif user_input == '8':
            new_additions = database.import_database_from_csv(connection)
            if(new_additions == 0):
                print("\nDatabase already up to date!")
            else:
                print(f"\n{new_additions} new entries added to the database!")

        # Restart Application
        elif user_input == '9':
            restart()

        # Quit
        elif user_input == '10':
            print("\nQuitting application...")
            sys.exit()

        # Invalid Input
        else:
            print("Please enter a valid option.")


menu()
