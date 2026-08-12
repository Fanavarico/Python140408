#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 21:01:28 2026

@author: apm




App besazim ok? --> ke Biad QUIZ MANAGEMENT.

Hadaf --> Yek app ke quiz ha dakehelsh bashe, daneshjo ha ham javab bedan o.. (QUIZ MANAGEMENT)



[] Box dar nazar migiram.



User ha --> daneshjoa --> sabte nam konan , esmeshono benevisan --> zakhriash ()
Table berizameshoon --> Jadval --> Users --> Full name, email , ... ...


---> Yek panel besazam ostad biad tarh kone (advanced)

--> Khodam aslan -> 5 ta quiz bsihtar nabashe [MAN] --> yek file behesh quiz_data quiz , question....


soal--> jadval dashte basham , gozine ham jadval --> sahihe sahih 





database.py --> in file zirsakhte database (na table)


file database.py --> runable nist --> 3 ta zarf (variable) ,yek tabe (yedone az hamin zarfaro)

engine , Base , Session [get_db()]

chera inaro dar yek file mziarim k runable nist? --> chon inaro 
importeshon konim



yek file man mikham k table ham ro oonja besazam structure (sakhtar) , import konm

models.py





Omadam dar file e models.py kolan 3 ta class sakhtam k az Base ers bari kard

imn see clas hamon se ta table (jadvale man hast)


aya runable? na --> ruensh --> 3 ta class .
ina mitonan import shan


shoma age bekhay k hamon lahze databaset sakhte beshe va table ha ham sakhte beshe

Base.metadata.create_all(engine)


file setup_db.py ro k sakhtam ino toosh gozahstam rftm runesh zdm


(base) apm@APMs-MacBook-Pro Project2_final % python3 setup_db.py
Database created successfully!


mige sakhte shod --> mubinam

file e jadid bename test_db_columns.py


(base) apm@APMs-MacBook-Pro Project2_final % python test_db_columns.py 
Tables in database:
- users
- questions
- choice




ta alan



----dataabse.py (engine,....)
----models.py (table ham bodan)
----setup_db.py (intoo misaze .db , table hasho) az dota file e bala




man yek jaei mikham az models.py --> class ro bekesham biron

question ham ro besazam --> seed.py

mitoni mostaghim dakheel seed.py --> hey clas haro import koni
va shoro koni soal haro besazi , 5 ta soale pish farz mikahm ...


vared koni , soal besazi , soal pasokh ,--> tabe ha 

hey tekrar naashe dar file seed.py


crud.py besaz k az function hae bashe k seed.py azash estefade kone

dakhele file e crud.py koi tabeye helper gozahstam , mitonam ino afzayesh ham bedam



dakehels seed.py az hamin tavabe ye crud.py estefade krdm

seed.py ro agar riun konm --> in soal ha rikhte mishe ? dakhele database am.




(base) apm@APMs-MacBook-Pro Project2_final % python setup_db.py 
Database created successfully!
(base) apm@APMs-MacBook-Pro Project2_final % python seed.py
Tables created successfully
Creating questions...
Questions created successfully
finalizing...







Yek chizi mikhahi k afrad bian sabte nam konan . va soal ha namayesh dade beshe va 
javab bedan , score bedi


1- CLI app

python main_cli.py --> run beshe



2- GUI app

python main_gui.py --> rub beshe



Takalif
Gui --> TKinter , Pyqt











main.py --->


input() , tkinter()



Core kar ro besazi -> be in noghte






Django , fastapi



Backend --> 

@/login
def login():
    username , email
    from crud.py


in views.py




html, javascript, --> agent haye emrozi

HTML ,... 

Bacxkend --> django, fastapi 




"""





