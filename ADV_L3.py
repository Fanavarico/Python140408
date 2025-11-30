
"""
Created on Sun Nov 30 17:34:45 2025

@author: apm




ADV_L3


"""




'''


Human (en) ---- python ----- Machine (binary 0,1)


python --> language -> vocab , grammar

1-Python built in functions (nareni) 
print() len() type() input() ,..........



2-Keywords ---> if else,  LOgical (mantegh)
If , elif , else
for , while
def 
class



3- Variables (moteghayer) zarf
ghavanin --> nam gozarishon
nam = value (meghdar)
3.1.Number 
    3.1.1 Int 0 1 2 3 -1 -4
    3.1.2. float  1.32837 1232.23232
    3.1.3. Complex 1j 4 + 2j
    operation : = ** * / + - 
    comparison : == != > < >= <= 
3.2. Boolean (True , False)
3.3. Str (string , reshte) --> word , kalame ,...
     esme zarf = 'value'
     assign --> a='ali'
     access --> esme_zarf[index]  index 0
     slice --> esme_zarf[start:end+1] a[2:8] 
     methods --> esme_zarf.function()
     a.lower() a.upper() a.title() a.strip() 
     
     rooye a taghir nmidadan -> khrooji mdiadan
     
     b = a.lower()


3.4. Iterables 
List --> []
Tuple -->
Set -->
dictionary --> 


'''


#------- Infrustructure (zirsakht)
#---> zirsakhte kh az sait az hamin logic (mantegh
#estefade mishe --> amazon, digikala , ....

'''

Server --> (servere abri)



device electronic --> goshi, computer ,....
-- > IP -> adade khase unique [shenasname]

computer khodam b ye computer 
dota ocmputer bham vasl konim
computer1 --> 199.80.145.10
computer2 --> 200.10.16.25

computer2 --> Host (mizban)

200.10.16.25 --->behesh vasl besham??

internet


goshi khdoet b agoshei kenari --> blutooth , airdrop 
madoon ghermez 
 
internet estefade beshe beyne dot adevice


maghaze 3 ,4 ta computer beham vaslbashan -->
4 ta markazi (laptab central) --> 100.10.80.90
--> vasl mishan

#---------

neuchatel --> Computer jolome --> 199.10.20.70 
man migam 

fard --> shoma -->yek codi ro run konam ama 
roye laptabe khdoet na rooye laptabe man
man behet ejare midam 
ye mah ejare midamesh .
virtual --> 199.10.20.70 --> be laptabe man vasl sho
barname --> laptabe man estefade mikoni 
laptabe, 100 t alpatab --->
eshterak bdm , gharz bdm b baghie 24 --> server dare

norway , alman --> server 
computers onja hastan , gahrs midan


computer --> ram , GPU , hard ,.. --> assemble 
ghafas ehats --> ram ram 

ram 16 .
server ram 1 ,2  

ghavi bood --> 64 , GPU NVIDIA --> Supercomputer , abar rayane

iran --> server dakheli 
sherkat --> ram o ... yekodom ejare koni
supercomputer --> abarrayne --> simorgh amirkabir 





--> shoro konam karamo --> website , hame brn toosh vared beshan
sabte nam konan (esm, paswordo zakhire konm)
tabel [mahsoolat] befrosham

entekhab kona user va bekharan

kahrideshon , karashon hame computer --> server

code run? --> serer


server mikahram --> dakheli , 
1 sal ejare mikonm ---> ip = 198.76.54.31

APP ---> ip , password mitoni baz koni laptabaro tooye laptabe

terminus [app] , .......

server --> widnows --> [Windows 7 , 10 , 11  | MacOS | Linux ]


GUI --> graphcial user interface rabete graphici karbar
terminal , coomand -> dastoor 

--> ls
main
op
usr
svr

---> cd main
(main)---> 

GUI 


server --> 2 G ram, 50 Gb hard , 2 core cpu ,.. windows linux 
198.76.54.31 , password

--> [terminus ,...] --> vasl msiham b oon computer
windows--> safe widnows
linuxi --> terminal siah (rooye oon ram , rooye on hard)
ejra konm --> roo on computer

domain --> damane mikahram --> GoDaddy ,...
plutus.com  -->commercial
plutus.org --> organziation 
plutus.ir --> iran
plutus.eu --> europ
plutus.ch --> 
plutus.it -->

plutus.ai --> ai --> angular 

DOMAIN -->

afrad browser --> bian 198.76.54.31

plutus.org  --> 198.76.54.31
browser plutus.org --> 198.76.54.31 ---> oon serveret


python --> run vas ehamishe
roosh --> html , css , javascript run mikoni
-->198.76.54.31 --> 
koja run bashe /home


plutus.org/home --> barname e k roo rune




Python harmogeh code minevisam too zehname baghie daran
az function haye man estefade mikonan
man khodm nisam fght -->baghie estefade kone




 Server side  <-----> User side
 
 
 user side ---_> [admin ] [developer] 
 
 plutus.org/admin 
 plutus.org/home --> customer



divar , digikala -->

--> foroshande
--->kharidaran

emrooz ye codi benevis ---> foroshande ha azash estefade mikonan
divar, amazon digikala ,.......


yekseri mahsol drn mikhan gheymato code name mahsoolesho ro sabt konan

 
 
'''

#-----mesal------

print('salam khosh amadid be fanavari shop....')

name = input('name mahsooleton ro bgoo:')
print(name) #nvidia







#----
'''
#fastapi , django ,......
#Front data --> API --> 
@fastapi.get('name,code,price')
def getting_information(name,code,price):
    new_name = name.lower()
    new_code = float(code)
    new_price = price*10 + 400
    
    text = 'daryaft shod'
    return text





-----fanavari shop--------\
name mahsool : Nvidia
Code mahsool : C1000
    Total price : 23000
    
aya etellaate bala ro taeed mikonid?


'''
print('salam khosh amadid be fanavari shop....')

name = input('name mahsooleton ro bgoo:')
code = input('code mahsooleton ro begoo:')
price = input('gheymate mahsooleton ro begoo:')

#chan khat chizi bnvisi '  --> '''

text = f''' ------  Fanavari Shop -----
Name mahsool : {name}
code mahsool : {code}
total price = {price}

aya etelaate balaro taeed mikonI?
'''

print(text)

#esme zarf print bshe, value zarf print bshe


#f string 

'''
 ------  Fanavari Shop -----
Name mahsool : Nvidia
code mahsool : n100
total price = 10000

aya etelaate balaro taeed mikonI?

'''



#---->

a=30

print('ali a saleshe')
#ali a saleshe

print('ali', a , 'saleshe') #ali 30 saleshe


#hamashoot oto y qutation

print('ali a saleshe')


'30li 30 s30leshe'

#yeja bfhme a --> harfe a e
#yeja bgm na baba variable a



# f {}
a=30

print(f'ali a saleshe')
#ali a saleshe

print(f'ali {a} saleshe')
#ali 30 saleshe
#f --> tooye in khat ychizaee az biron bairam
#kodom? --> {}


ghad=180

print('ghad e ali ghad hast')
#ghad e ali ghad hast

print(f'ghad e ali ghad hast')
#ghad e ali ghad hast

print(f'ghad e ali {ghad} hast')
#ghad e ali 180 hast





name = input('name mahsooleton ro bgoo:')
code = input('code mahsooleton ro begoo:')
price = input('gheymate mahsooleton ro begoo:')

text = f'''

++++++++ Plutus SHOP +++++++++++

+++ Name mahsool : {name}

+++ Code Mahsool : {code}
    
    Gheymate Kol : {price}
        
ba tashakaro
Pluts .co 2026
'''

print(text)

#print('f sdjhsdkjdshs a {{{]}}} 38732823')

#return Text --> front migiratesh b user namayesh



#------KEYWORDS----------------

#----> IF , if else , if elif --> chie ??


#----> mesale taeede tarakonesh , sabt

#---> moshkelate moheme digikala --> str functions() --> ahamiate onaro bdoni




#---> yekshanbe
#halghe ha beshim for , while --> yek manzare, didgahe dg yad bgirim

#hamino takmil konim
'''
ye ghesmat ya kole code ro run --> compiler
shoro mikone translate --> low level codes --> Binary
rooye hasteye engine kernele machine ejra mishe



Python --> mese ensan
az bala b paeen
az chap b rast
khat b khat

LOGIC ---> MANTEGH



in mantegh ro beham bznid --> 2.Kyeowrds 

if else elif ---> conditional statement --> sharti

'''





sen = input('senetoon cheghadre? :')

print('salam khosh oomadid')


#--> sen = 30 --> salam
#--> sen = 10 --> salam
#-->sen = 3228327193276 --> salam
#sen --> ali --> salam
#sen = djaksghd783qyadhw --> salam


#fght baraye afradi k seneshon
#balatar az 20 hast
#Khate 439 run bshe baraye ona





sen = input('senetoon cheghadre? :')



#if shart:
#    print('salam khosh oomadid')

#if shart 
#oon codi k mikhay sharti bshe
#y tag --> 4 ta space bere jolo


#shart --> yechizi bashe k javabesh
#Motagher --> True , False

#True --> code run mish
#False --> run nmishe

'''
tRUE FASLE?


a>10 
a==10
==
!=
>
<


.isdigit()
.is
.is --> True False



khate code morede nazaret


balash if 
khodesh 4 ta space [y tab] bre jolo
shart --> True False





'''

#in rabti b sharto if ndre ye nokte kolie
#input --> str 30 --> '30' 
#30 --> '30'


sen = input('salam sene shoma cheghadre')

sen / 8730

#TypeError: unsupported operand type(s) for /: 'str' and 'int'


sen =input('salam sene shoma cheghadre')

new_sen = int(sen)
new_sen = float(sen)


#------->


sen = int(input('salam sene shoma cheghadre'))

#sen > 18 --> True false --> Nesbat b sen



if sen > 18:
    print('salam khosh oomadid')



'''
nokteye nahaee
hamechi rajebe print nist
harchisi


'''
a=10

if sen>18:
    b=a+30
    

'''

yek khat az code ro sharti mikonm 


yek khat?? ---> body --> har chand kaht k bkham

'''



sen = int(input('salam sene shoma cheghadre'))



if sen>18 :
    print('salam')
    b=10
    c=20
    a= b+c
    print('khosh amadid')



#moshkel

'''

Khanevadeye shartoi


1- Just if --> faghat if --> rahzane
shart --> fght Ag true shod anjam mide
true nashdo ? --> beman che bere 




2- If else 




3- if elif elif .... else 







'''
    


sen = 5



if sen>10:
    print('salam')
    



print('khodafez')


'''
khodagfez chap mishe
'''

#------------------

sen = 20

print ( sen >10 ) #True



if sen>10:
    print('salam')
    





sen = 5

print ( sen >10 ) #False



if sen>10:
    print('salam')
    


'''

1-Just IF , Only If

oonaee bala 10 --> Salam
onaae k paeen 10 --> beman che !!???

rahzana --> ye seri afrado mikeshe kena
rbaghie ro kari ndre



'''




'''

dorahi baz konm

shart --> True --> kare 1
false --> kare 2


shart sen >10 


sen >10 [True] ---> salam
sen < 10 [False] --> bbkhshid



just if
 shart 
      |
   --------
  |
True     
 |
Kar     






2- if else


      shart 
        |
     --------
    |       |
  True     False
   |        |
  Kar1     Kar2



if shart: 
    kare 1
else:
    kare2





'''


sen = 20


if sen>10:
    print('salam')
else: 
    print('bebakhshid nemishe')

#salam



    
sen = 5


if sen>10:
    print('salam')
    print('')
    print()
    c=b+10
else: 
    print('bebakhshid nemishe')

#bebakhshid nemishe


'''

family 

 3-  if elif 
 
 dorahi dar do rahi besazam
 
 ag bala 30 --> yekar
 age paeentari --> ag ghade felan -->
 
 
         shart 
            |
     --------------
    |            |
  True         False
   |            |
  Kar1        SHart
               |
            --------
           |       |
           True    False
           kar2    kar 3
              





'''

if sen>30:
    print('salam')
elif sen >10:
    print('salam')
else:
    print('khodafez')
    




'''


balaye 30 paeene 30

balaye 30 ---->  salam


'''



#---------------------



name = input('name mahsooleton ro bgoo:')
code = input('code mahsooleton ro begoo:')
price = input('gheymate mahsooleton ro begoo:')

text = f'''

++++++++ Plutus SHOP +++++++++++

+++ Name mahsool : {name}

+++ Code Mahsool : {code}
    
    Gheymate Kol : {price}
        
ba tashakaro
Pluts .co 2026
'''

print(text)


answer = input('aya etelaate balaro taeed mikonid?:')

#answer=='yes' --> True , False

if answer=='yes':
    print('salam tabrik migam sabt shod')



#yes --> salam tabrik
#no --> hich
#kdsjygadsjyg -->


'''
se ta family if

shart darim True False

1- just if 
--> rahzane --> fgth baraye yeseria ye kar mikone

shart True bodo -- > Kar1



2- if else
---> dorahie --> 
SharT True --> kare1
shart False --> kar2


3- elif
dorahi haye to dar tooe
shart True shod kare 1
shart false --> shart --> Kare 2 , kare 3


'''





'''
if only
if shart :
    kar 1 


if else

if shart:
    kar1
else:
    kar2


'''


answer = input('aya etelaate balaro taeed mikonid?:')


if answer=='yes':
    print('sabt shod tabrik')
    
else:
    print('sabt nashod ozrkhahi mikonam')


'''
yes ---> sabt shod tabrik
no --> sabt nashod ozrkhahi mikonam
bale -->  sabt nashod ozrkhahi mikonm
'''







'''
        answer == yes
             |
     ---------------
    |              |
    true           false
    |              answer==no
 tabrik              |
                |             |
         ok laghv shod        bbkshid ba yes no javab bde




'''
answer = input('aya etelaate balaro taeed mikonid?:')

if answer=='yes':
    print('sabt shod tabrik') 
elif answer=='no' :
    print('bale laghv shod')
else:
    print('lotfan ba yes va no javabamo bde ')


#yes --> sabt shod tabrik
#no --> bale laghv shod
#jshasdh --> lotfan ba yes va no javabamo bde 



'''
product o .......
if o elif ......

run konid


--> yes    --> javab bad behet mide 
--> Yes

--> No 


handle mishe

ta hafteye dg



if , ---> moror konim
Yes , yes space

while for .......



'''







