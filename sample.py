


data = {
        "name": "rahul",
        "age": 24,
        "email": "mr.rahul415173@gmail.com",
        "pin": 7894,
        "phone": "8770803882",
        "accountno": "72p61EDP",
        "balance": 5000
    },








account = input("Enter Acc: ")
pin =int(input("Enter pin: "))
user_data = [i for i in data if i['accountno']==account and i['pin']==pin]
print(user_data)

if user_data == False:
    print("No such user ")
else:
    balance = int(input('Amount :'))
    user_data[0]['balance'] += balance
    print(user_data)