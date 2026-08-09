#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 20:55:23 2026

@author: apm
"""
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



#hayati

#BAse -> har tablke i k asakhatam -> ers borde Base

Base.metadata.create_all(engine)

#ham database, ham tabel haro misaze



#har dafe man ino run konm , az aval nmisaze , pak nmikone


#1--> ag db nist --> file .db ro besaz --> table haro besaz
#2-->ag db  hast -> vasl shod be .db --> table ha ag nist --> table haro besaz
#3--> ag db hast --> vasl sho b .db --> table ha ag hast --> ag updati (sotoni) emal kon






