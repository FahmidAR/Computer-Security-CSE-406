from distutils import text_file
import socket	
import S1705087_AES
import S1705087_RSA 	
import json
import os
import shutil

#Global Varribale Declare
debug=0
debugDeep=0
debugDeep1=0
default = 0

# main program
def main():

    print("\n===========================")
    print("Computer Security - CSE 406")
    print("Student ID = 1705087 - SERVER ")
    print("===========================\n")

    # 1705087 - AES
    
    print("\n===========================")
    print("Press 1 for Take input from txt/py/java/cpp file")
    print("Press 2 for Take raw input from console ^-^")
    print("Press 3 for Take input img/mp4/ohter from file")
    if default==0 :
        flagChoiceRK = int(input ("Enter your Choice = "))
    else :
        flagChoiceRK = 2
    print("===========================\n")

    key_length = 128 / 8 
    round = 10

    

    key_file_name =""
    file_Other = False
    png_flag = False

    if  flagChoiceRK == 1 :

        if(debug==1):
            print("Round Key Taken From File")
        
        key_file_name  = input("Enter File name which contain roundkey : ")
        text_file_name  = input("Enter File name which contain plain text : ")

        roundkey_file = open(key_file_name , "r")
        initial_roundkey = roundkey_file.read()

        if(debug==1):
            print("Round Key = "+initial_roundkey)

        roundkey_file.close()

        roundkey_file = open(text_file_name , "r")
        initial_text = roundkey_file.read()

        if(debug==1):
            print("Plain Text = "+initial_text)

        roundkey_file.close()

        file_Other = True
        file_info = (file_Other , text_file_name , png_flag)

    elif  flagChoiceRK == 3 :

        if(debug==1):
            print("Round Key Taken From File")
        
        key_file_name  = input("Enter File name which contain roundkey : ")
        text_file_name  = input("Enter File name which contain plain text : ")

        roundkey_file = open(key_file_name , "r")
        initial_roundkey = roundkey_file.read()

        if(debug==1):
            print("Round Key = "+initial_roundkey)

        roundkey_file.close()

        roundkey_file = open(text_file_name , "rb")
        initial_text = roundkey_file.read().decode('utf-8', 'ignore')

        if(debug==0):
            print("Plain Text = "+initial_text)

        roundkey_file.close()

        file_Other = True
        png_flag = True
        file_info = (file_Other , text_file_name , png_flag)


    else :

        if(debug==1):
            print ("Round Key Taken From Console")

        if default==0 :
            initial_roundkey = input("Enter initial roundkey : ")
            initial_text = input("Enter initial plain text : ")
            key_length = int(input("Enter key length (BIT) : "))
            key_length /=8
        elif default==1 :
            initial_roundkey = "Thats my Kung Fu"
            initial_text = "Two One Nine Two"
            key_length = 128 / 8
        else :
            initial_roundkey = "BUET CSE17 Batch"
            initial_text = "CanTheyDoTheirFest"
            key_length = 128 / 8

        if(debug==1):
            print("Round Key = "+initial_roundkey)
            print("Plain Text = "+initial_text)

        file_info = (file_Other , key_file_name , png_flag)

    if key_length == 128/8 :
        round = 10

    elif key_length == 192/8 :
        round = 12

    elif key_length == 256/8 :
        round = 14

    aes_info = (int(key_length) , round)

    if debugDeep == 1 :
        print(aes_info)

    cipher_text = S1705087_AES.cipher(initial_roundkey,initial_text,key_length,round,False)

    print("\nAES Encrypted Cipher Text = "+cipher_text)

    # 1705087 - RSA

    print("\n===========================")
    print("Press 1 for Auto Key Generation")
    print("Press 2 for Manual Key Input")
    if default== 0 :
        flagChoiceRK = int(input ("Enter your Choice = "))
    else :
        flagChoiceRK = 1
    print("===========================\n")

    if  flagChoiceRK == 1 :

        key_length = int(input("Enter key length in BIT (16,32,64,128,Any Power Of Two): "))

        p_q_length = key_length/2

        # Key generations Part
        public_key, private_key = S1705087_RSA.keyPairGeneration(p_q_length)

    elif flagChoiceRK == 2 :

        e = int(input ("Enter e = "))
        d = int(input ("Enter d = "))
        n = int(input ("Enter n = "))
        public_key = (e , n)
        private_key = (d , n)

    print("Public Key = ",public_key)
    print("Private Key = ",private_key)

    cipher_key = S1705087_RSA.encrypt(public_key, initial_roundkey)
    print("\nRSA Encrypted AES Key = ",cipher_key)

    s = socket.socket()		

    port = 12345			

    s.bind(('', port))		
    print ("Binding Done to  %s" %(port))

    s.listen(5)	
    print ("Waiting From Client ^-^ ")		

    while True:

        c, addr = s.accept()	
        print ('Connection Established from ', addr )

        c.send('Thank you for connecting :D'.encode())

        print (c.recv(1024).decode(),end='\n')

        c.send(cipher_text.encode())

        print (c.recv(1024).decode(),end='\n')

        data = json.dumps({"ck": cipher_key , "puk": public_key , "ai" : aes_info, "fi" : file_info })
        c.send(data.encode())

        print (c.recv(1024).decode(),end='\n')

        #Folder File Private Key

        folder_path =  'Don\'t Open This'

        if os.path.exists(folder_path):
            
            #os.rmdir(folder_path)
            shutil.rmtree(folder_path)

        os.mkdir(folder_path)

        data = json.dumps({"prk": private_key})

        with open(folder_path+'/key.txt', 'w') as f:
            f.write(data)

        c.send('Check Folder for Private Key :D'.encode())

        c.close()

        break

if __name__ == "__main__":
    main()