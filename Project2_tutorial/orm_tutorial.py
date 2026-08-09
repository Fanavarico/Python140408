#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 20:48:36 2026

@author: apm


ORM 



ta inja yad gerefti connection = .db vasl shi 

cursor besazi  

ba cursor.execute(' dastor bezabane SQL bedi')


khob man bayd sql balad basham


khob ORM (Object relational Mapping)


Pythonic beenevism



cursor.execute('''
    INSERT INTO  questions (quiz_id ,text ) 
    VALUES (?,?)
    ''' , (1 , "jAVABE Print('salam') che msihaavd"))




Questions(quiz_id=1 , text='javabe print chist')




ORM -->Man yek ketabkhon ei hastam k ejaze midam pythoni benevisi sql eto







"""

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

from sqlalchemy import create_engine

engine = create_engine('sqlite:///quiz_management2.db')

#url --> supabase --> cloud darim (abri)


#supabase --> shoam roo run dari appeto 

#haminjori data dare  insert mishe, pak mishe ,.... update mishe


#niazi b code ndri bzni ta database, Table hato bebini 


#supabase --> yek GUI , website miri dakhelkesh

#tak tajke table hat khoshgel radifas ,...

#Amn hast , ham cost-effective hazine ye negahdari data


#supabase addres mide --> databse 


from sqlalchemy import create_engine

engine = create_engine('sqlite:///quiz_management2.db')






from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String #ina type hastan

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



#boro file e second_try





#ino ag run konam chizi nmibinam



from sqlalchemy import create_engine
engine = create_engine('sqlite:///quiz_management2.db')
#yek engine fght sakhte --> zarfi bename engine











from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String #ina type hastan

Base = declarative_base()
class Question(Base):
    __tablename__ = 'questions'
    
    id = Column(Integer,primary_key=True)
    quiz_id = Column(Integer, nullable=False)
    text = Column(String,nullable=False)

#yek class sakhte 


#hadafe man ine ke yek database besazam , tooye databasame , yek jadval besazam/


Base.metadata.create_all(engine)

#ham database, ham tabel haro misaze



#har dafe man ino run konm , az aval nmisaze , pak nmikone


#1--> ag db nist --> file .db ro besaz --> table haro besaz
#2-->ag db  hast -> vasl shod be .db --> table ha ag nist --> table haro besaz
#3--> ag db hast --> vasl sho b .db --> table ha ag hast --> ag updati (sotoni) emal kon






from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine) #engine ->harjaei k engine



session  = Session() #yek object az class misazim

#insert.......

q1 = Question(quiz_id=1 , text='print salam chi msihe')


session.add(q1) #data --> table
session.commit() #-->sabt msihe tooye hardet




#--> negah kardan, select * from ...


quiz_ha = session.query(Question).all()

#kole tag\
    
    
for question in quiz_ha:
    print(question.quiz_id)
    print(question.text)
    
    

