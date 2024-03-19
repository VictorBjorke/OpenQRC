import json
import os
import sys

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def load_qcodes():
    """Loads Q-codes from a JSON file."""
    base_path = os.path.dirname(__file__)
    json_path = os.path.join(base_path, 'qcodes.json')
    
    try:
        with open(json_path, 'r') as file:
            qcodes = json.load(file)
            if isinstance(qcodes, dict):  # Ensure qcodes is a dictionary
                return qcodes
            else:
                print("Error: 'qcodes.json' is not properly formatted as a dictionary.")
                exit()
    except FileNotFoundError:
        return {}  # Return an empty dictionary if the file does not exist
    except Exception as e:
        print(f"Error loading 'qcodes.json': {e}")
        exit()

def save_qcodes(qcodes):
    """Saves Q-codes to a JSON file."""
    base_path = os.path.dirname(__file__)
    json_path = os.path.join(base_path, 'qcodes.json')
    with open(json_path, 'w') as file:
        json.dump(qcodes, file, indent=4)

def add_new_qcode(qcodes):
    """Adds a new Q-code to the database."""
    print("\nAdd a New Q-Code")
    qcode = input("Enter the Q-code (e.g., QSO): ").upper()
    
    if qcode in qcodes:
        print("This Q-code already exists in the database.")
    else:
        meaning = input("Enter the meaning of the Q-code: ")
        keywords = [input(f"Enter keyword {i}: ") for i in range(1, 4)]
        
        qcodes[qcode] = {'meaning': meaning, 'keywords': keywords}
        save_qcodes(qcodes)
        print(f"{qcode} added to the database.")
    input("Press Enter to continue...")

def search_qcodes(qcodes, query):
    """Searches Q-codes by code or keyword."""
    results = []
    for code, details in qcodes.items():
        if query.lower() in code.lower() or any(query.lower() in kw.lower() for kw in details['keywords']):
            results.append({'code': code, 'meaning': details['meaning'], 'keywords': details['keywords']})
    return results

def print_with_border(content):
    """Prints content with a border around it."""
    width = 70
    print("+" + "-" * (width - 2) + "+")
    for line in content.split("\n"):
        print("|" + line.center(width - 2) + "|")
    print("+" + "-" * (width - 2) + "+")

def print_openqrc_ascii_art():
    """Prints 'OpenQRC' in ASCII art with a border."""
    ascii_art = """
  ####      ####     #####  ##   ##    ####     ####     ####
 ##  ##    ##  ##   ##      ###  ##   ##  ##   ##  ##   ##  ##
 ##   ##  ##   ##  ##       #### ##  ##   ##  ##   ##  ##
 ##   ##  ######   ######   #######  ##   ##  ######   ##
 ##   ##  ##       ##       ## ####  ##   ##  ####     ##   ##
 ##   ##  ##       ##       ##  ###   #####   ## ##    ##  ##
  #####   ##       #######  ##   ##      ##   ##  ##    ####
    """
    print_with_border(ascii_art)

def prompt_for_search():
    """Prompts user for search input, displaying within borders."""
    query = input("| Enter Q-code or keyword to search: ").strip()
    return query

def display_results(results):
    """Displays the search results, formatted within borders."""
    if results:
        for result in results:
            print_with_border(f"Code: {result['code']} - Meaning: {result['meaning']}\nKeywords: {', '.join(result['keywords'])}")
    else:
        print_with_border("No results found.")
    input("\nPress Enter to go back...")

def main_menu():
    """Displays the main menu and handles user input with borders."""
    qcodes = load_qcodes()
    while True:
        clear_screen()
        print_openqrc_ascii_art()
        menu = "1. Search Q-codes\n2. Add New Q-code\n3. Exit"
        print_with_border(menu)
        choice = input("| Enter your choice: ").strip()

        if choice == '1':
            clear_screen()
            print_openqrc_ascii_art()
            query = prompt_for_search()
            results = search_qcodes(qcodes, query)
            clear_screen()
            display_results(results)
        elif choice == '2':
            clear_screen()
            add_new_qcode(qcodes)
            qcodes = load_qcodes()  # Reload the qcodes to include the newly added ones
        elif choice == '3':
            print_with_border("Exiting OpenQRC Tool.")
            break
        else:
            clear_screen()
            print_openqrc_ascii_art()
            print_with_border("Invalid choice, please try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()