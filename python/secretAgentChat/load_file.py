def load_file(filename):
    """Function to load a sheet from OTP."""
    try:
        with open(filename, "r") as fin:
            contents = fin.read().splitlines()
        return contents
    except FileNotFoundError as file_not_found_error:
        print(file_not_found_error)
    else:
        print("")
    finally:
        print(f"\n{filename} file loaded successfully\n" )
        

def save_file(filename, data):
    """Function to save the data."""
    try:
        with open(filename, "a+") as fout:
            fout.write(data)
    except FileNotFoundError as file_not_found_error:
        print(file_not_found_error)
    else:
        print("")
    finally:
        print("Processing...\n")
