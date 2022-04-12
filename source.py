'''

This is a coding assessment for CAPSTONE.
The program will take user capitalized input for the plaintext
and an integer between 1-5 for a shift key.

'''







def SKNinja():

    while True:
    #If text is not uppercase, try again
	
        try: 
            plaintext = str(input('Please enter your plaintext message in all uppercase letters: \n'))
            if plaintext.islower() or plaintext.isdigit():
                raise ValueError
            break
        except ValueError:
            print('Try again, and please use all uppercase letter in your plaintext. \n')
        
    while True:
#if key is out of range, try again
        try :
            shift = int(input('Enter Key to shift by between 1-5: \n'))
            if shift < 1 or shift > 5:
                raise ValueError
            break
        except ValueError:
            print('Key out of Range, please enter key between 1-5: \n')
        
#vowel table
    
    vowels = ['A', 'E', 'I', 'O', 'U']
    constanants = ['B', 'C', 'D', 'F', 'G', 'H', 'J','K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
#encryption message starts off blank
    encryption = ""
    for c in plaintext:
    # checks if text is a vowel, if so shift to right
        if c in vowels:
        # find the position in 0-25
            c_unicode = ord(c)
            c_index = ord(c) - ord("A")
        # perform the shift
            new_index = (c_index + shift) % 26
        # convert to new character
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)
        # append to encrypted string
            encryption = encryption + new_character
        else:
            if c in constanants:
        # check if not a vowel if so shift to the left
        # find the position in 0-25
                c_unicode = ord(c)
                c_index = ord(c) - ord("A")
        # perform the shift
                new_index = (c_index - shift) % 26
        # convert to new character
                new_unicode = new_index + ord("A")
                new_character = chr(new_unicode)
        # append to encrypted string
                encryption = encryption + new_character
            else:
                encryption = encryption + c
    print('\n')
    print("Your encrypted text is:\n",encryption)
    print('\n')

print('Welcome to the SKNinja CapCipher Encryption Algorithm, the coolest thing since the trampoline!!\n \n')
SKNinja()
input('Hit ENTER to exit. ')
