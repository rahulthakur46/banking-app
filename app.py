import streamlit as st
from pathlib import Path
import json
import random
import string

class Bank:
    database = 'database.json'
    data = []

    if Path(database).exists():
        with open(database) as fs:
            data = json.loads(fs.read())

    @classmethod
    def update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(cls.data))

    @staticmethod
    def accountno():
        alpha = random.choices(string.ascii_letters,k=5)
        digits = random.choices(string.digits,k=4)
        id = alpha + digits
        random.shuffle(id)
        return "".join(id)

    @classmethod
    def create_account(cls,name,email,phone,pin):
        acc = cls.accountno()
        d = {
            "name":name,
            "email":email,
            "phone No.":phone,
            "pin":pin,
            "Account No.":acc,
            "balance":0
        }
        cls.data.append(d)
        cls.update()
        return acc

    @classmethod
    def deposit(cls,accNo,pin,amount):
        user=[i for i in cls.data if i['Account No.']==accNo and i['pin']==pin]
        if not user:
            return "User not found"
        user[0]['balance']+=amount
        cls.update()
        return "Deposited"

    @classmethod
    def withdraw(cls,accNo,pin,amount):
        user=[i for i in cls.data if i['Account No.']==accNo and i['pin']==pin]
        if not user:
            return "User not found"
        if user[0]['balance']<amount:
            return "Insufficient Balance"
        user[0]['balance']-=amount
        cls.update()
        return "Withdrawn"

    @classmethod
    def details(cls,accNo,pin):
        user=[i for i in cls.data if i['Account No.']==accNo and i['pin']==pin]
        if not user:
            return None
        return user[0]


st.title("🏦 Bank Management System")

menu=st.sidebar.selectbox("Menu",
["Create Account","Deposit","Withdraw","Check Details"])

if menu=="Create Account":
    name=st.text_input("Name")
    email=st.text_input("Email")
    phone=st.text_input("Phone")
    pin=st.text_input("PIN")

    if st.button("Create"):
        acc=Bank.create_account(name,email,int(phone),int(pin))
        st.success(f"Account Created! Account No: {acc}")

if menu=="Deposit":
    acc=st.text_input("Account No")
    pin=st.text_input("PIN")
    amt=st.number_input("Amount")

    if st.button("Deposit"):
        msg=Bank.deposit(acc,int(pin),amt)
        st.success(msg)

if menu=="Withdraw":
    acc=st.text_input("Account No")
    pin=st.text_input("PIN")
    amt=st.number_input("Amount")

    if st.button("Withdraw"):
        msg=Bank.withdraw(acc,int(pin),amt)
        st.success(msg)

if menu=="Check Details":
    acc=st.text_input("Account No")
    pin=st.text_input("PIN")

    if st.button("Check"):
        data=Bank.details(acc,int(pin))
        if data:
            st.write(data)
        else:
            st.error("User not found")