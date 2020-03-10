'''Basic rotation cipher'''
def rotCipher():
    #opens message and asks for the rotation to use
    infile = open('message.txt', 'r')
    inMessage = infile.read()
    rotation = int(input('How many rotations should I make?\n'))
    outMessage = ""
    for character in inMessage:
        #rotates A-Z
        if ord(character) in range(65,91):
            if ord(character) + rotation > 90:
                outMessage += chr(ord(character) - (26 - rotation))
            else:
                outMessage += chr(ord(character) + rotation)
        #rotates a-z
        elif ord(character) in range(97,123):
            if ord(character) + rotation > 122:
                outMessage += chr(ord(character) - (26 - rotation))
            else:
                outMessage += chr(ord(character) + rotation)
        # leaves all other characters untouched
        else:
            outMessage += character
    #writes encoded message to a new file
    infile.close()
    outfile = open('encodedMessage.txt', 'w')
    outfile.write(outMessage)
    outfile.close
    
rotCipher()