"""
Created on Sun Feb  1 17:39:24 2026

@author: apm


-----L7------

"""


'''

Human (En) <------Interface ---> Machine (0,1 bianry)

Interface --->Python 


Python --->Vocab , Grammar




1- Python Built in fucntions --> Narenji
function daran , az ghabl neevshte shdod ast , reserv shdoe ast

print() input() type() len() ,.....
https://docs.python.org/3/library/functions.html



2- Python Keywords ---> Banafash
Python miad az bala b paeen, chap b rast khat b khat codetoon ro
ejra mikone
agar bekhaym taghiri bedim dar mantegh

print('salam') -->sharti


If --> dastoorate sharti
1-Just if
mese yek rahzan amal mikard

    shart
   ---------
   |True    |False
   kar1
   
   
   
2-if else -->dorahi


    shart
---------
|True    |False
kar1      Kare2



3-if elif else -->dorahi haye too dar too hastand 


    shart
---------
|True    |False
kar1     shart2
       ----------
       |True    | False
       kare2    kare3
       
       
       
#----Hlageh ha


For loop -->
for i in [1,2,3,4,5,....]:
    dastooor
    
    
i=1 -->dastoor 
...
...


for i in range(0,10):
    dastooor
    
    
    
    
while --> migoft k ta zamani k in shart true hast bayad anajm shavad


aval yadet bashe hataman varede shart beshe
yadet bashe ke az shart ham kharej beshe (sharte khoroj dashte bashe)



for i in range(0,10):
    print('salam')
    
    
i=0
while i<10:
    print('salam')
    i=i+1
    





3-Python Variables --> moteghayer -->zarf
esme zarf --> value

classification based on value type

1-Numebrs 
1.1. Int 1.2. Float 1.3. Complex

() ** * / + - 

== > < >= <= -->True False

2-Boolean

3-Str
quotation -->charcteri az keywordeton benevisid 
zarf[index]
zarf[start:end] -->slicing
str functions ---> zarf.function()
    in tavae emal nemishan , khorojhi midan
    khode zarf taghir nmikone--> joosh y zarf jadid
    new_zarf = zarf.str_function()
    3.1. Convert --> zarf.lower() zarf.upper() zarf.title()
    3.2. Adad ---> zarf.count('a')  zarf.find('a')
    3.3. True False --> is   zarf.isupper()  zarf.islower()
    

3-Iterables --> multiple value --> one variable
3.1. List ---> ordered (index) , changable, allow duplicated
zarf[index] -->element
zarf[start:end]
list functions --> emal mishan , khoroji ndaran
zarf.insert(index,element)
zarf.append(element)
zarf.clear() --> []


Tuple --> (element,elemnt) --> ordered(index) , unchangable , allow duplicated
set --> {eleemtn,e,e,} -->unordered(index) , unchangable, doesnt allow duplciated

dictionary --> {key :value}    --> zarf[index]   zarf[key] zarf[ghad]



'''


'''
ma 3 no nahveye neveshtane code ro darim

1- Monolothic (psudocode) --> az bala ta paeen , injori nvshte mishe
--> script --> gahi too sharayete khas , karborde khas estefade mishe

boti telegram --> se sale --> gheymate dollar, euro 12 zohr, shab 
ferank, bicoin, 8 ta 
sabz , ghermez
3% dota emoji sabz

exchange.py --> python exchange.py 
harrooz saate 12 ejra mishe kole cod





2- Microservcie fucntion

3- Integrated Object oriented Programming






CTO , CEO , 

CEO --> Modir amel

CTO --> Modire fani

Staff -> karmanda --> modire bakhshe , moavene , masoole , coordinator ,....


mosahebe ha ----> personality 
bnzrt collabroation -->behtr bshe abstract 

mosahebe haye fani --> CTO , mian azaton mosahebe







psudocode ---> exchange.py --> scripti hast

APP --> y app kheyli  khafan --->
dota app --> yeki az app -> Plutus --> 

panel --> Dashboard 


service dashte bashi 

k ag user khas rooye felan chiz click zad fght oon servcie ejra bshe na baghie

ye psudocode benevisim k biad ybar run bshe


microservices ---> kole servcie --> micro services

chanta servcie dar kenare ham


.py .py .py .py

main.py ---> run mikoni tamame .py function haye toosh amade hastan
k userat vghty jaee kari krdn --> guid be samte yek fucntion va functione run mishe



function --> repeat , flexibility , encapsulation


application ---> Microservice nevisi hast


website besazid --> Frontend | Backend

frontend --> Html , javascript ,.....
Backend --> Python --> ketabkhone has -->
platform --> django (kh kh kh sari karo vasat ok mikone, soratesh nesbat b )
fastapi --> kh -->sorati --> AI applciation aksaran roo in neevshte mishe


k kole karatono --> service
in service --> function benevisid



Django ---> folder
scrip --> views.py       urls.py


-------DJANGO-----------
urls.py --> /login ---> tabe seda bokhore
views.py --> oon tabe ro minevisi




-------FASTAPI--------
.py mikhay besaz 
tabe hato besaz balaye tabe hat /logic ,...

@fastapi.get('/login')
def mylogin():
    //////
    
    


'''



#========================================
#capsule --> [box]


#Input ---> BOX ---> Output
#========================================
#========================================

'''       FUNCTIONS           '''

'''

1-Definition

def name(arg,arg):
    body
    
    output
    
    

2-call  --> name(arg)



'''



#4 no tabe darim


#1-na khoroji na vorodi
def welcome():
    print('salam')
    
    
    
welcome() #salam


#Print != Khoroji

zarf = welcome()

print(zarf) #None




#2-vorodi nadare, khoroji dare

def pi():
    return 3.14


zarf = pi()

print(zarf) #3.14




#3-vorodi dare , khoroji ndre

def jam(a,b):
    print(a+b)



jam(10,20) #30


#******* --> 
#vorodi --> bOX ___> KHOROJI

#4- Vorodi dare, khoroji dare

#misazi
def jam(a,b):
    c=a+b
    return c




#in sakhtar -->skelet -->python ino hefz mikone -->Memory

#zarf --> zar fmisaze khalie mikahd chizi berize toosh

#jam --> mige in chie ? variable? tabe ast? --> memory
#mifahme ag bash emigw ahan


#check mikoen k vorodi migire ya na?
#dota ham migire

#


jam(a=4)
#TypeError: jam() missing 1 required positional argument: 'b'


jam(4,5,6,7)
#TypeError: jam() takes 2 positional arguments but 4 were given


zarf = jam(a=4 , b=5)


zarf = 9

#tafrigh(a=10,b=30) #NameError: name 'tafrigh' is not defined

print(zarf) #9

print(a) #NameError: name 'a' is not defined

print(c) #NameError: name 'c' is not defined

#***Note1 ---> tabe az input, output , body tashkil shode, fght body lozom dare

#***Note2 --> print ba khoroji fargh dare

#***Note3--> ravand yek tabe ro yad bgirid k chijori sdash mikonid chijori ejra mishe
#engar yek scripte jadid baz mishe va ejhra mishe


#***Note4 ---> variable haye daroone in tabe ha --> varibale haye LOCAL hastan na GLOBAL


a=10
b=30

def jam(a,b):
    c=a+b
    return c


#a , b --> oon adad jadide jam(a=4,b=5) -->miad mziare a=4 , b=5
#karo mikone, return k mikhore --> bejaye inke a , b o hazf 
#ag bood-->hamon adad ghabliaro sare jash mziare


#negah dashte she --> in akr anjam nmidan kh kam mishe
def jam(a,b):
    global c
    c=a+b
    return c

#c ro misaze movagaht -->chon poshtesh global (local)
#yani hazfesh nmikoje




#------
def newtonian_law(m, a):
    f = m * a
    return f

newtonian_law(m=5 , a=20) #100

#agah mishe yekar konim ag kasi a ro nadad
#yani baba manzoresh ine shetab , shetab sabete jahanie geranesh --> 9.8 (10)

newtonian_law(m=5)

#TypeError: newtonian_law() missing 1 required positional argument: 'a'


#pishfarz bezari --> default bezari

def newtonian_law(m, a=9.8):
    f = m * a
    return f


#f = 5 * 20 =100
newtonian_law(m=5 , a=20) #out[21]: 100
 

#f = 5 * 9.8 = 49
newtonian_law(m=5) #Out[22]: 49.0



#-------

def newtonian_law(m=10, a):
    f = m * a
    return f
#SyntaxError: non-default argument follows default argument


def newtonian_law(m, a=10 , s):
    f = m * a
    return f

#SyntaxError: non-default argument follows default argument



#tabe mitone chanta khoroji dashte bashe



def zarbjam(a,b):
    c = a*b
    
    d= a+b
    
    return c,d


#multiple value in one variable --> list, tuple , set ,....



zarf = zarbjam(10,20)


print(type(zarf)) #<class 'tuple'>

print(zarf) #(200, 30)

zarf[0] # 200

zarf[1] #30


#yedone zaarf = yek tabe
#zarf1 , zarf2  = tabe


res1 , res2  = zarbjam(10,20)

print(res1) #200
print(res2) #30




#---------Argument --> argument --> vorodi ha
# do no esm gozari darim

def jam(a,b):
    c = a+b
    return c


#positional arguments 
#a = 10 , b = 20

#pozitional arguments
jam(10,20) #30




#keyword arguments hastan
#keyword arguments
jam(a=10 , b=20) #30



#hata mitoni tooye tabat mamnoo koni 
#fght positional; argumenti migire, fght keyword argument

#* , other variables 
#tabe at ro --> keyword argument based
def jam(*,a,b):
    c = a+b
    return c
jam(10,20) #TypeError: jam() takes 0 positional arguments but 2 were given
jam(a=10 , b=20) #30



#other variables, /
#positional arguments
def jam(a,b,/):
    c = a +b
    return c

jam(10,20) #30
jam(a=10 , b=20) #TypeError: jam() got some positional-only arguments passed as keyword arguments: 'a, b'



#mixed konam
def complexxxxx(a,b,/,*,c,d):
    pass

complexxxxx(10,20,c=20,d=40)


#----------
#*arg
#**Kwarg



#---*arg
#* vasl koni b y zarf --> a , b, esm , esme zarf
def jam(*a):
    print(type(a))
    
    
    
    
jam(10,20,30,40,50,60,70,80,100) #<class 'tuple'>
    

def miangin(*a):
    
    print(sum(a)/len(a))
    
    
miangin(10,20,30,40,50,60)  
    
    


def miangin(*a):
    
    avali = a[0]
    
    dovomi = a[1]
    
    
#shoam miokhya m ahdodiat nazari baghei positional arguments binahayat barat befresan




#keywordi befrese chi?
#tuple --> dictionaly

#**kwarg

def jam(**b):
    
    print(type(b))
    
    print(b)
    
    
jam(ghad = 10)

'''
<class 'dict'>
{'ghad': 10}

'''



jam(ghad = 10 , vazn = 20 , sen = 40)
#b = {'ghad': 10, 'vazn': 20, 'sen': 40}
    
    
    
    
def bmi_calculator(**b):
    
    ghad = b['ghad']
    
    
    vazn = b['vazn']
    
    bmi =  ghad / vazn
    
    if bmi>30:
        return True
    else:
        return False
    
   
    
bmi_calculator(ghad = 40, vazn=200, sen=3000) #false
    
bmi_calculator(ghad = 40, sen=3000) #KeyError: 'vazn'



#-----------

def jam(a,b):
    c= a + b
    return c


jam() #no documenattion available

help(jam)
'''
Help on function jam in module __main__:

jam(a, b)

'''



def jam(a,b):
    '''
    This function is for adding two number
    a : float --> first number
    b : float --> second number
    
    output : float
    c = a + b
    c --> output
    '''
    
    c = a+b
    return c



jam()


help(jam)

'''
    This function is for adding two number
    a : float --> first number
    b : float --> second number
    
    output : float
    c = a + b
    c --> output
    
'''


def jam(a,b):
    '''
    Parameters
    ----------
    a : float
        First Number.
    b : float
        Second Number.

    Returns
    -------
    c : float
        Result of addition of both number.

    '''
    
    c = a+b
    return c


#ALL NOTES related to FUNCTIONS
#***Note1 ---> tabe az input, output , body tashkil shode, fght body lozom dare
#***Note2 --> print ba khoroji fargh dare
#***Note3--> ravand yek tabe ro yad bgirid k chijori sdash mikonid chijori ejra mishe
#engar yek scripte jadid baz mishe va ejhra mishe
#***Note4 ---> variable haye daroone in tabe ha --> varibale haye LOCAL hastan na GLOBAL
#***Note5 --> baraye default sazi shoma bayad tooye tarife tabe ooon argument ro jolosh adad tarif konid
#***Note6 --> beyne argument hatoon, aval argument haye non default badesh argument haye default
#***Note7 --> shoma mitoni chanta khoroji dashte bashi hata
#***Note8 --> shoma mitonid ba *, keyword arguemnt only , ya ba ,/ posoiitonal arguments only fucntioenton bokonid
#***Note9 --> *args --> behet yek tuple binahayt positional arguments begiri
#***Note10 --> **Kwargs --: behet ejaze mdie yek dictioanry az keyword arguments begiri
#***Note11 --> yadet bashe docstring bzari baraye fucntion hat baraye description

a=10000000
b=20000000

def jam(a,b):
    c = a + b 
    return c

#local -->mahali 


d = jam(a=10 , b=20)


print(d) #30

print(a) #NameError: name 'a' is not defined
print(b) #NameError: name 'b' is not defined
print(c) #NameError: name 'c' is not defined


'''
1-Psudocode , monolothic architecture

2- Microservice with Funcrions


3- *Integrated* Object oriented programming (OOP)



CLASS , OBJECT ----> python support az OOP


C ---> support az OOP
c++ ---> yeseri dastorat , memarish, OOP  


dar kheyli az library -->ketabkhone ha --> base aslie code nevisi has

library ha estefade mikonid --> class
application --> class sakhte mishe


AI --> Machine learning --> Neural Network --> shabakeye asabie masnooe

1940 --> 1970 , 1980 2000 2010 2020 -->80 sal riaziat 

mashin besazm-->charkh bsazi


modelo -->azash estefade koni

Multi layer percepteron --> 
from sklearn.neural_network import MLPregressor
model = MLPregressor()
model.fit(data)


class --> too delesh attributes (variable) , methods (function)

Madare -->koli tabe too deleshe

object bsazi, kole tabe az delehs bekshi bironnn



application
Bank, class , bashgah --> tabe, user , usera too yseri chiza bahm mosjhatarakan
hamashoon --> class hesab mishan  --> objecti az oon class hastan



'''

#bank --> shoma mikhay y banki bsazi 
#y frd biad toosh hesab baz kone --> 10000
#mojodish ro bebine b hamin sadegi



def initial(name , amount):

    balance = amount
    
    
def show_balance():
    print(balance)
    
    

initial(name='ali',amount=10000)

show_balance() #NameError: name 'balance' is not defined

#ATM ->azash poll kmshe
#Deposition --> pool brizam


def initial(name , amount):
    global balance
    balance = amount
    
    
def show_balance():
    global balance
    print(balance)
    

initial(name='ali',amount=10000)
show_balance() #10000




initial(name='vahid',amount=2000)
show_balance() #2000


#--------
#ali , vahid , ...--> object az yek class mitonan b ashan
#def bank(....)

#object = BANK(.....)

#class yek chizi hast k dar delesh mitoni koli tabe besazi

class BANK:
    #vaghty yeki mikhad object besaze, ch vorodi haee bayad bede
    def __init__(self,name,sen,initial_balance):
        pass
    
#self --> 

obj1 = BANK(name='ali',sen=20,initial_balance=2000)
obj1.name #AttributeError: 'BANK' object has no attribute 'name'



obj2 = BANK(name='vahi',sen=30,initial_balance=40000)



#*** classs ---> 1-attributes (varibale)  2-method (functions)


class BANK:
    #oon chizaee k usr mdie baraye skahte yek shey (object)
    #bayad berizimesh dar self
    #self -->hamon hcizie k mese databse engar zakhire mishe
    #zakhireye movagahat -->hafa ine beyne tavabe betoni in variable haro
    #transfer koni , hghabele dastres bashe
    
    def __init__(self,name,sen,initial_balance):
        self.name = name
        self.sen = sen
        self.initial_balance = initial_balance
        
    
obj1 = BANK(name='ali',sen=20,initial_balance=2000)
#yek seri variable (attribute) dare
obj1.name #Out[74]: 'ali'
obj1.sen #20





k = BANK(name='vahid',sen=30,initial_balance=40000)
k.name #Out[78]: 'vahid'




#---------
class BANK:
    
    #esmi k joloye __init__ -->chizie k namayesh dade mishe
    #b khodet harjaee k object mikhay besazi
    
    #esmi k . zade mishe rooye self -->
    #nam gozari ghafase dari mikoni

    def __init__(self,nam,sen,mojodi_avalie):
        self.name = nam
        self.age = sen
        self.initial_balance = mojodi_avalie
        



obj1 = BANK(nam = 'ali' , sen = 20 , mojodi_avalie=2000)

obj1.sen #AttributeError: 'BANK' object has no attribute 'sen'

obj1.age #20
obj1.name


obj2 = BANK(nam = 'vahid' , sen = 40 , mojodi_avalie=2000)

obj2.name





class BANK:
    def __init__(self,name,age,intial_balance):
        self.name = name
        self.age = age
        self.balance = intial_balance
        
        
        
        
        
        
#attributes -->variable

#class -->madari hast k fucntion ha dar dakhel khod darad





class BANK:
    def __init__(self,name,age,intial_balance):
        self.name = name
        self.age = age
        self.balance = intial_balance
        
    
    def welcome(self):
        print('salam khosh amadid')
        


obj1 = BANK(name = 'ali' , age = 20 , intial_balance=2000)
obj1.age #20

obj1.welcome() #salam khosh amadid


obj2 = BANK(name = 'vahid' , age = 40 , intial_balance=4000000)

obj2.welcome() #salam khosh amadid

#tavabe ro khososi sazi koni


        
class BANK:
    def __init__(self,name,age,intial_balance):
        self.name = name
        self.age = age
        self.balance = intial_balance
        
    
    def welcome(self):
        print('salam khosh amadid moshtarie aziz' , self.name)
        


obj1 = BANK(name = 'ali' , age = 20 , intial_balance=2000)

obj1.welcome() #salam khosh amadid moshtarie aziz ali


obj2 = BANK(name = 'vahid' , age = 40 , intial_balance=4000000)

obj2.welcome() #salam khosh amadid moshtarie aziz vahid




class BANK:
    def __init__(self,name,age,gender,intial_balance):
        self.name = name
        self.age = age
        self.gender = gender
        self.balance = intial_balance
        
    
    def welcome(self):
        
        if self.gender =='m':
            print('salam khosh amadid moshtarie aziz aghaye' , self.name)
        else:
            print('salam khosh amadid moshtarie aziz khanoome' , self.name)
        
        
        

obj1 = BANK(name = 'ali' , age = 20 ,gender='m', intial_balance=2000)
obj1.name #ali
obj1.gender #m
#methods
obj1.welcome() #salam khosh amadid moshtarie aziz aghaye ali


obj2 = BANK(name = 'asal' , age = 40 ,gender='f', intial_balance=4000000)

obj2.welcome() #salam khosh amadid moshtarie aziz khanoome asal







class BANK:
    def __init__(self,name,age,gender,intial_balance):
        self.name = name
        self.age = age
        self.gender = gender
        self.balance = intial_balance
        
    
    def welcome(self):
        
        if self.gender =='m':
            print('salam khosh amadid moshtarie aziz aghaye' , self.name)
        else:
            print('salam khosh amadid moshtarie aziz khanoome' , self.name)
    
    
    def show_balance(self):
        print('moshtarie aziz mojodie shoma hast:', self.balance)
        
        
        
        
obj1 = BANK(name = 'ali' , age = 20 ,gender='m', intial_balance=2000)
      
obj1.show_balance() #moshtarie aziz mojodie shoma hast: 2000

obj2 = BANK(name = 'asal' , age = 40 ,gender='f', intial_balance=4000000)
obj2.show_balance() #moshtarie aziz mojodie shoma hast: 4000000




#obj1= CLASS(arg,argu) ---> __init___

#obj1.function(argu) ---> self,....

#obj1.welcome() ---> def welcome(self)
#obj1.show_balance() ---> def show_balance(self)

#obj1.deposition(1323) --> def deposition(self,amount)
class BANK:
    def __init__(self,name,age,gender,intial_balance):
        self.name = name
        self.age = age
        self.gender = gender
        self.balance = intial_balance
        
    
    def welcome(self):
        
        if self.gender =='m':
            print('salam khosh amadid moshtarie aziz aghaye' , self.name)
        else:
            print('salam khosh amadid moshtarie aziz khanoome' , self.name)
    
    
    def show_balance(self):
        print('moshtarie aziz mojodie shoma hast:', self.balance)
        
    def deposition(self,amount):
        
        self.balance = self.balance + amount
        
        print('varize shoma ba moafaghiat anajm shod')
        print('mojodie shoma:', self.balance)
        
        
        
obj1 = BANK(name = 'ali' , age = 20 ,gender='m', intial_balance=2000)   
obj1.show_balance() #moshtarie aziz mojodie shoma hast: 2000

obj1.deposition(4000)
'''
varize shoma ba moafaghiat anajm shod
mojodie shoma: 6000

'''

obj1.show_balance()

#moshtarie aziz mojodie shoma hast: 6000



obj2 = BANK(name = 'asal' , age = 40 ,gender='f', intial_balance=4000000)
obj2.show_balance() #moshtarie aziz mojodie shoma hast: 4000000

obj2.deposition(200000)
'''
varize shoma ba moafaghiat anajm shod
mojodie shoma: 4200000

'''



obj2.show_balance()
#moshtarie aziz mojodie shoma hast: 4200000


obj1.show_balance()
#moshtarie aziz mojodie shoma hast: 6000



#obj.atm(3323) ---> def atm(self,amount)
class BANK:
    def __init__(self,name,age,gender,intial_balance):
        self.name = name
        self.age = age
        self.gender = gender
        self.balance = intial_balance
        
    
    def welcome(self):
        
        if self.gender =='m':
            print('salam khosh amadid moshtarie aziz aghaye' , self.name)
        else:
            print('salam khosh amadid moshtarie aziz khanoome' , self.name)
    
    
    def show_balance(self):
        print('moshtarie aziz mojodie shoma hast:', self.balance)
        
    def deposition(self,amount):
        
        self.balance = self.balance + amount
        
        print('varize shoma ba moafaghiat anajm shod')
        print('mojodie shoma:', self.balance)
        

    def ATM(self,amount):
        
        self.balance = self.balance - amount

        print('bardahste shoma ba moafaghiat anjam shod')
        print('mojodie shoma :', self.balance)
    
        
        
#__init__ --->tasmim migire k ch argument hae begire baraye object skahtan
#tooye self chiaro zakhire kone
obj1 = BANK(name = 'ali' , age = 20 ,gender='m', intial_balance=2000) 


#attributes --> variables
obj1.name #Out[122]: 'ali'


#methods --> functionms
obj1.welcome() #salam khosh amadid moshtarie aziz aghaye ali

obj1.show_balance() #moshtarie aziz mojodie shoma hast: 2000

obj1.deposition(4000)
'''
varize shoma ba moafaghiat anajm shod
mojodie shoma: 6000

'''


obj1.show_balance() #moshtarie aziz mojodie shoma hast: 6000


obj1.ATM(3000)
'''
bardahste shoma ba moafaghiat anjam shod
mojodie shoma : 3000

'''



obj1.show_balance()
#moshtarie aziz mojodie shoma hast: 3000






class BANK:
    def __init__(self,name,age,gender,intial_balance):
        self.name = name
        self.age = age
        self.gender = gender
        self.balance = intial_balance
        
        #---varibale khdoet besazie
        self.transactions = []
        
    
    def welcome(self):
        
        if self.gender =='m':
            print('salam khosh amadid moshtarie aziz aghaye' , self.name)
        else:
            print('salam khosh amadid moshtarie aziz khanoome' , self.name)
    
    
    def show_balance(self):
        print('moshtarie aziz mojodie shoma hast:', self.balance)
        
    def deposition(self,amount):    
        self.balance = self.balance + amount
        self.transactions.append(f'+{amount}')
        
        print('varize shoma ba moafaghiat anajm shod')
        print('mojodie shoma:', self.balance)
        

    def ATM(self,amount):
        
        self.balance = self.balance - amount
        
        self.transactions.append(f'-{amount}')

        print('bardahste shoma ba moafaghiat anjam shod')
        print('mojodie shoma :', self.balance)
    
    
    def show_transactions(self):
        
        for transact in self.transactions:
            if transact[0] == '+':
                print('Variz : ',transact[1:])
                
            else:
                print('Bardasht:', transact[1:])
            #print(transact)
            
            
        
obj1 = BANK(name = 'ali' , age = 20 ,gender='m', intial_balance=2000) 
obj1.deposition(4000)
obj1.show_balance() #moshtarie aziz mojodie shoma hast: 6000
obj1.ATM(3000)
obj1.deposition(5000)
obj1.deposition(2000)
obj1.ATM(1000)
obj1.ATM(2000)


obj1.transactions # ['+4000', '-3000', '+5000', '+2000', '-1000', '-2000']

obj1.show_transactions()
    
'''
+4000
-3000
+5000
+2000
-1000
-2000
'''

'''
Variz :  4000
Bardasht: 3000
Variz :  5000
Variz :  2000
Bardasht: 1000
Bardasht: 2000

'''


#yadet bashe b hamechiz --> PRACTICAL ---> Negahe nagahdane dashte bash

#yani donabel naghd begard
#donbale havas parti begard


obj1 = BANK(name = 'ali' , age = 20 ,gender='m', intial_balance=2000) 

obj1.ATM(3000)

'''
bardahste shoma ba moafaghiat anjam shod
mojodie shoma : -1000

'''


class BANK:
    def __init__(self,name,age,gender,intial_balance):
        self.name = name
        self.age = age
        self.gender = gender
        self.balance = intial_balance
        
        #---varibale khdoet besazie
        self.transactions = []
        
    
    def welcome(self):
        
        if self.gender =='m':
            print('salam khosh amadid moshtarie aziz aghaye' , self.name)
        else:
            print('salam khosh amadid moshtarie aziz khanoome' , self.name)
    
    
    def show_balance(self):
        print('moshtarie aziz mojodie shoma hast:', self.balance)
        
    def deposition(self,amount):
        
        self.balance = self.balance + amount
        self.transactions.append(f'+{amount}')
        
        print('varize shoma ba moafaghiat anajm shod')
        print('mojodie shoma:', self.balance)
        

    def ATM(self,amount):
        if self.balance <amount:
            print('Motasefane mojodie shoma kafi nemibashad')
        else:
            self.balance = self.balance - amount
            
            self.transactions.append(f'-{amount}')
    
            print('bardahste shoma ba moafaghiat anjam shod')
            print('mojodie shoma :', self.balance)
    
    
    def show_transactions(self):
        
        for transact in self.transactions:
            if transact[0] == '+':
                print('Variz : ',transact[1:])
                
            else:
                print('Bardasht:', transact[1:])
            #print(transact)
            
            
obj1 = BANK(name = 'ali' , age = 20 ,gender='m', intial_balance=2000) 

obj1.ATM(3000)

'''
#Motasefane mojodie shoma kafi nemibashad


'''




class BANK:
    def __init__(self,name,age,gender,intial_balance):
        self.name = name
        self.age = age
        self.gender = gender
        self.balance = intial_balance
        
        #---varibale khdoet besazie
        self.transactions = []
        
        self.show_balance_fee = 500
        #self.deposiiton_fee
        #self.ATM_fee
        
        #self.mendatory_intiial_balance
        #remaining_balance
        
        #shoamre kart besazid
        #shoamre karte daghigh
        
        #def -->
        
    
    def welcome(self):
        
        if self.gender =='m':
            print('salam khosh amadid moshtarie aziz aghaye' , self.name)
        else:
            print('salam khosh amadid moshtarie aziz khanoome' , self.name)
    
    
    def show_balance(self):
        if self.balance < self.show_balance_fee:
            print('mojodie mojodi ham nadarid')
            
        else:
            self.balance = self.balance - self.show_balance_fee
            print('moshtarie aziz mojodie shoma hast:', self.balance)
        
    def deposition(self,amount):
        
        self.balance = self.balance + amount
        self.transactions.append(f'+{amount}')
        
        print('varize shoma ba moafaghiat anajm shod')
        print('mojodie shoma:', self.balance)
        

    def ATM(self,amount):
        
        #if amount> self.max:
            
        if self.balance <amount:
            print('Motasefane mojodie shoma kafi nemibashad')
        else:
            self.balance = self.balance - amount
            
            self.transactions.append(f'-{amount}')
    
            print('bardahste shoma ba moafaghiat anjam shod')
            print('mojodie shoma :', self.balance)
    
    
    def show_transactions(self):
        
        for transact in self.transactions:
            if transact[0] == '+':
                print('Variz : ',transact[1:])
                
            else:
                print('Bardasht:', transact[1:])
            #print(transact)
           
            
'''
#self.deposiiton_fee
#self.ATM_fee
#self.maximum_ATM
#self.mendatory_intiial_balance
#remaining_balance

#shoamre kart besazid
#shoamre karte daghigh

#def -->

az y shoakmr ekart b y shoamre karter dg pool bzn

--> hade aksar



'''    


   
            