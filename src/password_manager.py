master_pwd = input("What is the master password? ")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip() #rstrip will strip the carriage return
            user , passw = data.split("|")
            print("User:", user,"\nPassword:", passw)



def add():
    name = input("Account Name:  ")
    pwd = input("Password:  ")

    #with open == closes the file when we finished using it, 'a' mode means that you can add something in the existing file, or if the file dosent exist it will create a new file named 'password.txt'
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")






while True:
 mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
 if mode == 'q':
     break

 if mode == 'view':
    view()
 elif mode == 'add':
    add()
 else:
    print("Invalid mode.")
    continue