"""
Created on Sun Dec 14 17:36:25 2025

@author: apm

ADV_L1 , L2 , L3 , L4 --> GITHUB code ha 



ADV _L5


------------------------
ADV_L6
ADV_L7


---------
ADV_PROj1 --> 
time , deadline
ADV_Proj2 --> 


GPT
W3school
tamrin
code Github

---

"""



'''
----- Overview ---------------


Human (en) <---python ---> machine (0,1 binary)

python-- > language --> vocabs and grammar

1-Python built in functions (tavaeye dakheli) -->developeraye python ino
narenj --> print() input() len() type() ,......
https://docs.python.org/3/library/functions.html


2- Keywords ->python az bala b paeen az chap b rast --> code ro mikhone
va run mikone --> in logic , mantegh ro taghir bdid 
if , if els, elif 
for , while
and or in ,.....

-----unreserved-------- sefid
3- Variables ( moteghayer) zarf 
zarf --> esm = meghdar
3.1. Numbers (int,float , complex) ** * / + -  | == != > < >= <=
3.2. Bool (True , False)
3.3. Str --> ' reshte ee az keyboarde shoma
   3.3.1 Zarf[index]
   3.3.2 zarf[start:end+1:step]
   3.3.3. str.function()  zarf.lower() .upper() .title()
   
3.4. Iterables --> tooye yek zarf -> chand meghdar brizim mesle4,5value

3.4.1. List
3.4.2. Tuple
3.4.3. Set
3.4.4. Dictionary





'''


#-----------------------
#-----Shoroot----------
#shorot se no hastan
sen= int(input('senet cheghadre?:'))

print('salam')


#senet 1 ch 2002w932829839 --> hamsihe salam print
#gahi mikhay y khat ya yek bakhsh az codet --> sharti
#

#---1.Just if --> rahzan
#yani baraye ye bakhshi fght age shart==True mige ejra kon
#ag false shod -->bikhial mohem nist
'''
     |
     shart
  -----------
  |true      |false
  kar1        
  ------------
        |
        |

'''
if sen>10:
    print('salam')
    
#sen>10 --> True --> salam
#sen<10 --> False --> ...



#-----2 - dorahi if else
#ag true shod kare 1 , false shod kare 2
'''
     |
     shart
  -----------
  |true      |false
  kar1        kar2
  ------------
       |
       |
       
'''

if sen>10:
    print('salam')
else:
    print('khodafez')
    
#sen>10 --> True -->salam
#sen<10 --> False --> khodafez






#-if ,elif else --> dorahiaye to dar too hastan

'''
     |
     shart1
  -----------
  |true      |false
  kar1        shart2
  |           |
  |      -----------
  |     |true      |false
  |     kar2        kar3         
  ------------
       |
       |
       
'''

if sen>18: #yani age bala 18
    print('salam')
elif sen>15: #yani ag beyne 15 ta 18
    print('nazdiki')
else: #yani paeentar az 15
    print('khodafez')
    
    
    


#=======================
#=======================
#=======================
#=======================
#----LOOPS (halghe ha)

#For , While


'''
for --> shomarande i , j, k , el esm -->zarf
ZARF tooye ye list mire --> hey zarfe ro mziare jaye list
hey code ro ejra mikone

'''




for i in [1,2,3,4,5]:
    print('salam')

'''
i --> 1,2,3,4,5 --.code ro ejra mikrd

i=1  print('salam') -->salam
i=2  print('salam') -->salam
i=3  print('salam') -->salam
i=4  print('salam') -->salam
i=5  print('salam') -->salam

salam
salam
salam
salam
salam

'''

for j in [1,2,3,4,5]:
    print('salam')





for ali in [1,2,3,4,5]:
    print('salam')


#chan khat ta madami k 
for ali in [1,2,3,4,5]:
    print('salam')
    print('khodafez')


#keywords -->banafsh ha mantegh or beham mzidn
#vaghty maiy biron mantegh sare jashe


for i in range(0,100,2):
    print('salam')
    
    
'''
i=0 
i= 2 
i=3 
.....
'''


#static repeat --> yekario tekrari anjm midad


#dynamic repeat --> az hamon i , ya shoamrande ham estefade



for i in range(0,101):
    print(i)
    
    
'''
i=0 --> print(i) --> print(0) --0
i=1 -->print(i) -->print(1)-->1

0
1
2
3
4
5
6
7
.....

91
92
93
94
95
96
97
98
99
100

'''


for i in ['ali','vahid','hamid']:
    print('salam')

'''

i= ali , print('salam') -->salam
i= vahid , print('salam') -->salam
i='hamid' , print('salam') -->salam

'''

my_names= ['ali','vahid','hamid']

for i in my_names:
    print('salam')




my_names= ['ali','vahid','hamid']
for name in my_names:
    print('salam')



#beram done done name haye my_names ro behesh dastresi peyda konm
#hala dorose inja too ha rloop az 'salam ' estefade mikonam
#ama man mitonm brm b name element haye yek iterable(list) dastresi peyda konm
#-0-->iteration


#for looop
#1- static repeat 
#2-dynamic repeat
#3-iteration......
my_names= ['ali','vahid','hamid']
for name in my_names:
    print(name)

'''
name --> ['ali','vahid','hamid']

name = ali --> print(name) , print(ali) -->ali
name = vahid--> print(name) , print(vahid) -->vahid
name = hamid--> print(name) , print(hamid) -->hamid

'''
print(my_names) #['ali', 'vahid', 'hamid']

#iteration konam --> beram varrsi toye ye list

#yani gahan ye jahaee shoam niaz dari varde yek listi beshui
#done donashono bekeshi biron
#ya taghiri emal koni , chizi check koni ,......

#for , shorot gharo ghati mishan



my_names= ['ali','vahid','hamid','reza','farnoosh' ,'ahmad','amir','maryam','arash','aysan']

for name in my_names:
    print(name)


#bejaye inke begam mikham name porint she , andazashon print she???/


for name in my_names:
    name_size = len(name)
    
    
print(name_size) #5


my_names= ['ali','vahid','hamid','reza','farnoosh' ,'ahmad','amir','maryam','arash','aysan']
for name in my_names:
    name_size = len(name)
    if name_size>3:
        print(name)
    
'''
vahid
hamid
reza
farnoosh
ahmad
amir
maryam
arash
aysan

'''
    
my_names= ['ali','vahid','hamid','reza','farnoosh' ,'ahmad','amir','maryam','arash','aysan']
for name in my_names:
    name_size = len(name)
    if name_size>3:
        print(name) 
    
    
'''
name = ali --> name_size=len(ali)=3 , 3>3 ->false
name= vahid --> name_size=len(vahid)=5 , 5>3 -->True print(name) print(vahid) -->vahid


''' 
    


my_names= ['ali','vahid','hamid','reza','farnoosh' ,'ahmad','amir','maryam','arash','aysan']
for name in my_names:
    if len(name)>3:
        print(name) 
    



my_names= ['ali','vahid','hamid','reza','farnoosh' ,'ahmad','amir','maryam','arash','aysan']

#ye list daram k koli element dare
#aval done doen be elemtn ha dastresi peyda konm
#bad vase hardoonashon, harfe avalo bbinam
#bad check konm ag a bood printeshon konm

#done done dastess--> iteration
    
for name in my_names:
    if name[0] == 'a':
        print(name)

'''
ali
ahmad
amir
arash
aysan

'''

#iteration --> too dle for , if , .....

#iteration : dar yek iterable (list,set,.) becharkhi yeseri shorot ro check koni

#shorotsh ag True shod? -->chiakr mikhay koni?


#---1 - print-----------

my_names= ['ali','vahid','hamid','reza','farnoosh' ,'ahmad','amir','maryam','arash','aysan']
 
for name in my_names:
    if name[0] == 'a':
        print(name)

'''
ali
ahmad
amir
arash
aysan

'''



#---2- Beshmorishon
my_names= ['ali','vahid','hamid','reza','farnoosh' ,'ahmad','amir','maryam','arash','aysan']

count = 0

for name in my_names:
    if name[0]=='a':
        #print(name)
        count = count + 1
        
'''
name = ali , if name[0]=='a'-->True --<> count = count +1 = 0 +1 =1
name = 'vahid' , if name[0]=='a' -->False -->  count = 1
hamid , reza, farnoosh
name = ahmad , if name[0]=='a'-->True --> coutn = count +1 = 1+1 =2

'''

print(count) #5
print(len(my_names)) #10
#az 10 ta esm, 5 tash ba a shoro mishe



#3--- Inaro joda kone brize too y liste dg
my_names= ['ali','vahid','hamid','reza','farnoosh' ,'ahmad','amir','maryam','arash','aysan']

mylist = []

for name in my_names:
    if name[0]=='a':
        #print(name)
        #count = count + 1
        mylist.append(name)
    
        
        
'''
name=ali , if name[0]=='a' -->True -->mylist.append(ali) --> [] , mylist = [ali]
name= vahid , if name[0]=='a'->False 
name hamid , reza , frnosh
name=ahmad --> if name[0]=='a'-->True -->mylist.append(ahmad)--> [ali] --->[ali,ahmad]


[ali,ahmad,.........]

'''
        
print(mylist) #['ali', 'ahmad', 'amir', 'arash', 'aysan']
print(len(mylist)) #5
        


#4- remove ono did -->filtering

for name in my_names:
    if name[0]=='a':
        my_names.remove(name)
        
print(my_names)#['vahid', 'hamid', 'reza', 'farnoosh', 'maryam']

#remove , pop --> 
mylist=[1,2,3,4]

for i in mylist:
    i=i+1
    
#i -->shoamrande namone , 1,2,3,4 mipare badi miapre ghabli



forces = [100,60,300,400,50]
displacement = [10,5,14,17,18]
    
#stress = force / displaacement 

#stress_list = [.. , .. , .. ,, ]

#for force in forces:
#    for displace in displacement:
        
    
#for yechiz in chiz ha

#indexi rftar koni


my_names= ['ali','vahid','hamid','reza','farnoosh' ,'ahmad','amir','maryam','arash','aysan']
for name in my_names:
    if name[0] == 'a':
        print(name)
#name = alu , vahid , hamid ,...
#mikahsti b element brse --> name estefade 


#i= 0,1,2,3...index
#i -->index kar kon
#ag bekhay b eklemetn my_names[i]
for i in range(len(my_names)):
    print(i)
    
'''
0
1
2
3
4
5
6
7
8
9
'''

for i in range(len(my_names)):
    print(my_names[i])
    
'''
ali
vahid
hamid
reza
farnoosh
ahmad
amir
maryam
arash
aysan
'''

my_names= ['ali','vahid','hamid','reza','farnoosh' ,'ahmad','amir','maryam','arash','aysan']
for name in my_names:
    if name[0] == 'a':
        print(name)
        
        
my_names= ['ali','vahid','hamid','reza','farnoosh' ,'ahmad','amir','maryam','arash','aysan']
for i in range(len(my_names)):
    if my_names[i][0] == 'a':
        print(my_names[i])
        
        
#-------------------------

forces = [100,60,300,400,50]
displacement = [10,5,14,17,18]
stress_list=[]

for i in range(len(forces)):
    stress = forces[i] / displacement[i]
    
    stress_list.append(stress)
    
    


print(stress_list)

#[10.0, 12.0, 21.428571428571427, 23.529411764705884, 2.7777777777777777]



for force in forces:
    for dis in displacement:
        print(force, dis)


count=0
for force in forces:
    for dis in displacement:
        count  = count + 1

print(count) #25





count = 0 
for i in range(len(forces)):
    stress = forces[i] / displacement[i]
    
    stress_list.append(stress)
    count=count+1
    
print(count)      #5


#--------------------------------
#--------------------------------
#--------------------------------
#--------------------------------
#--------------------------------
#--------------------------------

'''

while --> for  ba y ravande


i , ....



while shrt:
    ye kari kon
    
    
    
    



'''


#sen = 18

#while sen>10:
#    print('salam')


'''
aval bayad halgeh True beshe ta vare beshe
sen>10 --> True --> print('salam')
salam , salam , salam , salam

'''


#sen=0
#while sen<10:
#    print('salam')
    
#for i in [1,2,3,4,5,6,7,]


sen=0
while sen<10:
    print('salam')
    sen= sen + 1
    
'''
sen=0
sen<10 --> True -->print(salam) salam sen = sen+1 = 0+1 =1
sen<10 --> 1<10 --.True -->print(salam) salam sen= sen+1 = 1 +1 =2


sen=8 --> 8<10 ->True -->salam sen = 8+1 = 9
sen=9 --> 9 <10 -->True -->salam sen= 9+1 =10
10<10 -->False  -->logice hamishegi python edame mide
'''

'''

for i in range(start,end,step):
    kari



i=start
while i<end:
    kar
    i = i + step


'''


#------------------
'''
1- start ro benevisid 
2- shart True bashe baraye vorod
3- bayad sharte ekhtetam dashte bashid





'''
#for i in [1,2,3,4]
#i=1


#----->errore aval

while i<10:
    print('salam')
    i = i+1
    
#i is not defined
#ejra nmsihe, doros ejra nmsihe, error

#error mide ---> i is not defined 



#-------


i=20

while i<10:
    print('salam')
    i= i+1
    
'''

i=20

while shart rue mibashad felan


i<10 --> 20<10 --> False 




'''

#1- start bezarid
#2- bayad vared halgeh beshe, begoone ee start bzarid

#----------

#for i in [start ,....end]

#for i in [1,2,3,4,5]

#i =1 , i=2 i=3 i=4 



i=0

while i<10:
    print('salam')
    
    
'''
i=0 defined
i<10 -_> 0<10 -->Trye 0-->varde loop mishe

ta zamani k i<10 hast print kon salam

i=0 i<10 0<10 True ->salam  loop
i<10 ? --> i=0 0<10 -->True -_>salam
i=0
i=0
i<10
ta abd print('salam')



'''   


i=0

while i<10:
    print('salam')
    i = i +1
    
    
'''
i=0 defined
i<10 0<10 True -->varede halghe

--> print('salam') salam --> i = i+1 = 0 + 1
i<10 --> 1<10 True -->salam --> i = i+1 = 1 + 1 = 2

i=9 --> 9<10 True --> salam --> i = i + 1 = 9+1 = 10
i<10 --> 10<10 -->False --> miad


'''
    
#i defined mikonam , na bayad i am sharto
#na i = i+1   
for i in range(0,10):
    print('salam')
    
 
    
#--------------
i=0
while i<10:
    print('salam')
    i = i +1


#

'''

while true hast y kari kon


'''

name = input('vared konid name mahsolo:')
code = input('vared konid code mahsoolo:')
price = input('vared konid price:')

text = f''' name : {name} , code : {code} 
hazine : {price}
'''

print(text)

answer= input('aya etelaate balaro ghabol mikoni?')


if answer.lower().strip() == 'yes':
    print('sabt shod')
    
else:
    print('sabt nashod')

#---> strateghy frgh mikone
#ta zamani k trf yes nazade , ag zad no , dobare azash name , cod , price ,..

#

#------


name = input('vared konid name mahsolo:')
code = input('vared konid code mahsoolo:')
price = input('vared konid price:')
text = f''' name : {name} , code : {code} 
hazine : {price}
'''
print(text)
answer= input('aya etelaate balaro ghabol mikoni?')

#ag answere taraf yes nabashe -->vared mishe
while answer.lower().strip() != 'yes':
    print('khob mojadad por konid')
    name = input('vared konid name mahsolo:')
    code = input('vared konid code mahsoolo:')
    price = input('vared konid price:')
    text = f''' name : {name} , code : {code} 
    hazine : {price}
    '''
    print(text)
    answer= input('aya etelaate balaro ghabol mikoni?')


print('etelaate mahsole shoma sabt shod')


'''
WHILE --->
1-varede halghe shae -->shart darim

2- Ekhttam bezarim vase trf



'''

    
    
#yes --> etelaate mahsole shoma sabt shod 



#while True --> True ta abd bdoen hcih checki asan vared mishe
#while shart ---> tooy dele while yehori sharto naghs

#rahe dovom -->Hamishe true --> 


while True:
    name = input('vared konid name mahsolo:')
    code = input('vared konid code mahsoolo:')
    price = input('vared konid price:')
    text = f''' name : {name} , code : {code} 
    hazine : {price}
    '''
    print(text)
    answer= input('aya etelaate balaro ghabol mikoni?')
    
    if answer.lower().strip()=='yes':
        break
    
print('moafaghh')  



#----------------

#continiue , pass, break
#for , while


#pass -->

for i in range(0,10):
    pass
    
    
    
    
    
#name = 'ali'



for i in range(0,5):
    print(i)


'''
0
1
2
3
4

'''

for i in range(0,5):
    print(i)
    if i==3:
        continue
    
    
'''
0
1
2
3
4

#-----
i=0 , print(i) -->print(0) false --> 0
i=1 , print(i)-->prtint(1) false-->1
i=2 , print(i)-->prtint(2) false-->2
i=3 , print(i) -->print(3)-->3 ,if i==3 True continieu 
i=4


'''


for i in range(0,5):
    if i==3:
        continue
    
    print(i)
    
    
'''
0
1
2
4

i=0 , if i==3 ? na -->print(i)-->i=0  
i=1  1
i=2 2
i=3 --> if True ->continiu XXPRINTXXX i=4
i=4  pirnt 



'''



for i in range(0,5):
    print(i)
    if i==3:
        break


'''
i=0 --> print(i) -->print(0) -->0 if i==3?
i=1 --> print(i) -->print(1) -->1
i=2 --> print(i) -->print(2) -->2
i=3 -->print(i) -->print(3)-->3 , if i==3 -->break 
...
0 1 2 3

0
1
2
3

'''

for i in range(0,5):
    if i==3:
        break
    
    print(i)
    


'''
i = 0 , print(i) -->print(0 ) -->0
i = 1 , print(i) -->print(1 ) -->1
i = 2 , print(i) -->print(2 ) -->2

i=3 , if i==3  -->out 


0
1
2
'''




#-------------------------
'''
CONCLUSION


shoma yek karfarma, ya y sehrkat , CTO, CEO 
startup 

ide ee dari bayad az sefr besazi --> System design ->details roo code
miay too kar -->y option ezafe, feature ezafe koni, buggio begiri

Bug --> mese ye python az bala b paeen az chap b rast 
bshin bekhon --> bekhon too maghz compile




Feature ezafe kardan??
matn ya yek ide farsi darid -->translate --> Python

trasnlate
yek donyaee bozorg az tamame chiz ha , str.title()  list.append() for if break , input ,...



TIP  ----> ROAD MAP <-------

1-python built in
2-keywoprd
3-variable


namayesh bdi (monitoring) bbini chnad (debug) --> print()
input() ---> shabih saze ine k az user chizi mgiir

shoma hargah khasti chzii zakhrie koni ag ydonas zarf -->3-variables [number, str
                                                                      . ]
answer az user --> answer -->xakhir -->str -->function , acces,...


ag jaee --> 'age shenidi' dorahi, vase yeseri afrad , dorahi haye too dar too , range bandi clasification
--> Conditional (dastoorate sharti)
1--->agar yek rahzane -->baraye yekseri jaha yekseri code --> just if
2- dorahie --> ag inshod inja ahg nashod --> if else
3- chanta dorahi , daste bandi ha , range bandi --> if elif else


#----ag jaee tekrar bood
#yechizi besoate saabet tekrar mishod, ye kar , y nevshte

For loop --> static repeat

#ag ychzii bayad taghri ham kone tekrar
for loop --> dynamic repeat for i in range(o0) i--> dastoroat

ye listi , set -->mikhay bri toy on done done ye balaee sarshon

for iteration --> iteration (for , if ,else ,. continiue, count , list.append() , break)


#------Ag ta zamani
ta zamani k shndii 
ta zamani k user felan akrd felan kone

While -->
1- khodet shart mziari toosh ekhtetam mzire
yeseeir shart True nm,ishe nmire too lop , onae k mire to olop 

2- hame bayd brn too lop ,yeseria mian biron While True



'''










