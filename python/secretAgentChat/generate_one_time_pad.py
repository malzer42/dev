from random import randint



def generate_otp(nSheets, nCharacters):
    """ 
    Function to generate a One Time Pad.
    @param nSheets: number of sheets in the pad
    @nCharacters: number of characters that each sheet can encrypt
    """
    try:
        print("Processing, please wait ...\n")
        for sheet in range(nSheets):
            with open("otp" +str(sheet)+".txt", "w") as fout:
                print(f"opt{str(sheet)}.txt file generated")
                for i in range(nCharacters):
                    fout.write(str(randint(0,26)) + "\n" )
    
    except IOError as io_error:
        print(io_error)

    else:
        print("")

    finally:
        print(f"{nSheets} Sheets with {nCharacters} characters generated")
