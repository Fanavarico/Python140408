#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 20:08:08 2026

@author: apm



Quiz ro daram , mikham quiz hamo dostan , zakhire konm 


quiz ---> chanta question , --> question --> gozine (choice)



"""

Quiz1 = 'Python1'

#az quiz1 , question1 
qeustion1_1 = 'javabe print(salam) chi mibashad '

choice1_1_1 ='s'
choice1_1_2 = 'sal'
choice1_1_3 ='salam salam'
choice1_1_4 = 'salam'

correct_1_1 = 4


#ROOYE RAM zakhire mishe

#zmaani k dostan . mane ali miam spyder ro mibndm , tamme ina hazf mishe az roo ram



#baraye sakhtan question , choice eb ndre

#kenareina, javabe karbaramam zakhire konam


numebr_karbar = input('namber:')
print(qeustion1_1)
print(choice1_1_2)
print(choice1_1_3)
print(choice1_1_4)

entekhab = input('entkehab:')


if entekhab ==1 :
    
    choice_user_1_1_1 = 1

elif entekhab == 2:
    choice_user_1_1_1 = 2
    
    
#user 2 , user 3 , user 4 ,....


#choice --> variable shode 

#python ro mibndm -> tamame in ha ham az beyn mire 


#RAM --> HARD zakhire beshe


'''

hard --> yekk jaeei k ina zakhire bashe
soala , questiona



run konm , az onja vardare

trf javab mide -> record bshe


100 rooz dg ham bkhm bbinm felan user chi jvb dade save bashe


--> Non-Volatile  (HARD)



YEJA ---> DataBase




Database --> koli Table dakheleshe . table koli soton darim (value)


hard zakhiras , hichvaght az beyn nmire


computer , app rretsrt, computer hamosjrohna, server ghat nashe 


in hamishe zakhire daemi.




2 dalil
1---> hamishe hast (zakhire vaghei , )
2----> managemente asoon , variable variable -> table




questions-----------
id     soal  
1      print('salam') ch mishavad
2      print('khodafez') ch msihavad
3      for i in range(0,10): print(i) chi midahad




choice ----------------
id    choice        soal_id
1     sal           1        
2     sala          1
3      sal sal      1
4     salam          1
5     12,3,45        2
6     1,2,.,.10      2
7     1,2,....,9     2
8     0,...9         2


'''
    

    

#database --> Mysql , postgre , Sqlite ,.,... (HARD) || Redis (RAM ) -->cache



#Sqlite --> kh kh sari va bekar hast

#zabon darad , code bayad bzni

'''
sqlite -->

pip install sqlite3



gpt , video youtube , telegram b bande payam midi
'''


#------------------------------------------------------------
#-----
#k ejhaze mdie shoam db besazio ...
import sqlite3


#agar nadari --> misaze .db
#agar dari --> vasl mishe behesh
connection = sqlite3.connect('quiz_management.db') #file misaze bnam .db   .xlsx   .db -> [jadval , .xlsx .xlksx]

cursor = connection.cursor()

#harjae run bznid --> quiz_management.db -->database misaze

#dastoroate sql ro shoma run konid
#dostan --> khode sql mese zaban

#mikham yek jadval besazam baraye user ham (danesh amoozam) --> id , name , email

'''


id       name     email
1         ali     alipilehvar@gamil.com


'''
#cursor --> 
#boro besaz yek jadval bename users
#quiz_management.db --> yekl table bename users besaz
#az aval misaze az aval msiaze
cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )          
     """)

#Out[20]: <sqlite3.Cursor at 0x307f95bc0>

connection.commit()  #roo hard
connection.close()

'''

tabel besaz

sotona --> id , name , email

INTEEGR , TEXT ,..... (GPT BORO BEKHOOON)


python int , float, ..... , str
sql --> INTEGER  , TEXT 

'''







connection = sqlite3.connect('quiz_management.db') #file misaze bnam .db   .xlsx   .db -> [jadval , .xlsx .xlksx]

cursor = connection.cursor()

cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY,
        quiz_id INTEEGR NOT NULL,
        text TEXT NOT NULL
    )          
     """)
     
connection.commit()
#connection.close()

'''


id   quiz_id   text
1      1        soale question ......


'''


#-------Creation of DB

#------Creation of Table

#-----Insert konim 

import sqlite3 

connection = sqlite3.connect('quiz_management.db')

cursor = connection.cursor()

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

'''
[(1, 1, "jAVABE Print('salam') che msihaavd")]




id      quiz id    text



'''




#--------Object relational Mapping (ORM)----------

'''
object 0--> table
class --> table
objecy ---> row
attribute --> columns



'''''


#select * from questions   

#quiz.questions

#tadb quiz.questions tbale ->

cursor.execute("""
    INSERT INTO  questions (quiz_id ,text ) 
    VALUES (?,?)
    """ , (1 , "jAVABE Print('salam') che msihaavd"))






question = Question(
    quiz_id = 1,
    text = 'javabe print(salam) che msihavad')

session.add(quiz)
session.commit()




#pip install sqlalchemy 

#sqlite --> python vasl mikond



from sqlalchemy import create_engine

#---> supabase

#ba orm sakhtam

engine = create_engine('sqlite:///quiz_management2.db')




#-----table --> cursor. create tagble --> clas besaz

#class --> ers bari --> base


from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


'''
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY,
    quiz_id INTEEGR NOT NULL,
    text TEXT NOT NULL
    
'''


class Question(Base):
    __tablename__ = 'questions'
    
    id = Column(Integer,primary_key=True)
    quiz_id = Column(Integer, nullable=False)
    text = Column(String,nullable=False)




#yek class

#baraye inke in class ha k sakhtam daghighan bshe hamoni k mikhasam


Base.metadata.create_all(engine)


#har clasi k az Base ersbari karde  [table]
#engine --> db , tbale haro misaze
#



#ghadim....
conection  = sqlite3.connect('quiz_management2.db')
cursor = connection.cursor()




from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

session  = Session()


#session.add()
#session.commit()
#session.query()
#session.delete()



#yek object dade
q1 = Question(quiz_id=1 , text='print salam chi msihe')


session.add(q1)
session.commit()




q1 = Question(quiz_id=2 , text='for i in range(0,50 chi msihe')


session.add(q1)
session.commit()










quiz_ha = session.query(Question).all()

#kole tag\
    
    
for question in quiz_ha:
    print(question.quiz_id)
    print(question.text)
    
    
'''
1
print salam chi msihe
2
for i in range(0,50 chi msihe
'''



'''Nokatio ro migam

500,6000






'''







