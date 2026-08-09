
"""
In The Name of GOD

Folder 2 --> Project2_tutorial

Folder 3 --> Final_Project

Created on Sun Aug  9 20:17:21 2026

@author: Ali Pilehvar Meibody



Project2_Final


Human(en)<----python----> Machine(0,1binary)

Python:
    1-Python built in functions
    2-Keywords 
    3-VAariables (moteghayer)
        3.1.Numbers (int,float,complex)
        3.2.Bool 
        3.3.Str
        3.4Iterables (List,tuple,..dict)
        
        
        
Moteghayer ha rooye RAM zakhire mishavand 
yani shoma agar computer khamosh shavad

che moishaavd --> tamame moteghayer ha hazf mishaavd



CPU (process)<--> Cache <--> RAM(volatile farrar hafeze 2,4,8,16,32Gb) 

RAM <----- HARD (265 Gb, 512 Gb , kond hast ama non volatile)


computer ro khamosh mikoni, cpu khamoshe, cache mipare , ram mipare, Hard zakhire dare

roshan mikone, oon barname e k miari bala (browser, app , chatgpt) , az hard yek meghadar etellat
ro miare roo RAM --> CPU process shoma bbini



HARD ---> DAKHELESH CHIZI ZAKHIRE



Database (paygahe dade) --> yek jaei hast k koli table (jadval) dakhelesh hast


DB  haye mokhtalef : mysql , sqlite , postgre ,.... --> (Ask GPT)


sqlite ro bardashatm , real sqlite .


yek zabane --> yek barname jodast --> python -->  neevshtan . 


Ketabkhone pythonesham sakhtan, k az tarighe python 

pip install sqlite


Ketabkhone ei bekhahi yad begiri 


nasb mishe --> mitonid import

"""

import sqlite3


connection = sqlite3.connect('quiz_management.db')


#ag nabashe --> misaze
#agar bashe vasl mishe


#harjaei k bezari, harjaei k run konish
cursor = connection.cursor()



'''
Table

column1(str) column2 column3   column4(int) 
...       ...      ...
user1      ali     pilehvar    ....  .....

'''

cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )          
     """)

'''

Table name : users


id(int , pk)      name(TEXT)     email(TEXT)
0                 ali            ali....@...
1
2
3
4
....



'''

#sabtesh kon roo hard
connection.commit()  #roo hard

#bebandesh
connection.close()



# first_try.py






#Table creation -----
import sqlite3
connection = sqlite3.connect('first_try.db')
cursor = connection.cursor()
cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )          
     """)
    
connection.commit()
connection.close()




#-----Insert konim 
import sqlite3 
connection = sqlite3.connect('quiz_management.db')

cursor = connection.cursor()
#aval jadvalamo bayad besazzama 
#badesh insert vared konm
cursor.execute("""
    INSERT INTO  questions (quiz_id ,text ) 
    VALUES (?,?)
    """ , (1 , "jAVABE Print('salam') che msihaavd"))

connection.commit()





#-------bebinam chijori shode
import sqlite3 
connection = sqlite3.connect('quiz_management.db')
cursor = connection.cursor()
cursor.execute("""
    SELECT * FROM questions
    """)

quizz = cursor.fetchall()
print(quizz)




#----Boro file e ORM bekhonesh


