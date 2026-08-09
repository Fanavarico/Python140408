#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 20:29:50 2026

@author: apm

oon bala samte rast agar dar /USERS/APM/DESKTop
tooye desktop run mishe 

first_try.db (mohtaviate tamame jadvael toshe) oponja zakhire


jaei k code run mishe

ye ravesh



raveshe dovom--> az IDE/EDITOR baraye run

Terminal

Mac --> Terminal --> Command + space --> terminal -> safe siah


Windows --> Powershell (search bznid)



CLI (command line interface)--> khate farman
GUI (graphical user interface)-->rabete geraphici karbar 

windows hamechit GUI hast , folder beshi , mibini , click mikoni
file hato mibini, click bzni new file , hazf koni


CLI --> ba code mitoni koni, ba code ba kole engine , kernel computeret harfbzni



vaghty vared mishi aval kojaei?

(base) apm@APMs-MacBook-Pro ~ % pwd
/Users/apm


(base) apm@APMs-MacBook-Pro ~ % cd desktop
(base) apm@APMs-MacBook-Pro desktop % pwd
/Users/apm/desktop




kolan 

(base) apm@APMs-MacBook-Pro ~ % pwd
/Users/apm
(base) apm@APMs-MacBook-Pro ~ % cd desktop
(base) apm@APMs-MacBook-Pro desktop % pwd
/Users/apm/desktop
(base) apm@APMs-MacBook-Pro desktop % python3 first_try.py





"""

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



'''
Che biay az dakhele spyder run bzni --> first_try.db jaei k run krdi


az raveshe dovom terminal (CLI) -->runesh koni --> first_try.db  



Editor (VS code ) --> run --> CLI run 




'''


