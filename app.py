import sys

from constants.strings import MENU_PROMPT
from utils.prompt_options import (add_new_coffee_bean, best_preperation_method,
                                  export_csv, find_coffee_bean_by_name,
                                  get_all_preperation_methods, import_csv,
                                  view_all_coffee_beans,restart_app,
                                  worst_preperation_method)

def menu():

    while (True):
        user_input = input('\n'+MENU_PROMPT)

        if user_input == '1':
            # Add a new coffee bean
            add_new_coffee_bean()

        elif user_input == '2':
            # View all coffee beans
            view_all_coffee_beans()

        elif user_input == '3':
            # Find a coffee bean by name
            find_coffee_bean_by_name()

        elif user_input == '4':
            # See which preparation method is best for a coffee bean
            best_preperation_method()

        elif user_input == '5':
            # See which preparation method is worst for a coffee bean
            worst_preperation_method()

        elif user_input == '6':
            # Get All Preperation Methods
            get_all_preperation_methods()

        elif user_input == '7':
            # Export operations to CSV
            export_csv()

        elif user_input == '8':
            # Import Database from CSV
            import_csv()

        elif user_input == '9':
            # Restart Application
            restart_app()

        elif user_input == '10':
            # Quit
            print("\nQuitting application...")
            sys.exit()

        else:
            # Invalid Input
            print("Please enter a valid option.")


if __name__ == '__main__':

    menu()
