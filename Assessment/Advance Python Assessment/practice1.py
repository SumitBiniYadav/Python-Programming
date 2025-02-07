import pymysql  #imports the pymysql liabrary from the liabrary 

mydb = pymysql.connect(host="localhost", user="root",password="")   #establishes conncection to A MYSQL XAmmp 
mycursor = mydb.cursor() #cursor is method () creates object that allows you to execute and fetch results

mycursor.execute("CREATE DATABASE if not exists Banking")  #executes the code
mydb.commit()   #saves the commited changes to the database

mydb = pymysql.connect(host="localhost", user="root", password="",database="Banking")
mycursor = mydb.cursor()

mycursor.execute("CREATE table if not exists Banker (Id int primary key auto_increment, bname varchar(80), bemail varchar(80), bmobile bigint, bpass varchar (80))")
mydb.commit()