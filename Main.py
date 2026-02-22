from pathlib import Path
import json
import random 
import string 
class Bank:
    database = 'database.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("sorry we are facing some issues")
    
    except Exception as err:
        print(f"An error occurred as {err} ")
    
    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(cls.data))
    
    @staticmethod
    def __accountno():
        alpha = random.choices(string.ascii_letters,k = 5)
        digits = random.choices(string.digits,k= 4)
        id = alpha + digits 
        random.shuffle(id)
        return "".join(id)


    def createaccount(self):
        d = {
            "name":input("please tell your name: "),
            "email": input("please tell your mail : "),
            "phone No.":int(input("Tell your phone Number:-")),
            "pin":int(input("please tell your pin (4 digit)")),
            "Account No.":Bank.__accountno(),
            'balance':0           
            }
        print(f"please note down your account number :{d['Account No.']}")
        if len(str(d['pin'])) != 4:
            print("please review your pin ")
        
        elif len(str(d["phone No."])) != 10:
            print("please review your phone number")
        else:
            Bank.data.append(d)
            Bank.__update()
    
    def deposite_money(self):
        accNo = input("Enter your account no.")
        pin = int(input("Enter your pin: "))
        user_data = [i for i in Bank.data if i['Account No.']==accNo and i["pin"]==pin]
        print(user)    
        if not user_data:
            print("user not found")
        else:
            amount = int(input("Enter amount to be deposited: "))
            if amount <= 0:
                print("Invalid amount")
            elif amount > 10000:
                print("Greater than 10000")
            else:
                user_data[0]['balance'] += amount
                Bank.__update()
                print("Amount credited")

    def withdraw_money(self):
        accNo = input("Enter your account no.")
        pin = int(input("Enter your pin: "))
        user_data = [i for i in Bank.data if i['Account No.']==accNo and i["pin"]==pin]  
        if not user_data:
            print("user not found")
        else:
            amount = int(input("Enter amount to be withdraw: "))
            if amount <= 0:
                print("Invalid amount")
            elif amount > 10000:
                print("Greater than 10000")
            else:
                if user_data[0]['balance'] < amount:
                    print("Insufficent Balance")
                else:
                    user_data[0]['balance'] -=amount
                    Bank.__update()
                    print("Amount Debited")
        
    def details(self):
        accNo = input("Enter your account no.")
        pin = int(input("Enter your pin: "))
        user_data = [i for i in Bank.data if i['Account No.']==accNo and i["pin"]==pin]  
        if not user_data:
            print("user not found")
        else:
            for i in user_data[0]:
                print(i,user_data[0][i])

    def delete(self):
        account = input("Enter account no.: ")
        pin = int(input('Enter your 4 digit Pin: '))
        user_data = [i for i in Bank.data if i['Account No.']==accNo and i["pin"]==pin]  
        if not user_data:
            print("user not found")
        else:
            print("Are you sure you want to delete your account (yes/no)")
            choice = input("yes/no: ")
            if choice == "yes":
                ind = Bank.data.index(user_data[0])
                Bank.data.pop(ind)
                Bank.__update()
                print("Account deleted successfully")

    def update(Self):
        accNo = input("Enter your account no.")
        pin = int(input("Enter your pin: "))
        user_data = [i for i in Bank.data if i['Account No.']==accNo and i["pin"]==pin]
        print(user)    
        if not user_data:
            print("user not found")

        else:
            print('Aap Account No. aur Balance Update/Change nahi kar sakte ho')

            print("Enter your details to update or just press emter to skip them")

        new_data = {
            "name":input("please tell your name: "),
            "email": input("please tell your mail : "),
            "phone No.":(input("Tell your phone Number:-")),
            "pin":(input("please tell your pin (4 digit)")),

        }

        if new_data['name'] == "":
            new_data['name'] == user_data[0] ['name']

        if new_data['email'] == "":
            new_data['email'] == user_data[0] ['email']

        if new_data['phone No.'] == "":
            new_data['phone No.'] == user_data[0] ['phone No.']
        else:
            new_data['phone No.'] = int(new_data['phone No.'])    

        if new_data['pin'] == "":
            new_data['pin'] == user_data[0] ['pin']

        else:
            new_data['pin.']= int(new_data['pin'])     

        new_data['Account no.'] = user_data[0]['Account No.']
        new_data['balance'] = user_data[0]['balance']


        user_data[0].update(new_data)
        Bank.__update()

        
        



user = Bank()
print("press 1 for creating an account ")
print("press 2 to deposit money")
print("press 3 to withdraw money")
print("press 4 for details ")
print("press 5 for updating the details ")
print("press 6 for deleting the account")

check = int(input("tell your choice : - "))

if check == 1:
    user.createaccount()

if check == 2:
    user.deposite_money()

if check == 3:
    user.withdraw_money()


if check == 4:
    user.details()

if check == 5:
    user.update()

if check ==6:
    user.delete()
        


















