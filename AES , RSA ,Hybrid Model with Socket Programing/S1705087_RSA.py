from Crypto.Util import number
import math 
import time

debug=0
debugDeep=0
debugDeep1=0
default = 0


def keyPairGeneration (key_length) :

    key_length = int (key_length)

    if(debug==1):
            print("Key = ",key_length)

    p = number.getPrime(key_length)

    if(debug==1):
            print("P = ",p)

    q = number.getPrime(key_length)

    while(p == q) :
        q = number.getPrime(key_length)

    if(debug==1):
            print("Q = ",q)

    n = p*q

    phi = (p-1) * (q-1)

    for e in range(2, phi ):
        if math.gcd(e, phi) == 1 :
            break
    
    if(debug==1):
            print("E = ",e)
    """

    for d in range(2, phi):
        if (e * d) % phi == 1:
            break   
    """
    #Heu Ristic 
    d = pow(e, -1, phi)

    if(debug==1):
            print("D = ",d)

    return ((e, n), (d, n))

def encrypt(public_key, plain_text) :

    e , n = public_key

    cipher_text = []

    for c in plain_text :
        cipher_text.append( pow(ord(c), e, n) )

    return cipher_text
    

def decrypt(private_key, cipher_text):

    d , n = private_key

    plain_text = []

    for c in cipher_text :
        #heuristic 2
        plain_text.append( chr(pow(c, d, n) ))

    plain_text = ''.join(plain_text)

    return plain_text

# main program
def main():

    print("\n===========================")
    print("Computer Security - CSE 406")
    print("Student ID = 1705087 - RSA ")
    print("===========================\n")

    if(debug==1):
        print("-Python DEBUG mode ON\n")

    print("\n===========================")
    print("Press 1 for Statistic Genaration")
    print("Press 2 for Manual Test")
    if default== 0 :
        flagChoiceRK = int(input ("Enter your Choice = "))
    else :
        flagChoiceRK = 2
    print("===========================\n")

    if flagChoiceRK ==1 :

        initial_text = input("Enter plain text : ")

        print("K Value   ,   Key Schedulling   ,    Encryption    ,    De-cryption ")
        
        for y in range(4, 12 ):

            print("K = ",pow(2,y),end=' ')

            start = time.time()
            public_key, private_key = keyPairGeneration(pow(2,y))
            end = time.time()

            print(" ",end - start,end=' ')

            start = time.time()
            cipher_text = encrypt(public_key, initial_text)
            end = time.time()

            print(" ",end - start,end=' ')

            start = time.time()
            decrypt(private_key, cipher_text)
            end = time.time()

            print(" ",end - start)

        return

    print("\n===========================")
    print("Press 1 for Auto Key Generation")
    print("Press 2 for Manual Key Input")
    if default== 0 :
        flagChoiceRK = int(input ("Enter your Choice = "))
    else :
        flagChoiceRK = 1
    print("===========================\n")

    if  flagChoiceRK == 1 :

        key_length = int(input("Enter key length in BIT (16,32,64,128,Any Power Of Two ): "))

        p_q_length = key_length/2

        # Key generations Part
        public_key, private_key = keyPairGeneration(p_q_length)

    elif flagChoiceRK == 2 :

        e = int(input ("Enter e = "))
        d = int(input ("Enter d = "))
        n = int(input ("Enter n = "))
        public_key = (e , n)
        private_key = (d , n)

    print("Public Key = ",public_key)
    print("Private Key = ",private_key)
    
    print("\n===========================")
    print("Press 1 for Take Plain Text from file")
    print("Press 2 for Take Plain Text from console")
    if default==0 :
        flagChoiceRK = int(input ("Enter your Choice = "))
    else :
        flagChoiceRK = 2
    print("===========================\n")

    if  flagChoiceRK == 1 :

        if(debug==1):
            print("Round Key Taken From File")
        
        text_file_name  = input("Enter File name which contain plain text : ")

        file = open(text_file_name , "r")
        initial_text = file.read()

        if(debug==1):
            print("Plain Text = "+initial_text)

        file.close()

    else :

        if(debug==1):
                print ("Plain text Taken From Console")

        if default==0 :
            initial_text = input("Enter initial plain text : ")
        elif default==1 :
            initial_text = "Two One Nine Two"

    cipher_text = encrypt(public_key, initial_text)
    print("\nCipher Text = ",cipher_text)

    print("\n===========================")
    print("Press 1 for Take round key from console")
    print("Press 2 for Take round key from Cipher Function")
    if default==0 :
        flagChoiceRK = int(input ("Enter your Choice = "))
    else :
        flagChoiceRK = 2
    print("===========================\n")

    if flagChoiceRK == 1 :
        private_key = input("Enter Private : ")
        cipher_text = input("Enter the cipher_text : ")   

    print("\nDe-Cipher Text = "+decrypt(private_key, cipher_text))

     

if __name__ == "__main__":
    main()