import math

import random

def decryptionStage1():
     print("Enter Your Public Key N:")
     publicKey_N = int(input())
     print("Enter Your Private key d:")
     privateKey_D = int(input())
     print("Please enter the message you want to Decrypt")
     m1 = str(input())
     m1 = m1.replace('[', '')
     m1 = m1.replace(']', '')
     m2 = []
     values = m1.split(",")
     for i in values:
        club = int(i)
        messageClub = decryptionStage2(club, privateKey_D, publicKey_N)
        m2.append(messageClub)
     print(m2)
     club = ''.join(m2)
     print(club)

def decryptionStage2(str, D, N):
    stat=''
    decryptedMessage = squareAndMultiply(str, D, N)
    hexString = hex(decryptedMessage)
    stat = stat+hexString.replace('0x','')
    bytesLayout = bytes.fromhex(stat)
    decryptedMessage = bytesLayout.decode("ASCII")
    return decryptedMessage



def validateSignature():
     print("Enter the details as per the data uploaded on moodle")
     print("Enter the partner's signed text : ")
     r1 = str(input()) # the encrypted message is stored in the value r1
     print("Enter the partner's original text : ")
     signature = str(input())
     print("Enter the Partner's Public key N")
     publicKey_N = int(input())
     print("Enter the Partner's Public key e")
     privateKey_D = int(input())
      
     r1 = r1.replace('[', '') #removing open square brackets 
     r1 = r1.replace(']', '') #removing close square brackets
     r2 = []
     values = r1.split(",")
     for i in values:
        s = int(i)
        r3 = decryptionStage2(s, privateKey_D, publicKey_N) #calling decryption function
        r2.append(r3)
     combine = ''.join(r2)
     if(signature == combine):
         print('Signature verification is: True')
     else:
         print('Signature verification is: False')
     print(combine)
    
def signature():
     
     print("Please enter the your Public key N") #taking user inputs
     publicKey_N = int(input())
     print("Please enter the your Private key D")
     publicKey_E = int(input())
     print("Please enter Your Signature to be encrypted")
     m1 = str(input())      #m1 is taking string input from user
     List_Temp = []
     temp =''
     m2=[]
     for i in range(0, len(m1), 3):  #using loop to divide message into 3 letters group
        if (len(m1) - i > 3): 
            miniString = m1[i:i+3]   #if length is greater than 3 break the string and append to listtemp
            List_Temp.append(miniString)
        else:
            miniString = m1[i :]
            List_Temp.append(miniString)
     print(List_Temp)
     for x in List_Temp:
        m12 = encryptionStage2(x, publicKey_N, publicKey_E)
        m2.append(m12)
     for i in m2:
        temp += str(i)+','
     temp = temp[0:-1]
     print('The encrption of my signature is as below : ')
     print('['+temp+']')
def encryptionStage1():
        
     print("Enter Your Partner's Public Key N:")    #taking user inputs
     publicKey_N = int(input())
     print("Enter Your Partner's Public Key e:")
     publicKey_E = int(input())
     print("Enter the message to be enrypted")
     m1 = str(input())
     m2 = []
     stat = ''
     List_Temp= []
    
     for i in range(0, len(m1), 3): #using loop to divide message into 3 letters group
        if (len(m1) - i > 3): 
            miniString = m1[i:i+3]   #if length is greater than 3 break the string and append to listtemp
            List_Temp.append(miniString)
        else:
            miniString = m1[i :]
            List_Temp.append(miniString)
     print(List_Temp)
     for x in List_Temp:
        m12 = encryptionStage2(x, publicKey_N, publicKey_E)
        m2.append(m12)
        
     for i in m2:
        stat = stat+str(i)+','
     stat = stat[0:-1]
     print('['+stat+']')

def encryptionStage2(str, N, e):
     stat = ''
     for i in str:
        ascii = ord(i)
        hexString = hex(ascii) #convert ascii to hex
        stat +=hexString.replace('0x','')     #stripping the 0x
     value = int(stat,16)
     encryptedMessage = squareAndMultiply(value, e, N)
     return encryptedMessage

def squareAndMultiply( str,  e,  N):
    Dict = {} 
    binaryString = bin(e).replace("0b", "") #stripping the 0b
    print(binaryString)
    reverseBinaryString=binaryString[::-1]
    result = 0
    finalResult = 1
    for i in range(len(binaryString)):
        if (i == 0):
            result = str
        else:
            result = result * result
            if (result >= N):
                quotient = result // N
                result -= quotient * N
        Dict[i] =  result
    for j in range(0, len(reverseBinaryString)):
        if (reverseBinaryString[j] == '1'):
            finalResult *= Dict[j]
            if (finalResult >= N):
                quotient = finalResult // N
                finalResult -= quotient * N

    if (finalResult >= N):
        quotient = finalResult // N
        finalResult -=quotient * N
    return finalResult

def switch():
    option = int(input("Select: \n 1.Encryption \n 2.Decryption \n 3.Signature \n 4.Validate Signature "))

    if option == 1:
        encryptionStage1()
 
    elif option == 2:
        decryptionStage1()
 
    elif option == 3:
        signature()
    
    elif option == 4:
        validateSignature()
 
    else:
        print("Incorrect option selected. Please select valid option!")


print('This is the program for Encryption, Decryption, Signing and validation of Signature!')
switch()







