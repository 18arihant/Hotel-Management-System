import pymysql
def customer_details():
    createTable="""CREATE TABLE IF NOT EXISTS customer_details(CID VARCHAR(20),NAME VARCHAR(30),ADDRESS
           VARCHAR(30),AGE VARCHAR(30),NATIONALITY VARCHAR(30) ,PHONENO VARCHAR(30),EMAIL VARCHAR(30));"""
    cr.execute(createTable)
    cid=input("Enter Customer ID:")
    name=input("Enter Customer Name:")
    address=input("Enter Customer Address:")
    age=input("Enter Customer Age:")
    nationality=input("Enter Customer Country:")
    phoneno=input("Enter Customer Contact Number:")
    email=input("Enter Customer Email:")
    query="INSERT INTO customer_details(cid,name,address,age,nationality,phoneno,email) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(
            cid,name,address,age,nationality,phoneno,email)
    cr.execute(query)        
    db.commit()
    print("New Customer Entered In The System Successfully !!!")
    
def booking():
    createTable="CREATE TABLE IF NOT EXISTS BOOKING(CID VARCHAR(20),CHECK_IN DATE,CHECK_OUT DATE);"
    cr.execute(createTable)
    cid=input("Enter Customer ID:")
    checkin=input("Enter Customer CheckIN Date in YYYY-MM-DD format:")
    checkout=input("Enter Customer CheckOUT Date in YYYY-MM-DD format:")
    query="""INSERT INTO booking(cid,check_in,check_out) VALUES('{}','{}','{}')""".format(cid
            ,checkin,checkout)
    cr.execute(query)
    db.commit()
    print("CHECK-IN AND CHECK-OUT ENTRY MADED SUCCESSFULLY !!!")
    
def roomrent():
    createTable="""CREATE TABLE IF NOT EXISTS ROOM_RENT(CID VARCHAR(20),ROOM_CHOICE INT,
                 NO_OF_DAYS INT,ROOM_NO INT ,ROOM_RENT INT);"""
    cr.execute(createTable)
    cid=input("Enter Customer ID:")
    print("-----We have The Following Room Categories-----")
    print("1.Superior room: Rs.4000/-")
    print("2.Premium room: Rs.6000/-")
    print("3.Executive suite: Rs.8000/-")
    print("4.Duplex suite nature view: Rs.10000/-")
    room_choice =int(input("Enter Your Option:"))
    room_no=int(input("Enter Customer Room No:"))
    no_of_days=int(input("Enter Number Of Days:"))
    if room_choice==1:
        room_rent=no_of_days*4000
        print("Superior room Rent:",room_rent)
    elif room_choice==2:
        room_rent=no_of_days*6000
        print("Premium Room Rent:",room_rent)
    elif room_choice==3:
        room_rent=no_of_days*8000
        print("Executive suite Rent:",room_rent)
    elif room_choice==4:
        room_rent=no_of_days*2500
        print("Duplex suite nature view Rent:",room_rent)
    else:
        print("Wrong choice entered")
    query="""INSERT INTO room_rent(cid,room_choice,room_no,no_of_days,room_rent)
             VALUES('{}','{}','{}','{}','{}')""".format(cid,room_choice,room_no,no_of_days,room_rent)
    cr.execute(query)
    db.commit()
    print("Thank You , Your Room Has Been Booked For : ",no_of_days , "Days" )
    print("Your Total Room Rent is : Rs. ",room_rent)

def restaurant():
    createTable ="""CREATE TABLE IF NOT EXISTS RESTAURANT(CID VARCHAR(20),
                MEAL_CHOICE VARCHAR(30),QUANTITY VARCHAR(30),RESTAURANT_BILL VARCHAR(30));"""
    cr.execute(createTable) 
    cid=input("Enter Customer ID:")
    print("1.Breakfast per person (Buffet): Rs.450/-")
    print("2.Lunch/Dinner per person (Buffet): Rs.700/-")
    meal_choice=int(input("Enter the meal choice:"))
    quantity=int(input("Enter the number of persons:"))
    if meal_choice==1:
        restaurant_bill=quantity*450
    elif meal_choice==2:
        restaurant_bill=quantity*700
    else:
        print("Wrong choice entered")
    query="""INSERT INTO restaurant(cid,meal_choice,quantity,restaurant_bill)
             VALUES('{}','{}','{}','{}')""".format(cid,meal_choice,quantity,restaurant_bill)    
    cr.execute(query)
    db.commit()
    print("Your Total Bill Amount Is : Rs. ",restaurant_bill) 
    
def roomservices():
    createTable ="""CREATE TABLE IF NOT EXISTS ROOM_SERVICES(CID VARCHAR(20),
                CHOICE VARCHAR(30),QUANTITY_OF_CLOTHES VARCHAR(30),SERVICE_BILL VARCHAR(30));"""
    cr.execute(createTable)
    cid=input("Enter Customer ID:")
    print("1.Room cleaning sevice: Rs.200/-")
    print("2.Laundary sevice (per cloth): Rs.50/-")
    print("3.Ironing sevice (per cloth): Rs.50/-")
    service_choice=int(input("Enter the choice:"))
    quantity_of_clothes=int(input("Enter number of clothes:"))
    if choice==1:
        service_bill=200
    elif choice==2 or choice==3:
        service_bill=quantity_of_clothes*50
    else:
        print("Wrong choice entered")
    query="""INSERT INTO room_sevices(cid,service_choice,quantity_of_clothes,service_bill) VALUES(
            '{}','{}','{}','{}')""".format(cid,choice,quantity_of_clothes,service_bill)    
    cr.execute(query)
    db.commit()
    
def otherservices():
    createTable ="""CREATE TABLE IF NOT EXISTS OTHER_SERVICES(CID VARCHAR(20),
                CHOICE VARCHAR(30),QUANTITY VARCHAR(30),OTHERSERVICE_BILL VARCHAR(30));"""
    cr.execute(createTable) 
    cid=input("Enter Customer ID:")
    print("1.Spa service: Rs.1000/-")
    print("2.Massage service: Rs.1000/-")
    enter_choice=int(input("Enter the choice:"))
    quantity=int(input("Enter the number of persons:"))
    if choice==1 or choice==2:
        otherservice_bill=quantity*1000
    else:
        print("Wrong choice entered")
    query="""INSERT INTO other_sevices(cid,choice,quantity,otherservice_bill)
             VALUES('{}','{}','{}','{}')""".format(cid,enter_choice,quantity,otherservice_bill)   
    cr.execute(query)
    db.commit()

def totalamount():
    createTable ="""CREATE TABLE IF NOT EXISTS TOTAL_AMOUNT(CID VARCHAR(20),NAME VARCHAR(30),
                 ROOM_RENT INT ,RESTAURANT_BILL INT ,SERVICE_BILL INT,OTHERSERVICE_BILL INT,GRANDTOTAL INT);"""
    cr.execute(createTable) 
    cid=input("Enter Customer ID:")
    name=input("Enter Customer Name:")
    grandTotal=room_rent + restaurent_bill + service_bill  + otherservice_bill
    query="""INSERT INTO total_amount(cid,name,room_rent,restaurant_bill,service_bill,otherservice_bill,
             grandTotal) VALUES('{}','{}','{}','{}','{}','{}','{}')""".format(cid,name,room_rent,
             restaurant_bill,service_bill,otherservice_bill,grandTotal)
    cr.execute(query)
    db.commit()
    print("**** HOTEL MONTREAL ****")
    print("**** CUSTOMER BIILING ****")
    print("CUSTOMER NAME: " ,name)
    print("ROOM RENT: Rs. ",room_rent)
    print("RESTAURENT BILL: Rs. ",restaurent_bill)
    print("ROOM SERVICE BILL: Rs. ",service_bill)
    print("OTHER SERVICE BILL: Rs. ",otherservice_bill)
    print("---------------------------------------")
    print("TOTAL AMOUNT: Rs. ",grandTotal)
    print("---------------------------------------")
    
    
def search_record():
    cid=input("ENTER CUSTOMER ID : ")
    query="SELECT * FROM CUSTOMER_DETAILS WHERE CID= %s"
    cr.execute(query,(cid,))
    data=cr.fetchall()
    if data:
        print(data)
        return True
    else:
        print("Record Not Found Try Again !")
        return False
    
def delete():
    cid=input("ENTER CUSTOMER ID : ")
    query="DELETE FROM CUSTOMER_DETAILS WHERE CID= %s"
    cr.execute(query,(cid,))

def display():
    query="SELECT * FROM CUSTOMER_DETAILS"
    cr.execute(query)
    data=cr.fetchall()
    if data:
        print(data)
        return True
    else:
        print("Record Not Found Try Again !")
        return False
    
print("\t\t------------------------------------------")
print("\t\t    WELCOME TO HOTEL MONTREAL SRINAGAR")
print("\t\t------------------------------------------")
try :
    x=input("Enter The Password Of Your Database:")
    dr = pymysql.connect(host="localhost",user="root", password=x)
    cur=dr.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS Hotel_Management_System")
    db=pymysql.connect(host="localhost",user="root",password=x,db="Hotel_Management_System")
    print("Connected Sucessfully !!!!")
    Data="USE Hotel_Management_System"
    cr=db.cursor()
    cr.execute(Data)
    print("Database Openned!!!!!")
except Exception as e:
    print("Database connection error",e)
while(True):
    print("1--->Enter Customer Details\n")
    print("2--->Booking Record\n")
    print("3--->Calculate Room Rent\n")
    print("4--->Calculate Restaurant Bill\n")
    print("5--->Calculate Room Services Bill\n")
    print("6--->Calculate Other Services Bill\n")
    print("7--->Display Customer Details\n")
    print("8--->GENERATE TOTAL BILL AMOUNT\n")
    print("9--->Delete a record\n")
    print("10-->Display all records\n")
    print("11-->EXIT\n") 
    choice=int(input("Enter Your Choice:"))
    if choice==1:
        customer_details()
    elif choice==2:
        booking()
    elif choice==3:
        roomrent()
    elif choice==4:
        restaurant()
    elif choice==5:
        roomservices()
    elif choice==6:
        otherservices()
    elif choice==7:
        search_record()
    elif choice==8:
        totalamount()
    elif choice==9:
        delete()
    elif choice==10:
        display()
    elif choice==11:
        break
    else:
        print("Wrong choice entered")

    
    
        
    
