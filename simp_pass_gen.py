import random

def password_gen():
    
    num_passwords = int(input('Enter the number of passwords you want to generate '))
    passowrd_length = int(input('Enter the length of the password '))
    
    elements = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ!@#$%^&*()-+?123456789'
    
    
    for password in range(num_passwords):
        password = ''
        for e in range(passowrd_length):
            password += random.choice(elements)
        print(password)
        
        
password_gen()
        
    
    