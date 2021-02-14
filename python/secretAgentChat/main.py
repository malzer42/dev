# File: main.py
from menu import menu

def main():
    try:
        menu()
    except FileNotFoundError as file_not_found_error:
        print(file_no_found_error)
    else:
        print("")
    finally:
        print("Program Ended Successfully")

    
if __name__ == "__main__":
    main()
