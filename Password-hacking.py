import hashlib  
print("# # # # # #  Password Hacking # # # # # #")  
          
# to check if the password is found or not in the text file.  
password_found = 0                                       
   
inputinput_hashed = input(" Please enter the hashed password: ")  
   
password_document = input(" \n Please enter the passwords file name including its path (root / home/): ")  
    
try:  
    # here, we will try to open the passwords text file.  
    password_file = open(password_document, 'r')               
except:  
    print("Error: ")  
    print(password_document, "is not found.\n Please enter the path of file correctly.")  
    quit()  
   
   
# now, for comparing the input_hashed with the hashes of the words present in the password text file for finding the password.  
   
for word in password_file:  
    # to encode the word into utf-8 format  
    encoding_word = word.encode('utf-8')   
               
    # to Hash the word into md5 hash  
    hashed_word = hashlib.md5(encoding_word.strip())    
    
    # to digest that the hash into the hexadecimal value      
    digesting = hashed_word.hexdigest()          
        
    if digesting == input_hashed:  
        # to compare the hashes  
        print ("Password found.\n The required password is: ", word)    
        password_found = 1  
        break  
   
# if the password is not found in the text file.  
if not password_found:  
    print(" The password is not found in the ", password_document, "file")    
    print('\n')  
print(" # # # # # # Thank you # # # # # # ")  




Input 1:

# # # # # #  Password Hacking # # # # # #  
 Please enter the hashed password:  1f23a6ea2da3425697d6446cf3402124  
   
Please enter the passwords file name including its path (root / home/):  passwords.txt  
Output:

Password found.
 The required password is:  manchester123

 # # # # # # Thank you # # # # # #
Input 2:

# # # # # #  Password Hacking # # # # # #  
 Please enter the hashed password:  b24aefc835df9ff09ef4dddc4f817737  
   
 Please enter the passwords file name including its path (root / home/):  passwords.txt  
Output:

Password found.
 The required password is:  heartbreaker07

 # # # # # # Thank you # # # # # #
