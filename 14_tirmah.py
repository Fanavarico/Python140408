"""

In The Name of GOD


Created on Sun Jul  5 18:09:11 2026

14 Tirmah 19:39 1405


@author: Ali Pilehvar Meibody







"""




'''


Blogfa ,.....

|

W3school , ... --> Barname nevisi [zaban haye mokhjtalef yad midan]

|

Ai (Chatgpt, gemeni , claud , .....)

[Book] reference




concepti ro yad begirid , sari narid soraghesh


1- Aval ba estefade az AI , hatman bebinid shoma dar kojaye donyaye elm
gharar darid? Django yad begire , be besmela django chist.

Boro bego agah dar elme computer, django kojas, behem Hierarchical (selsele maratebi)

aval computer --> compputer b chan daste taghsim mishe, felan ...


Applciationesh chie (vaghei bego behem)

ch chizhaee niaz e (utility)


Mohito mishnasi, ham mitoni behtar tasmim begiri 



too hamoon conversation (mokaleme)

2 - che topic haee dare in bakhshi  (django, ketabkhone, zabane jadid , for , while if ,..)

topic haro mige, bego ba detail hamashon ro nam bebar .[amade beshe]

hala bego yek barname ye chan jalase ee khobe yek frd b sat he junior motevaset b bala beresad . 

15 jalase , felan jalase


3- jalase bandi ba detail kon begoo behem jalase 1 chi bayad tadris bshe ,..



4- context --> jalase 1 ro shoro kon ta zamani k begam 2 . 
5- hamon kole topic haro coneversation, AI ghavitar ,... --> behem dars bede



sari editor (IDE) va shoro kon b nevshtan haminjori k bht mig
kholase .py dashte bashi k betoni review koni 

va hey run bzni . va say kon naghadane negah koni


Barname nevisi mohm trin negah :
    
            - B in fk kon , manteghi dare , va khodeto bezar jaye on kasi k avalin bar ino sakhte
            - Inghdrm etemad nakon, naghadane ham negah kon , ag nashod chi , ag on shod
            
***
etemad be nafs dahst ebash, 1 milliard adam zaban barname nevisi baladan
hichvaght soalat ro natar bayan kon harchedgh ham fekr mikoni maskhare bashe




har hafte ham oon file hato , moratab


junior --> man baladam dar sathe junior , felan chizo , nokate takmili

senior --> senior behem yad bde   --> alternative [[porozhe vaghei bezani]]
khodeto bendaz too porozhe

yani kh jaha niazi nis k 100% balad bashi

30%  [ba AI] mitoni vared shi

AI prozhe barat -> PRD , milestone 

PRD --> k behet mign felan vizhegi bayad sjate, mini app, service sakhte shod..


PRD --> Milestone (Phase) --> hal krdnesh



Too ghesmate legend bshi --> BOOK 
python microservciesd with fast api



Introduction to= Machine Learning with Python A GUIDE FOR DATA SCIENTISTS
Andreas C. Müller & Sarah Guido  
Oreilley


Hands-on Machine Learning with Scikit-Learn,
Keras & TensorFlow Concepts, Tools, and Techniques to Build Intelligent Systems
Oreilley


Building Python Microservices with FastAPI: Build secure, 
scalable, and structured Python microservices from design 
concepts to infrastructure (English Edition)



Python ,..... XX [system design]

Designing Data-Intensive Applications The Big Ideas Behind Reliable, Scalable, and Maintainable Systems
Martin Kleppmann
Oreilley


'''




#===========================================
#===========================================
'''         Python fundemental          '''
#===========================================
#===========================================

'''


Python --> yek zbaane barname nevisi

ENSAN (En) <-------Python ------> Machine (Binary)


2ghesmat mikonim


------Defined (mishansateshon) ------------
1- Python built in function (print() , input() , len() ,type() , open() ,....) , spyder narenji
search bzn google , gpt  



2- Keywords --> logic , and , or , if , else, def, for , while ,,......





---- Undefined (nemsihnase) --------------

3- Variable (zarf dar nazar migire)

    3.1. Numbers
        3.1.1. int (adad sahih 2, 34 ,4 ,43)
        3.1.2. float (ashari 2.344334, 34232.23423234)
        3.1.3. complex (1j + 5  , 5j  --> aj+b)
        
        a + b = c  XXXXXXXXX
        c = a + b aval zaf ra besaz
        
        algebric operation -> ** , * , / , + -  --> dastor midi , run mishe
        
        comparisonal --> == != > >= < <=  --> urn , soal hast --> montazeri javab
        
                a == b   , a >=b
                
    3.2. Boolean (Bool)
            True, False 
            
    
    3.3. String (reshte ha ) --> horof, kalame , character, jomle ,..
             zarf = 'shdhdsdhsjhdshsd'  '2' != 2  HAR KEYWORDI K rooye keybaordet --> '' mishe sting
             
             index -->
             
             index az 0 shoro mishe
             
             zarf[0]  --> avalin elemnt ro vrmidare
             zarf[1]  --> 1
             
             zarf[0:6]  0,1,2,3,4,5      python 
             avali --> 0 
             akhari --> exclude --> dar nazar grfte  [0:6]  6 na , range(0,5)  5 , np.arange(0,100) 100
             
             str fucntions --> khoroji mide (emal nmikone)
             
             new_str = str.function()
             
             name.lower()   name taghir nmikrd, khoroji midad shoma 
             name.upper()
             name.title()
             
             cleaning text --> app ha vaghty ba text kar
             
             comment minevisid --> mashin 
             
             SALAM  , salam , Salam 
             
             text
             
             if text == 'salam':
                    send_message_todirect(user_id)
                
            if text.lower().strip() =='salam':
                    send_message(user_id)
                    
            salam, Salam , salam  , -> salam dar nazar migire
            
            str method functions
            
            
    Ta inja ma yek zarf dahstim (variable) yek value
    agar chanta value bashe chi?
    4. Iterables --> yechizi k tosh beshe iteration kard 
    
        4.1. List -> ordered , changable , allow duplicated
            a  = list(10,20)
            a = [10,20,'Ali',True, 32.43]
            
            elemenbt
            a[0]
            a[]
            
            chanagble
            a[2] = 20 --> injori taghir mikone
            
            
            list function -> aply
            
            a.append(10) --->kjhorji --> b liste a taghireh mide
            
            a.insert(2,10)
            
            list method functions
            
            
            a.append()
            a.clear() 
            a.extend(b)
            
        
        4.2. tuple -> ordered, unchangable , allow duplciated
        
            a = (10,20,30,40)
            
            a[0]
            
            change nmishe
            a[1] = 20 --> jahae k mikhahi chn value brizi to y zarf
            in zarf mire too ye process va nmikhay --. read only 
            taghir nakon, edit natone 
            
            
        4.3. Set --> unorder (index) , unchangable , No duplicate
        
        a = {1,4,5,6}
        
        a[chizi ndre]
        
        majmooe ha ,. hazf krdne chizaye tekrari 
        
    
        4.4. Dict --> dictionary 
        
        index value
        ...   ...
        ...   ..
        
        zarf[index]
        
        
        
        key value
        ..  ..
        
        
        zarf[key]
        
        zarf[esm] 
        zarf[ghd]
        
        a = ['ali',18 , 180 , 80 ]
        
        
        a= {'name':'ali'  , 'sen':18 , 'ghad':180 , 'vazn':80}
        
        
        

        Casting -> hameye in charta beham tabdil mishan
        a=[10,20,30]
        b= tuple(a)
        
        c = list(b)
        
        d = set(c)
        
        ....
             






vaghty yek chizi mikhay zakhirash koni 
mikhay chan chizo kenare hm bexari yeja yegoshe
yeja savesh koni, mikhay beshmori , 

keep , negah dashtan , assignment ,...


--> Variables



password = '3934493498'



hameja yechizi

name_company = 'Plutus'



asami ro bekeshi biron aazash, karbar hae, pardakhtie in maho nkrdn
listi hast

Variable --> injori bekar miad 


'''









#===========================================
#===========================================
'''        Keywords        '''
#===========================================
#===========================================
'''
vaghty mizani rooye run , done done 

python az bala b paeen, chap b rast shoro mikone be khoondan

man jaee bekham in ghazie ro , bezanam zire miz

asaye in kar--> keywords  -->logic(mantegh)

'''

a=10
b=30

print('salam')




#---------------------------------------------
'''     Shoroot  (dastoorate sharti )     '''
#---------------------------------------------
#conditinal statement

'''

Ama agar, do rahi, ya mikhay dewrakhte tasmim (derakhte chantar)
vase yek seri afrad yekseri felan hayek kari ro anjam bdi




'''


#-------- 1- Just If --------------
#rahzan , fgth yek seri khat , khotote codet mikhay ejra bshe

a= 10

print('salam')

#a=10 --> salam
#a= 100 --> salam



#code khate 420 --> mortabet koni va shartish koni b a az if
#tab : 4 ta space


if a >20 :
    print('salam')


#print('salam) ejra nmishe

#agar shart True shavad

#a>20 --> shart --> True , False , b khode a


a=10

if a>20:
    print('salam')


#false --> ejra nmishe on khat


#Trye --> print('salam) -->salam

#fght baraye shorot etrue ejra mishe



'''


if Shart1 and/or shart2 :
    dastoor1
    dastooor2
    dastoor3
    ......
    



and --> dota shart hatman bayad baham dg True beshan
True True --> ejra bshe [ejra nmishe]


or --> ya --> hadeaghal yekishon
True True
True False
false True
tamame in se ta halat ejra mishe dastopor

False false --> ejra nmishe


'''


#ya maid , karbar vared kone, website mifrste, download, read

#input --> simualtor --> shabih saze 
#** CLI --> comand line interface --> python felan.py --> GUI code bzni



sen_karbar = input('senetan cheghadr hast')


#agar bala 18 bod are 

#ag paen 19 bod bge nmitoni vared


if sen_karbar <18:
    print('sene shoma ghanoni nist')
    
    
    



#-------- 2- if else --------------


#agar Shart True --> dastore 1 , ag nabood bikhial (hcihi)


#age shart True bod datsor 1 , ag nabood dastore 2 (bikhialeh nasho)

#dorahi besazi -> ya in ya oon

#if --> rahe 1 , else rahe do
sen = input('seneton chghdre?')

if sen>18:
    #shart true shdo 
    print('khoshg amadid')
    
else:
    #paeinu
    print('seneton kamtar az 8 has')
    
    
    
    
#-------- 3- if elif --------------

    #agar sharte 1 shod --> Dastore 1 , age nashod na 
    
    #shart 2 --> aga shod dastore 2 , dastore
    
    
'''


if elif else

    Shart1
      |
      |
    ---------------
  |              |
  True           False
  |              |
dastor1          Shart2
                 |
        ---------------
        |              |
        True           False
        |              |
       dastoor2        dastooor3






if elif elif else

    Shart1
      |
      |
    ---------------
  |              |
  True           False
  |              |
dastor1          Shart2
                 |
        ---------------
        |              |
        True           False
        |              |
       dastoor2        Shart3
                        |
               ---------------
               |              |
               True           False
               dastoor3       dastoor4
               
'''
    
bmi = input('bmi shoma chnade?')

if bmi>8:
    print('chagh')
elif bmi>6:
    print('motevaset')
elif bmi>4:
    print('laghar')  
else:
    print('kh laghar')


'''
range az inja t aina (in ) ,,az inja b bad in

start -------- P1  ---------P2 ----------P3 --------End
       dastoor1      dastoor2    dastoor3    dastooor4
       
       
if a > P3:
    dastoor4
elif a >P2:
    dastoor3
elif a > P1:
    dastoor2
elif a >start:
    dastoor1


'''


#---------------------------------------------
'''     Halghe ha (Loop)     '''
#---------------------------------------------

#yek tekrar repeat  (static , dynamic)  10 10 10 , 1 ,2 ,3 
#mikhahid iteration -> varede yehcizi beshid berid dakhelesh


'''

for shomarande in yekchizi:
    dastoor
    dasdtoorat..
    
    
yekchizi --> list, tupel ,.. , range()

shomarande -> az avale on chizi hast ta tahesh
har dafe dastoor ro ejra mikone



shomarande --> i , j , k , .... 


yekchizi 


dastoor

'''


for i in [1,2,3,4,5]:
    print('salam')
    
'''
i--> az 1 ta 5 dastore zir ro ejra kon 


i=1 ----> print('salam') p--> salam
i=2 ----> print('salam') p--> salam
...
i=5 ----> print('salam') p--> salam


5 ta salam



Static repeat 

3 bar ychizi 

dobar yekari anajm bshe


#telegram -->har user, file , voice, ..--> id unique

developer_id = [334473347,4344434344]

b ezaye developeram yek kare tekrari anjam beheshon masaage bede gheymat dolar


for developer in developer_id:
    
    print('salam')
    
    
developer =334473347  , salam
developer = 4344434344 , salam





repeat dynamic az lkhdpe sghoamrande

for i in [1,2,3,4,5]:
    print(i)
    
    
    
i=1 --> print(i) --> print(1)--->1
i =2 -->print(i) -->print(2)--->2

1 2 3 4 5 
    
    
    
    
    
    
    
for developer in developer_id: 
    dolar = gheymat_dolar()
    
    send_teelgram_message(developer ,dolar )
    
    
developer = 334473347   , dolar = 1703232 , send mikone b 334473347 , gheymat
developer = 4344434344 , dolar = .... , send mikone b 4344434344 , gheymat


user_id = [32323,3223,2332,323232,323223,32223,32223,32332,32223]






for i in range(0,20,)



range(start,end,step)

by default step = 1  ,start =0

range(10)

range(0,10,1)

az 0 ta 10 , 1 ki 1 ki boro .   0 , 1, 2, 3,4,5,6,7,8,9 i ro 



range(0,10,2)
0 ,2 ,4 , 6 , 8




 
'''

#----------Iteration ------------------------
#list, ... --> iterable ->chizi k mishe toosh iteration kard
#iteration--> for i in felan 

#i --> elemente oon felan

#list --> liste gheymat ha , liste user ha , liste sene user ha , liste esme uyser , ....
user_names = ['ali','vahid','hamid','reza']

for i in user_names:
    print(i)


'''
i= ali ---> print(i) -->pritn('ali') -->ali


ali , vahid , hamid , reza

'''

#iteraytin --> dakhele loop, if , sle , 

for name in user_names:
    if name[0]=='a':
        print(name)
        
'''      
name= ali , if  a == 'a' true -> print(name) -->print(ali) -->ali
name = vahid , if v=='a' False
name = hamid , if h=='a' False
name = reza , if r=='a' False


too ye list donbael ychi gashatm print
'''

#beshmorio
count = 0
for name in user_names:
    if name[0]=='a':
        #print(name)
        count = count + 1
        
        
        
#chizi print nmikonem yek zarf dri k betedade afradi k in shart True shod
#avale esmeshon a bode -> count 1 ki behesh ezafe shod --> shoamresh

a_names = []

for name in user_names:
    if name[0]=='a':
        #print(name)
        #count = count + 1
        a_names.append(name)
        
        
#print
#a_names = [ali]

#pass
#continiue (mipare mire badi)
#break -> mishkone, az halghe kharej mishe




#Mohemtrin chiz
        
#---------------------------------------------
#while b andaze for 
        

#for --> start o end dari --> b ezaye dakhele in start end (range,list) ejra mishe codet

#while --> ta zamani k in shart true hast , payanesh -> payane on sharte rnage specific (khas)


'''

for i in range(start,end,step):
    dastooor
    
    
    
i=start
while i <end:
    dastoor
    i = i+step
    
    
start nabashe , i tarif nkrde bashe
i -->shart ro true -> vared nshe
step --> kharej nashe az shrt (infinit loop) 





while True:
    
    in codd ro ejra mikone hey ejra ejra
    
    
    
    if shart:
        break



ta zamani k true --> hey az taraf ramz migiri , ta zamni k ramzesh -> dorso bashe (safe)

gheymat migiri --> gheymat ejaze nadare 1000 toman bashe, ta zamani k

    
    
'''

while True:
    price = float(input('gheymat ra vared konid:'))
    
    if price >1000:
        break



new_price = price * 0.7 

print('takhfife shoma emal shod : ',new_price)

'''
gheymat ra vared konid:200
gheymat ra vared konid:300
gheymat ra vared konid:4005
takhfife shoma emal shod :  2803.5

'''






#---------------------------------
#---------------------------------
#---------------------------------
#---------------------------------

# 1- mONOLOTHIC --> yani masan

name = input('esmet')


code_takhfif = input('code takhfifeto bde')


if code_takhfif =='JOME405':

    final_price = price * 0.8  #20%
    new_name = name.lower().strip()

    if new_name=='ali':
    
        final_price = final_price * 0.9 #10 % roye ghabli taghir midam
        
    
    print(f'moshtarie aziz {new_name} mablaghe gahbele pardakht {final_price} mibashad')




#-------man code zdm




#------Perfum hamo mifrosham
#100 ml , 50 ml, 25 ,  testeer ,...

#50 khat code

perfums= ['dior homme' , 'marly' ,'xerjof', 'amoaj','gio armani' ,'roja']

#......

perfums_prices = [150 , 230 , 290 , 240 , 70 , 340 ]


#perfum migire ...kodom gheymat kodome


#perfums_prices --> price

#grftm -> name


#price , name --> BOX --> dfinal_price emal kone takhfifo

if code_takhfif =='JOME405':

    final_price = price * 0.8  #20%
    new_name = name.lower().strip()

    if new_name=='ali':
    
        final_price = final_price * 0.9 #10 % roye ghabli taghir midam
        
    print(f'moshtarie aziz {new_name} mablaghe gahbele pardakht {final_price} mibashad')







#------Perfum hamo mifrosham
#lebas ham 

cloths = ['zara 205' , 'zara 408']
cloths_price=[]


if code_takhfif =='JOME405':

    final_price = price * 0.8  #20%
    new_name = name.lower().strip()

    if new_name=='ali':
    
        final_price = final_price * 0.9 #10 % roye ghabli taghir midam
        
    print(f'moshtarie aziz {new_name} mablaghe gahbele pardakht {final_price} mibashad')



#----------------------------
#eynak aftabi

glass = ['tebi','tebi405','tebi2343']


if code_takhfif =='JOME405':

    final_price = price * 0.8  #20%
    new_name = name.lower().strip()

    if new_name=='ali':
    
        final_price = final_price * 0.9 #10 % roye ghabli taghir midam
        
    print(f'moshtarie aziz {new_name} mablaghe gahbele pardakht {final_price} mibashad')



#-------------
#shalavr

shalavr = [',']

if code_takhfif =='JOME405':

    final_price = price * 0.8  #20%
    new_name = name.lower().strip()

    if new_name=='ali':
    
        final_price = final_price * 0.9 #10 % roye ghabli taghir midam
        
    print(f'moshtarie aziz {new_name} mablaghe gahbele pardakht {final_price} mibashad')




#ey kash baba yek box bood hamaro capsule mikrdm va fgth seda mizadam

#Monolothic --> Function capsule mikoni --> tabe estefade mikone


'''


vorodi ---> BOX ---> khrooji mide



def name(vorodi1 , vorodi2 ,vordoi3,....):
    dastorat
    chizahe 
    va vav va 
    return khoroji1 , khoroji2 , lhoroji3



'''


#price, name , code_takhfif ---> BOX [apply takhfif] ---> final price


def apply_takhfif(name,price,code_takhfif,REFERENCE_CODE):
    
    final_price = price
    
    if code_takhfif ==REFERENCE_CODE:
        final_price = final_price* 0.8
        
        new_name = name.lower().strip()
        
        if new_name =='ali':
            final_price = final_price*0.9

    return final_price
    
    

#test , debug
def debug_apply_takhfif(name,price,code_takhfif):
    return 1000







#--------perfums
perfums= ['dior homme' , 'marly' ,'xerjof', 'amoaj','gio armani' ,'roja']
perfums_prices = [150 , 230 , 290 , 240 , 70 , 340 ]
#perfum migire ...kodom gheymat kodome
#perfums_prices --> price
#grftm -> name


#price , name , code_takhfi --> BOX --> dfinal_price emal kone takhfifo

final_price = apply_takhfif(name,price,code_takhfif,'ATR405')


#... resid , ... , ... ,......




#-----lebase
cloths = ['zara 205' , 'zara 408']
cloths_price=[]

final_price = apply_takhfif(name,price,code_takhfif,'LEBAS405')

#----------------------------
#eynak aftabi

glass = ['tebi','tebi405','tebi2343']

final_price = apply_takhfif(name,price,code_takhfif,'GLASS406')


#-------------
#shalavr

shalavr = [',']

final_price = apply_takhfif(name,price,code_takhfif,'SHALVARRRRR')


#1 --> sorate develope man ajib gharib awli mishe
#2--->debugginge man awli mishe , man mikham bbinm moshkel kojas
#3 ->change , yek tabe change mikonam code takhfif





#===============================
#===============================
#===============================
#===============================


'''

django --> Tabe minevsiid



urls.py ---> /perfumes  --> perfumes_calculator() (views.py)



views.py --> por az tabe ast

/perfumes --> tabey 




perfumes_calculator()  --> kloli tabe




'''
#vorodi --> khrooji bde



from __future__ import annotations

import json
import re
import urllib.error
import urllib.request

TGJU_PROFILE_URL = "https://www.tgju.org/profile/price_dollar_rl"
TGJU_API_URL = (
    "https://api.tgju.org/v1/market/indicator/summary-table-data/price_dollar_rl"
    "?draw=1&start=0&length=1"
)

#por konid
USER_AGENT = ( ''' '''
)


def _fetch(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=15) as response:
        return response.read().decode("utf-8")


def _parse_price(value: str) -> int:
    return int(value.replace(",", "").strip())


def _scrape_from_html(html: str) -> int | None:
    patterns = [
        r'data-market-nameslug="price_dollar_rl"[^>]*data-price="([\d,]+)"',
        r'data-price="([\d,]+)"[^>]*data-market-nameslug="price_dollar_rl"',
        r'data-col="info\.last_trade\.PDrCotVal">([\d,]+)',
    ]

    for pattern in patterns:
        match = re.search(pattern, html)
        if match:
            return _parse_price(match.group(1))

    return None


def _scrape_from_api() -> int | None:
    payload = json.loads(_fetch(TGJU_API_URL))
    rows = payload.get("data") or []
    if not rows or not rows[0]:
        return None

    # First column is the closing price for the latest trading day.
    return _parse_price(rows[0][0])


def scrap_dollar() -> int | None:
    """Return the current free-market USD price in Iranian Rials, or None on failure."""
    try:
        html = _fetch(TGJU_PROFILE_URL)
        price = _scrape_from_html(html)
        if price is not None:
            return price
    except (urllib.error.URLError, TimeoutError, ValueError):
        pass

    try:
        return _scrape_from_api()
    except (urllib.error.URLError, TimeoutError, ValueError, json.JSONDecodeError, IndexError):
        return None

 
scrap_dollar() #1756000




def scrap_dollar():
    
    #mire too yek siti
    
    #scrap mikone
    
    #bot , headless, browsr ,...... (AI)
    
    #AI --> behm tabe 
    
    
    pass
    
    
    
    
    
    
def send_dollar_to_telegram(dollar,developer):
    
    #api telegram bot
    
    #date --> date
    
    text = """
    
    ------- Bename khoda -------
    
    tarikhe {} date
    
    #telegram.send_message(id ,)
    """
    
    
    

DEVELOPER_ID=[43424334,4343242332]

for developer in DEVELOPER_ID:
    
    dollar = scrap_dollar()
    
    send_dollar_to_telegram(dollar,developer )
    
    
    



#-----------------------------------------------

def tabe(a,b):
    c = a + b
    return c




d = tabe(10,20)

#a=10 ,b =20  -> c = 30 --> d =30

# a , b , c -> variable haye dakheli hazf mikone --> local variables

print(a)



#tavabe nemitonan beham dg variable haro beham pass bedan


#shoma majbor mishid -->gahan berid soraghe --> Class --> object besazid






#-----class --> sade migm --> sakhte class kamel toizh dade , estefade ash


#class ---> too delesh koli variable, va tabe hast k beham dg mortabvet hjastan

#yechize madar --> class { variable ()attributes    , tabe ha --> methods }



#objetct = Bank(......)

class Bank:
    
    
    #ch vroodi hae niaze k yek frd yek object az clas bedsaze
    def __init__(self,name,shoamre_meli,initial_balance):
        #self -->chizi hast k ejaze mide tavabe ha betonan beham pas bdn value ro 
        #va local variable nabashe , hazf nshe 
        
        
        #vorodi k az karbar grfte ro zakhirash kon tooye yek mohiti self
        #self -> toosh koli ghafase dare
        #too gahfase name , name ro briz
        
        
        self.name = name
        self.shoamre_meli = shoamre_meli
        self.balance = initial_balance
        
        
        
        
    #method ----------
    def show_balance(self):
        print(self.balance)
        
        
        
    def ATM(self,amount):
        
        self.balance = self.balance - amount
        
        print('moafagh bood')
        print(self.balance)
        
        
        
        
        
        
#Object ------> misazi


obj1 = Bank('ali','0000000000',2000)


#object k az class skahti too delesh 

#Koli attributes (variable) , koli method


#attributes -> vizhegi hash
obj1.name #ali
obj1.shoamre_meli #00000000
obj1.balance #20000



#methods -. tavabe k beyneshon hast  obj.method()  vorodi 

#hamon tabe ast , vali in tabe mokhtase in objecte

obj1.show_balance()  #2000

obj1.ATM(400)

'''
moafagh bood
1600

'''


obj1.ATM(200)

'''
moafagh bood
1400

'''



'''



Backend -------

Django ---> Function besaz




Fastapi --> fucntion bayad besazi --> layer by layer --> 

lAYER servcie --> har service --> yek class k too dleehs koli method



Filterservice()

.filter esm haro bar asase alefba

fil


service = Filterservice()



service.filter_by_name()


service.filter_by_age()





'''

class Filterservice:
    
    def __init__(self):
        pass

    def filter_by_name(self):
        pass
    def filter_by_age(self):
        pass
    def filter_by_felan1(self):
        pass
    
    def filter_by_felan1(self):
        pass
    
    def filter_by_felan1(self):
        pass
    
    def filter_by_felan1(self):
        pass
    
    def filter_by_felan1(self):
        pass
    
    def filter_by_felan1(self):
        pass
    
    def filter_by_felan1(self):
        pass
    
    
    def full_filter(self):
        
        self.filter_by_name()
        
        self.filter_by_age()

        self.filter_by_felan()
        
        
        
    #service (Object)  ---> class
    
    
    #method hash estefade mikone
    
    #yejae az filter_by_name()
    
    
    #yejae az filter_by_age()
    
    #full_fiter()
    
    
    
    
    











