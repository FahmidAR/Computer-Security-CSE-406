import socket	
import S1705087_AES
import S1705087_RSA 	
import json	

# main program
def main():

    print("\n===========================")
    print("Computer Security - CSE 406")
    print("Student ID = 1705087 - Client ")
    print("===========================\n")

    s = socket.socket()		

    port = 12345			

    s.connect(('127.0.0.1', port))

    print (s.recv(1024).decode(),end='\n')

    s.send('Client : Give me encrypted Message To Decode :D'.encode())

    cipher_text = s.recv(1024).decode()
    print ("The AES cipher Text = " ,cipher_text,end='\n')

    s.send('Client : Received the AES cipher Text . Give me RSA encrypted AES key for Decodeing :D'.encode())

    data = s.recv(1024)
    data = json.loads(data.decode())
    cipher_key= data.get("ck")
    public_key = data.get("puk")

    aes_info = data.get("ai")
    file_info = data.get("fi")

    print ("Received RSA Encrypted AES Key = " ,cipher_key ,end='\n')

    s.send('Client : Received RSA Encrypted AES Key . I am Searching fo RSA Private key :D'.encode())

    print (s.recv(1024).decode(),end='\n')

    file = open('Don\'t Open This/key.txt' , "r")
    file_data = file.read()
    file.close()

    data = json.loads(file_data)
    private_key = data.get("prk")

    key_length , round = aes_info

    print ("Taken RSA private Key from Folder = " , private_key ,end='\n')

    # Aes key with Rsa
    aes_key = S1705087_RSA.decrypt(private_key, cipher_key)
    # Plain Text with Aes
    plain_text = S1705087_AES.decipher(str(aes_key),cipher_text,key_length,round,False)

    print ("\nFinal Decrypted Sender Text *-* = " , plain_text ,end='\n')

    s.close()	

    file_other , file_name , png_flag= file_info
    file_name = "1705087_output_"+file_name

    if file_other :

        if png_flag :
            file = open(file_name, "w")
            file.write(plain_text)
            file.close()
        
        else :
            file = open(file_name, "wb")
            file.write(plain_text.encode('ascii', 'ignore'))
            file.close()
	
if __name__ == "__main__":
    main()