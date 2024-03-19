import json
import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def load_qcodes():
    """Loads Q-codes from a JSON file."""
    try:
        with open('qcodes.json', 'r') as file:
            return json.load(file)
    except Exception as e:
        print("Error loading 'qcodes.json':", e)
        exit()

def search_qcodes(qcodes, query):
    """Searches Q-codes by code or keyword."""
    results = []
    for qcode in qcodes:
        if query.lower() in qcode['code'].lower() or any(query.lower() in kw.lower() for kw in qcode['keywords']):
            results.append(qcode)
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
   ____                    ____  _____   _____ 
  / __ \                  / __ \|  __ \ / ____|
 | |  | |_ __   ___ _ __ | |  | | |__) | |     
 | |  | | '_ \ / _ \ '_ \| |  | |  _  /| |     
 | |__| | |_) |  __/ | | | |__| | | \ \| |____ 
  \____/| .__/ \___|_| |_|\___\_\_|  \_\\_____|
''''''''''|_|'''''''''''''''''''''''''''''''''''''                                     
    """.strip()  # Replace this with your ASCII art
    print_with_border(ascii_art)

def prompt_for_search():
    """Prompts user for search input, displaying within borders."""
    query = input("| Enter Q-code or keyword to search: ").strip()
    return query

def display_results(results):
    """Displays the search results, formatted within borders."""
    result_text = "\n".join([f"Code: {result['code']} - Meaning: {result['meaning']}\nKeywords: {', '.join(result['keywords'])}" for result in results]) or "No results found."
    print_with_border(result_text)
    input("\nPress Enter to go back...")

def main_menu():
    """Displays the main menu and handles user input with borders."""
    qcodes = load_qcodes()
    while True:
        clear_screen()
        print_openqrc_ascii_art()
        menu = "1. Search Q-codes\n2. Exit"
        print_with_border(menu)
        choice = input("| Enter your choice: ").strip()

        if choice == '1':
            clear_screen()
            print_openqrc_ascii_art()
            query = prompt_for_search()
            results = search_qcodes(qcodes, query)
            clear_screen()
            print_openqrc_ascii_art()
            display_results(results)
        elif choice == '2':
            clear_screen()
            print_openqrc_ascii_art()
            print_with_border("Exiting OpenQRC Tool.")
            break
        else:
            clear_screen()
            print_openqrc_ascii_art()
            print_with_border("Invalid choice, please try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()
