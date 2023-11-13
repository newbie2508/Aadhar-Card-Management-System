import csv
def create():
    with open("aadhar.csv","w",newline='') as f:
        cv=csv.writer(f)
        cv.writerow(['NAME','GENDER','AADHAR_NUMBER','ADDRESS','PHONE_NUMBER'])
        while True:
            name=input("enter the name")
            gender=input("enter the gender")
            aad_no=int(input("enter the aadhar number"))
            add=input("enter the address")
            pho_no=int(input("enter the phone number"))
            rec=[name,gender,aad_no,add,pho_no]
            cv.writerow(rec)
            c=input(" do you want to continue?")
            if c in 'nN':
                break
        

def search():
    with open("aadhar.csv","r",newline='') as f:
        cr=csv.reader(f)
        option2=input("enter your aadhar number")
        for c in cr:
            if c[2]==option2:
                print("your details are:")
                print("NAME:",c[0])
                print("GENDER:",c[1])
                print("AADHAR NUMBER:",c[2])
                print("ADDRESS:",c[3])
                print("PHONE NUMBER:",c[4])


def display():
    with open("aadhar.csv","r",newline='') as f:
        cr=csv.reader(f)
        for c in cr:
            print(c)
    
def update():
    with open("aadhar.csv","r",newline='') as f:
        cr=csv.reader(f)
        option=input("enter the aadhar number to be searched:")
        lists=[]
        for c in cr:
            if c[2]==option:
                while True:
                    option2=input("enter the information to be updated")
                    if option2.upper()=='NAME':
                        change=input("enter the name to be updated")
                        c.pop(0)
                        c.insert(0,change)
                        print("updated information",c)
                    elif option2.upper()=='GENDER':
                        change=input("enter the gender to be updated")
                        c[1]=change
                        print("updated information",c)
                    elif option2.upper()=='AADHAR NUMBER':
                        change=input("enter the aadhar number to be updated")
                        c[2]=change
                        print("updated information",c)
                    elif option2.upper()=='ADDRESS':
                        change=input("enter the address to be updated")
                        c[3]=change
                        print("updated information",c)
                    elif option2.upper()=='PHONE NUMBER':
                        change=input("enter the phone number to be updated")
                        c[4]=change
                        print("updated information",c)
                    else:
                        break
            lists.append(c)
        with open("aadhar.csv","w",newline='') as g:
            cw=csv.writer(g)
            for i in lists:
                cw.writerow(i)
            
                    
def delete():
    lists=[]
    with open("aadhar.csv","r") as f:
        cr=csv.reader(f)
        option=input("enter the aadhar to be deleted:")
        for c in cr:
            lists.append(c)
            if option==c[2]:
                lists.remove(c)
        with open("aadhar.csv","w",newline='') as g:
            cw=csv.writer(g)
            for i in lists:
                cw.writerow(i)

def add():
    lists=[]
    with open("aadhar.csv","r",newline='') as f:
        cr=csv.reader(f)
        for c in cr:
            if len(c[0])==0:
                print("your name is missing")
                c[0]=input("enter your name")
            elif len(c[1])==0:
                print("your gender is missing")
                c[1]=input("enter your gender")
            elif len(c[2])==0:
                print("your aadhar card number is missing")
                c[2]=int(input("enter your aadhar card number"))
            elif len(c[3])==0:
                print("your address is missing")
                c[3]=input("enter your address")
            elif len(c[4])==0:
                print("your phone number is missing")
                c[4]=int(input("enter your gender"))
            else:
                print("everything is complete")
            lists.append(c)
        with open("aadhar.csv","w",newline='') as g:
            cv=csv.writer(g)
            for i in lists:
                cv.writerow(i)

print("WELCOME TO THE AADHAR PORTAL","\n")
user=input(" Are you the admin?,(y/n)")
if user in "yY":
    login_id=input("enter the login id")
    password=input("enter your password")
    if login_id=='ADMIN' and password=='21aadhar':
        print("----you have successfully logged in----","\n")
        print("****WELCOME ADMIN****","\n")
        print("1. UPDATE INFORMATION")
        print("2. DISPLAY ALL INFORMATION")
        print("3. DELETE INFORMATION")
        print("0. EXIT")
        while True:
            option=int(input("enter the option"))
            if option==1:
                update()
            elif option==2:
                display()
            elif option==3:
                delete()
            elif option==0:
                print("THANK YOU")
                break
            else:
                print("enter a valid option","\n")
    else:
        print("enter correct login id and password")

else:
    option=input("enter do you already have an account")
    if option in 'yY':
        login_id=input("enter the login id")
        password=input("enter your password")
        if login_id=='USER' and password=='21aadhar':
            print("----you have successfully logged in----")
            print("****WELCOME USER****")
            print("1.DISPLAY YOUR INFORMATION")
            print("2. ADD A PARTICULAR INFORMATION")
            print("0. EXIT")
            while True:
                option=int(input("enter the option"))
                if option==1:
                    search()
                    print(" ")
                elif option==2:
                    add()
                    print(" ")
                elif option==0:
                    print("THANK YOU")
                    break
                else:
                    print("enter a valid option","\n")
    else:
        print("CREATE A NEW ACCOUNT")
        login_id=input("create a new login id")
        password=input("create a new password")
        create()
        print("THANK YOU")



import mysql.connector

# Create a connection to the MySQL database
conn = mysql.connector.connect(
    host="your_host",
    user="your_user",
    password="your_password",
    database="aadhar_db"
)
cursor = conn.cursor()

# Create a table to store Aadhar information
cursor.execute('''
    CREATE TABLE IF NOT EXISTS aadhar (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        gender VARCHAR(10),
        aadhar_number BIGINT,
        address TEXT,
        phone_number BIGINT
    )
''')

def create():
    while True:
        name = input("Enter the name: ")
        gender = input("Enter the gender: ")
        aadhar_no = int(input("Enter the Aadhar number: "))
        address = input("Enter the address: ")
        phone_no = int(input("Enter the phone number: "))

        # Insert the data into the database
        cursor.execute("INSERT INTO aadhar (name, gender, aadhar_number, address, phone_number) VALUES (%s, %s, %s, %s, %s)",
                       (name, gender, aadhar_no, address, phone_no))
        conn.commit()

        c = input("Do you want to continue? (y/n): ")
        if c in 'nN':
            break

def search():
    option2 = input("Enter your Aadhar number: ")
    cursor.execute("SELECT * FROM aadhar WHERE aadhar_number = %s", (option2,))
    result = cursor.fetchone()
    if result:
        print("Your details are:")
        print("NAME:", result[1])
        print("GENDER:", result[2])
        print("AADHAR NUMBER:", result[3])
        print("ADDRESS:", result[4])
        print("PHONE NUMBER:", result[5])
    else:
        print("Aadhar number not found.")

def display():
    cursor.execute("SELECT * FROM aadhar")
    for row in cursor.fetchall():
        print(row)

def update():
    option = input("Enter the Aadhar number to be searched: ")
    cursor.execute("SELECT * FROM aadhar WHERE aadhar_number = %s", (option,))
    result = cursor.fetchone()
    if result:
        while True:
            option2 = input("Enter the information to be updated (NAME/GENDER/AADHAR NUMBER/ADDRESS/PHONE NUMBER): ")
            if option2.upper() == 'NAME':
                change = input("Enter the name to be updated: ")
                cursor.execute("UPDATE aadhar SET name = %s WHERE aadhar_number = %s", (change, option))
                conn.commit()
            elif option2.upper() == 'GENDER':
                change = input("Enter the gender to be updated: ")
                cursor.execute("UPDATE aadhar SET gender = %s WHERE aadhar_number = %s", (change, option))
                conn.commit()
            elif option2.upper() == 'AADHAR NUMBER':
                change = int(input("Enter the Aadhar number to be updated: "))
                cursor.execute("UPDATE aadhar SET aadhar_number = %s WHERE aadhar_number = %s", (change, option))
                conn.commit()
            elif option2.upper() == 'ADDRESS':
                change = input("Enter the address to be updated: ")
                cursor.execute("UPDATE aadhar SET address = %s WHERE aadhar_number = %s", (change, option))
                conn.commit()
            elif option2.upper() == 'PHONE NUMBER':
                change = int(input("Enter the phone number to be updated: "))
                cursor.execute("UPDATE aadhar SET phone_number = %s WHERE aadhar_number = %s", (change, option))
                conn.commit()
            else:
                break
    else:
        print("Aadhar number not found.")

def delete():
    option = input("Enter the Aadhar number to be deleted: ")
    cursor.execute("DELETE FROM aadhar WHERE aadhar_number = %s", (option,))
    conn.commit()
    if cursor.rowcount > 0:
        print("Aadhar number deleted.")
    else:
        print("Aadhar number not found.")

def add():
    while True:
        option = input("Enter your Aadhar number: ")
        cursor.execute("SELECT * FROM aadhar WHERE aadhar_number = %s", (option,))
        result = cursor.fetchone()
        if result:
            print("Aadhar number already exists. Your information:")
            print("NAME:", result[1])
            print("GENDER:", result[2])
            print("AADHAR NUMBER:", result[3])
            print("ADDRESS:", result[4])
            print("PHONE NUMBER:", result[5])
        else:
            name = input("Enter your name: ")
            gender = input("Enter your gender: ")
            aadhar_no = int(input("Enter your Aadhar number: "))
            address = input("Enter your address: ")
            phone_no = int(input("Enter your phone number: "))

            cursor.execute("INSERT INTO aadhar (name, gender, aadhar_number, address, phone_number) VALUES (%s, %s, %s, %s, %s)",
                           (name, gender, aadhar_no, address, phone_no))
            conn.commit()
            print("Information added successfully.")

        c = input("Do you want to continue? (y/n): ")
        if c in 'nN':
            break

print("WELCOME TO THE AADHAR PORTAL","\n")
user = input("Are you the admin? (y/n): ")
if user in "yY":
    login_id = input("Enter the login id: ")
    password = input("Enter your password: ")
    if login_id == 'ADMIN' and password == '21aadhar':
        print("----you have successfully logged in----","\n")
        print("****WELCOME ADMIN****","\n")
        print("1. UPDATE INFORMATION")
        print("2. DISPLAY ALL INFORMATION")
        print("3. DELETE INFORMATION")
        print("0. EXIT")
        while True:
            option = int(input("Enter the option: "))
            if option == 1:
                update()
            elif option == 2:
                display()
            elif option == 3:
                delete()
            elif option == 0:
                print("THANK YOU")
                break
            else:
                print("Enter a valid option","\n")
    else:
        print("Enter the correct login id and password")

else:
    option = input("Do you already have an account? (y/n): ")
    if option in 'yY':
        login_id = input("Enter the login id: ")
        password = input("Enter your password: ")
        if login_id == 'USER' and password == '21aadhar':
            print("----you have successfully logged in----")
            print("****WELCOME USER****")
            print("1. DISPLAY YOUR INFORMATION")
            print("2. ADD A PARTICULAR INFORMATION")
            print("0. EXIT")
            while True:
                option = int(input("Enter the option: "))
                if option == 1:
                    search()
                    print(" ")
                elif option == 2:
                    add()
                    print(" ")
                elif option == 0:
                    print("THANK YOU")
                    break
                else:
                    print("Enter a valid option","\n")
        else:
            print("Invalid login id or password.")
    else:
        print("CREATE A NEW ACCOUNT")
        login_id = input("Create a new login id: ")
        password = input("Create a new password: ")
        create()
        print("THANK YOU")

# Close the database connection when done
conn.close()
# Make sure to replace "your_host", "your_user", and "your_password" with your MySQL server's host, username, and password. 
# Additionally, create a MySQL database named "aadhar_db" before running the script.

            
            
                    
                    
            
            
    





            
            
        
    
                
            
            
        
