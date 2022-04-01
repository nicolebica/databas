from atexit import register
from distutils.util import execute
from sqlite3 import connect
from tkinter import N
import psycopg2
import math
from datetime import date
user_email=""
def add_products():
    name_input = input("Vänligen skriv in ett produktnamn: ")
    quantity=input("Skriv in antal:")
    price=input("Skriv in pris")
    supplier=input("Skriv in supplier")
    conn = psycopg2.connect(
    database="grupp_17", user='al7834', password='d7s92q9v', host='pgserver.mau.se', port= '5432')
    cursor = conn.cursor()
    cursor.execute(f"insert into products(p_name, quantity, base_price, s_name) VALUES('{name_input}','{quantity}','{price}','{supplier}')")
    print("Connection established to: ")
    conn.commit()
    conn.close()

def add_supplier():
    sup=input("Supplier: ")
    add=input("Adress: ")
    phone=input("Telefonnummer: ")
    conn = psycopg2.connect(
    database="grupp_17", user='al7834', password='d7s92q9v', host='pgserver.mau.se', port= '5432')
    cursor = conn.cursor()
    cursor.execute(f"insert into suppliers(s_name, adress, phone_nr) VALUES('{sup}','{add}','{phone}')")
    conn.commit()
    conn.close()

#add_supplier()
#admin_menu()

#Visar upp produkter 
def show_products():
    conn = psycopg2.connect(
    database="grupp_17", user='al7834', password='d7s92q9v', host='pgserver.mau.se', port= '5432')
    cursor = conn.cursor()
    cursor.execute(f"select*from products")
    product = cursor.fetchall()
    for row in product:
        print("Id: ", row[0])
        print("Name: ", row[1])
        print("Antal: ",row[2])
        print("Pris: ", row[3])
        print("Leverantör: ", row[4])
    conn.commit()
    conn.close()


def login_user():
    try:
        global user_email
        user_email = input("Emailadress: ").lower()
        conn = psycopg2.connect(
        database="grupp_17", user='al7834', password='d7s92q9v', host='pgserver.mau.se', port= '5432')
        cursor = conn.cursor()
        cursor.execute(f"select email from users where email = '{user_email}'")
        checkEmail=cursor.fetchone()[0]

        if user_email == checkEmail:
            print("Välkommen!")
            #användarens_menyval()

    except:
        print("Felaktigt inlogg")

#lägger till användare
def register_user():
    try:
        name=input("Namn: ")
        efternamn=input("Efternamn: ")
        email=input("Email: ")
        conn = psycopg2.connect(
        database="grupp_17", user='al7834', password='d7s92q9v', host='pgserver.mau.se', port= '5432')
        cursor = conn.cursor()
        cursor.execute(f"insert into users(f_name,l_name, email) values('{name}','{efternamn}','{email}')")
        conn.commit()
        conn.close()
        print(f"Du är nu inlagd, välkommen {name}!")
    except:
        print("Det gick ej att lägga till dig")
#register_user()