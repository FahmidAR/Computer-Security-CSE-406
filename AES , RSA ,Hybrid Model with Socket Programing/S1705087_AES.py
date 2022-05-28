from BitVector import *
import time

Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

Mixer = [
    [BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03")],
    [BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02")]
]

InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E")]
]

#Global Varribale Declare
debug=0
debugDeep=0
debugDeep1=0
default = 0

all_keys = []

all_texts = []

def subByteAll(word) :

    temp_bitvec = BitVector(size=0)

    for i in range(0, word.length(), 8):
        byte = word[i:i+8].get_bitvector_in_hex()
        b = BitVector(hexstring=byte)
        int_val = b.intValue()
        s = Sbox[int_val]
        s = BitVector(intVal=s, size=8)
        temp_bitvec+=s
        #print(s.get_bitvector_in_hex())

    return temp_bitvec

def subInvByteAll(word) :

    temp_bitvec = BitVector(size=0)

    for i in range(0, word.length(), 8):
        byte = word[i:i+8].get_bitvector_in_hex()
        b = BitVector(hexstring=byte)
        int_val = b.intValue()
        s = InvSbox[int_val]
        s = BitVector(intVal=s, size=8)
        temp_bitvec+=s
        #print(s.get_bitvector_in_hex())

    return temp_bitvec

def multiplyBitVector(bv1,bv2) :

    AES_modulus = BitVector(bitstring='100011011')

    #bv1 = BitVector(hexstring="02")
    #bv2 = BitVector(hexstring="63")
    bv3 = bv1.gf_multiply_modular(bv2, AES_modulus, 8)
    #print(bv3)

    return bv3


def keyTo16(initial_key,key_length) :

        if len(initial_key) > key_length:
            initial_key = initial_key[0: key_length]
        elif len(initial_key) < key_length:
            #initial_key = initial_key.zfill(16)
            #initial_key.pad_from_right(key_length - len(initial_key))
            initial_key += (int(key_length) - len(initial_key))*'0' 

        if(debug==1):
            print("Key to 16 Byte = "+initial_key)
        
        return initial_key

def plainTo16(initial_text,text_length) :

        text_length = 16

        if (len(initial_text) % text_length) != 0: 
            initial_text += (text_length - len(initial_text)%text_length)*'0'     

        if(debug==1):
            print("Text to 16 Byte = "+initial_text)
        
        return initial_text

def fileTo16(initial_text) :

        text_length = 16

        if (len(initial_text) % text_length) != 0: 
            initial_text += (text_length - len(initial_text)%text_length)*'0'     

        if(debug==1):
            print("Text to 16 Byte = "+initial_text)
        
        return initial_text

def shiftWord(old_word,n) :

    new_word = old_word

    return new_word<<n

def gFunction(old_word,round_constant) :

    new_word = BitVector(hexstring=old_word.get_bitvector_in_hex())

    #bit vector shift left
    #old_word.shift_left(8)
    #old_word=old_word<<8
    new_word = shiftWord(new_word,8)

    if debugDeep :
        print("Shift Byte = ",new_word.get_bitvector_in_hex())

    #sub byte 
    new_word = subByteAll(new_word)

    if debugDeep :
        print("Sub Byte = ",new_word.get_bitvector_in_hex())

    #for making rc 00 00 00
    round_constant += BitVector(hexstring="000000")

    if debugDeep :
        print("Round Constant = ",round_constant.get_bitvector_in_hex())
    
    #adding round constant
    new_word ^= round_constant

    return new_word


def keyOperations(initial_key,key_length,round) :

    all_keys.clear()

    all_keys.append(BitVector(textstring=keyTo16(initial_key,key_length)))

    if(debug==1):
        print("Round initial Hex key = ")
        print(all_keys[0].get_bitvector_in_hex())

    #Key Expantion

    AES_modulus = BitVector(bitstring='100011011')

    rc1 = BitVector(hexstring="01")
    rc2 = BitVector(hexstring="02")

    w=[]
    ks = 0

    w.append(all_keys[0][0:32])
    w.append(all_keys[0][32:64])
    w.append(all_keys[0][64:96])
    w.append(all_keys[0][96:128])

    ks = 4

    if(round>10) :

        w.append(all_keys[0][128:160])
        w.append(all_keys[0][160:192])

        ks = 6

    if(round>12) :

        w.append(all_keys[0][192:224])
        w.append(all_keys[0][224:256])

        ks = 8

    all_keys[0] = all_keys[0][0:128]

    if(debug==1):
        print("Round initial Hex key = ")
        print(all_keys[0].get_bitvector_in_hex())

    rc = []

    for x in range(round+1):

        rc.append (rc1)
        rc1 = rc2.gf_multiply_modular(rc1, AES_modulus, 8)

        if(debugDeep==1):
            print("G funtion Value of Round ",x+1," = ",rc[x].get_bitvector_in_hex())

    n = int(key_length*8//32)

    if(debugDeep==1):

        print("n = ",n)

        print("w i  0 = ",w[0].get_bitvector_in_hex())
        print("w i  1 = ",w[1].get_bitvector_in_hex())
        print("w i  2 = ",w[2].get_bitvector_in_hex())
        print("w i  3 = ",w[3].get_bitvector_in_hex())



    for i in range(ks,(round+1)*4) :

        #w.append(BitVector(size=0))

        temp = BitVector(size=0)

        if i%n == 0 :
            temp = w[int(i-n)]^gFunction(w[int(i-1)],rc[int(i//n-1)])
            w.append(temp)
            if(debugDeep==1):
                print("w i = ",i,w[i].get_bitvector_in_hex())

        elif i%n == 4 and n>6:
            temp = w[int(i-n)]^subByteAll(w[int(i-1)])
            w.append(temp)
            if(debugDeep==1):
                print("w i  shift = ",i,w[i].get_bitvector_in_hex())

        else :
            if(debugDeep==1):
                print("w[i-n] , w[i-i] = ",w[int(i-n)].get_bitvector_in_hex()," ",w[int(i-1)].get_bitvector_in_hex())
            temp = w[int(i-n)]^w[int(i-1)]
            w.append(temp)
            if(debugDeep==1):
                print("w i  else = ",i,w[i].get_bitvector_in_hex())
                #print("i-1 , i-n = ",int(i-1)," ",int(i-n))


    for i in range(1,(round+1)) :

        temp_key = w[4*i]+w[4*i+1]+w[4*i+2]+w[4*i+3]

        all_keys.append(temp_key)

        if(debug==1):
            print("Round ",i," Hex key = ")
            print(all_keys[i].get_bitvector_in_hex()) 

    '''

    word_len = 32
    total_len = 128

    for y in range(0, total_len, word_len):

            if y/word_len == 0 :
                w[y//word_len]=gFunction(w[total_len//word_len-1],rc)^all_keys[x][y:y+word_len]
                #w[y//word_len]=gFunction(w[total_len//word_len-1],rc)
                temp_key = w[y//word_len]
                #print("Temp ",temp_key)

            else :
                w[y//word_len]=w[y//word_len-1]^all_keys[x][y:y+word_len]
                temp_key += w[y//word_len]
                #print("Temp ",temp_key)

            if y/word_len == total_len/word_len-1 :
                
                all_keys.append(temp_key)

    if(debug==1):
        print("Round ",x+1," Hex key = ")
        print(all_keys[x+1].get_bitvector_in_hex()) '''

def TextTo2DMatrix(text) :

    matrix_1D = []

    for i in range(0, 16*8, 8) :
        matrix_1D.append(text[i:i+8])

    matrix_2D = []

    for row in range(4):
        inner_list = []
        for col in range(4):
            inner_list.append(matrix_1D[4*col+row])
        matrix_2D.append(inner_list)

    return matrix_2D

def print2DMatrix(state_matrix) :

    print()

    for row in range(4):
        
        for col in range(4):

            print(state_matrix[row][col].get_bitvector_in_hex(), end = ' ')

        print()
        

def addRoundKey(state_matrix,key_matrix) :

    matrix_2D = []

    for row in range(4):
        inner_list = []
        for col in range(4):
            inner_list.append(None)
        matrix_2D.append(inner_list)

    for row in range(4):
        for col in range(4):
            matrix_2D[row][col] = state_matrix[row][col]^key_matrix[row][col]

    return matrix_2D

def subByteMatrix(state_matrix,mode) :

    #mode false for INVERSE

    matrix_2D = []

    for row in range(4):
        inner_list = []
        for col in range(4):
            inner_list.append(None)
        matrix_2D.append(inner_list)

    for row in range(4):
        for col in range(4):
            if mode :
                matrix_2D[row][col] = subByteAll(state_matrix[row][col])
            else :
                matrix_2D[row][col] = subInvByteAll(state_matrix[row][col])

    return matrix_2D

def shiftInvMatrix(state_matrix) :

    matrix_2D = []

    for row in range(4):
        inner_list = []
        for col in range(4):
            inner_list.append(None)
        matrix_2D.append(inner_list)

    for row in range(4):
        for col in range(4):
            matrix_2D[row][col] = state_matrix[row][col-row]

    return matrix_2D

def shiftMatrix(state_matrix) :

    matrix_2D = []

    for row in range(4):
        inner_list = []
        for col in range(4):
            inner_list.append(None)
        matrix_2D.append(inner_list)

    for row in range(4):
        for col in range(4):
            if col == 0 :
                shift_col = row
            else :
                shift_col = (col+row)%4
            matrix_2D[row][col] = state_matrix[row][shift_col]

    return matrix_2D

def mixMatrix(state_matrix,key_matrix) :

    #key matrix mean mixer/ inv mixer
    #multiplication serail mix before state

    matrix_2D = []

    for row in range(4):
        inner_list = []
        for col in range(4):
            inner_list.append(None)
        matrix_2D.append(inner_list)

    # iterate through rows of state_matrix
    for i in range(len(key_matrix)):
    # iterate through columns of key_matrix
        for j in range(len(state_matrix[0])):
            # iterate through rows of key_matrix
            for k in range(len(state_matrix)):
                if k == 0 :
                    matrix_2D[i][j] = multiplyBitVector(key_matrix[i][k],state_matrix[k][j])
                else :
                    matrix_2D[i][j] ^= multiplyBitVector(key_matrix[i][k],state_matrix[k][j])

    return matrix_2D

def stateMatrixToCipher(state_matrix) :

    cipher_text = BitVector(size=0)

    for col in range(4):
        for row in range(4):
            cipher_text  += state_matrix[row][col]

    return cipher_text 

def stateMetrixInvRound(text,key_length,text_length,round) :

    state_matrix = [[]]

    if(debug==1):
           print("State Matrix INV TEXT Before Round ",0," Text = ")
           print(text.get_bitvector_in_hex())  

    if debug :
        print("\n## INV Round Operations no 0 ")
    
    # Add Round Key

    state_matrix = TextTo2DMatrix(text)
    key_matrix = TextTo2DMatrix(all_keys[round])

    if debug :
        print2DMatrix(state_matrix)
        print2DMatrix(key_matrix)

    state_matrix = addRoundKey(state_matrix,key_matrix)

    if debug :
        print2DMatrix(state_matrix)

    for r in range(round):

        if debug :
            print("\n## INV Round Operations no ",r+1)

        # INV shift Matrix

        state_matrix = shiftInvMatrix(state_matrix)

        if debug :
            print2DMatrix(state_matrix)

        #Sub Byte Matrix

        
        state_matrix = subByteMatrix(state_matrix,False)

        if debug :
            print2DMatrix(state_matrix)
        
        # Add Round Key

        key_matrix = TextTo2DMatrix(all_keys[round-r-1])
        state_matrix = addRoundKey(state_matrix,key_matrix)

        if debug :
            print2DMatrix(state_matrix)

        # INV Mix Collumn

        if r != round -1 :

            state_matrix = mixMatrix(state_matrix,InvMixer)

            if debug :
                print2DMatrix(state_matrix)
    
    return stateMatrixToCipher(state_matrix)

        
      

def stateMetrixRound(text,key_length,text_length,round) :

    state_matrix = [[]]

    if(debug==1):
           print("State Matrix TEXT Before Round ",0," Text = ")
           print(text.get_bitvector_in_hex())

    if debug :
        print("\n## Round Operations no 0 ")

    # Add Round Key

    state_matrix = TextTo2DMatrix(text)
    key_matrix = TextTo2DMatrix(all_keys[0])

    if debug :
        print2DMatrix(state_matrix)
        print2DMatrix(key_matrix)


    state_matrix = addRoundKey(state_matrix,key_matrix)

    if debug :
        print2DMatrix(state_matrix)

    
    for r in range(round):

        if debug :
            print("\n## Round Operations no ",r+1)

        #Sub Byte Matrix

        
        state_matrix = subByteMatrix(state_matrix,True)

        if debug :
            print2DMatrix(state_matrix)
        
        # shift Matrix

        state_matrix = shiftMatrix(state_matrix)

        if debug :
            print2DMatrix(state_matrix)

        # Mix Collumn

        if r != round -1 :

            state_matrix = mixMatrix(state_matrix,Mixer)

            if debug :
                print2DMatrix(state_matrix)

        # Add Round Key

        key_matrix = TextTo2DMatrix(all_keys[r+1])
        state_matrix = addRoundKey(state_matrix,key_matrix)

        if debug :
            print2DMatrix(state_matrix)
        
    return stateMatrixToCipher(state_matrix)
    


def textOperations(initial_text,key_length,text_length,round) :

    all_texts.clear()

    initial_text = BitVector(textstring=plainTo16(initial_text,text_length))

    if(debug==1):
        print("Initial Hex Text = ")
        print(initial_text.get_bitvector_in_hex())

    final_cipher = BitVector(size=0)

    for i in range(0, initial_text.length(), text_length):

        all_texts.append(initial_text[i:i+text_length])
        final_cipher +=stateMetrixRound(all_texts[i//text_length],key_length,text_length,round)

        if(debug==1):
           print("Text ",i//text_length," Hex Value = ")
           print(all_texts[i//text_length].get_bitvector_in_hex())

    if(debug==1):
           print("Final Cipher Text Hex Value = ")
           print(final_cipher.get_bitvector_in_hex())

    return final_cipher
  
def cipherOperations(initial_cipher_text,key_length,text_length,round) :

    all_texts.clear()

    initial_cipher_text = BitVector(hexstring=initial_cipher_text)

    if(debug==1):
        print("Initial Hex Cipher Text = ")
        print(initial_cipher_text.get_bitvector_in_hex())

    final_cipher = BitVector(size=0)

    for i in range(0, initial_cipher_text.length(), text_length):

        all_texts.append(initial_cipher_text[i:i+text_length])
        final_cipher +=stateMetrixInvRound(all_texts[i//text_length],key_length,text_length,round)

        if(debug==1):
            print("Text ",i//text_length," Hex Value = ")
            print(all_texts[i//text_length].get_bitvector_in_hex())

    if(debug==1):
        print("Final Cipher Text Hex Value = ")
        print(final_cipher.get_bitvector_in_hex())

    return final_cipher


def cipher(initial_key,initial_text,key_length,round,Time) :

    #bit = byte*8   
    text_length = int(16*8)

    start = time.time()
    keyOperations(initial_key,key_length,round)
    end = time.time()

    if Time :
            print("Key Scheduling Time (ms) = " , end - start)

    start = time.time()
    final_cipher = textOperations(initial_text,key_length,text_length,round)
    end = time.time()

    if Time :
        print("Encryption Time (ms) = " , end - start)

    return final_cipher.get_bitvector_in_hex()

def decipher(initial_key,initial_cipher_text,key_length,round,Time) :

    #bit = byte*8   
    text_length = int(16*8)

    keyOperations(initial_key,key_length,round)

    start = time.time()
    final_text = cipherOperations(initial_cipher_text,key_length,text_length,round)

    hex_string= str(final_text.get_bitvector_in_hex())
    bytes_object = bytes.fromhex(hex_string)
    ascii_string = bytes_object.decode("ASCII")
    end = time.time()

    if Time :
        print("De-Encryption Time (ms) = " ,end - start)

    ascii_string = ascii_string.replace('0', "")

    return ascii_string


# main program
def main():

    print("\n===========================")
    print("Computer Security - CSE 406")
    print("Student ID = 1705087 - AES ")
    print("===========================\n")

    if(debug==1):
        print("-Python DEBUG mode ON\n")
    
    print("\n===========================")
    print("Press 1 for Take round key from file")
    print("Press 2 for Take round key from console")
    if default==0 :
        flagChoiceRK = int(input ("Enter your Choice = "))
    else :
        flagChoiceRK = 2
    print("===========================\n")

    key_length = 128 / 8 
    round = 10

    

    key_file_name =""

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
            key_length = 192 / 8
        else :
            initial_roundkey = "BUET CSE17 Batch"
            initial_text = "CanTheyDoTheirFest"
            key_length = 128 / 8

        if(debug==1):
            print("Round Key = "+initial_roundkey)
            print("Plain Text = "+initial_text)

    if key_length == 128/8 :
        round = 10

    elif key_length == 192/8 :
        round = 12

    elif key_length == 256/8 :
        round = 14

    cipher_text = cipher(initial_roundkey,initial_text,key_length,round,True)
    
    print("\nCipher Text = "+cipher_text)

    print("\n===========================")
    print("Press 1 for Take round key from console")
    print("Press 2 for Take round key from Cipher Function")
    if default==0 :
        flagChoiceRK = int(input ("Enter your Choice = "))
    else :
        flagChoiceRK = 2
    print("===========================\n")

    if flagChoiceRK == 1 :
        initial_roundkey = input("Enter initial roundkey : ")
        cipher_text = input("Enter the cipher_text : ")         

    print("\nDe-Cipher Text = "+decipher(initial_roundkey,cipher_text,key_length,round,True))



if __name__ == "__main__":
    main()