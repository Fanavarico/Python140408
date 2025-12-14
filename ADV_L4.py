"""

In The Name of GOD

Created on Sun Dec  7 17:17:02 2025

@author: Ali Pilehvar Meibody



ADV _ L4


"""


'''

Human (En) <----interface ----> Machine(0,1)
Python--> vobacs, grammar


1-Python built in functions (nareni () )
print() input() len() type() open() ,......


2-Keywords -->
python by default --> az bala b paeen az chap b rast
khat b khat codeto mikhoni
gahan shoma mikhay in logic ro beham bzni
---> keywords --> banafsh 
if else elif while for


3-Variables --> moteghayer
esme zarf 
zarf (moteghayer , variable)

esm = meghdar (value)
3.1.Numbers ( int,float, complex) ** * / + - | == != > < =:
3.2. Bool (True,False)
3.3.String --> '' "" name[index]  name[start:end+1]
      str functions --> emali nistan , khoroji midan
      new_name=name.lower()
      3.3.1. convert --> .lower() .upper() .title() .capitalize() .replace()
      3.3.2. adad --> .find('a')  .count('a')
      3.3.3. True --> .isdigit()  .islower()  .isupper()
      
3.4. Iterables --> agha jan ma mikhaym k gahi bejaye inek
dar yek zarf--> yek value zakhire konim
chanta value zakhire konm 
3.4.1.List 
3.4.2. Tuple
3.4.3. Set
3.4.4. Dictionary








'''
#----------------------------
#python 3.8
name='alipilehvarmeibody'

n=len(name)
if n>10:
    print('bale')

if len(name)>10:
    print('bale')
    
if (n:=len(name))>10:
    print('bale')
    
if (n:=len(name))>10:
    print('bale')
#----------------------------


#----------------------------------
#------KEYWORDS-------------------
'''
conditional statement

dastoorate sharti 


'''

sen = 20

print('salam khosh omadid')

#ta abad salm khsoh omadid print mishe --> logic python interpreator

#Mikham print fght dar yek sharateri ejra bshe
#baghei sharayet run nashe


#khate 96 baste b sharti bashe b sen
#nesbsta b sen run bshe
#sen >18 run bshe , run nashe 


#logic --> keywords --> banafsh hastan

#family conditional --->
#if , else , elif 


'''
3 no darim


1- Just if --> ye if e khali estefade mikoni
shoma fek kon --> rahzan
rahzan miad fght yekseri afrad ro migire joloshono mige felan kaor konid

shart --> True shod --> code ha ejra mishe
ag False shod --> hichi barashon ejra nmishe

if shart:
    dastoor1
    dastooor2
    dastooor3
    ....
   
* shart bayad y chizi bashe dar javab True False



code mamooly 

shart(True , False)
      |
  --------------
 |True        |false
Kare 1        continiue edame bde



2--- If else
dorahi mikhahim bsazim

**dar just if --> ag true bod yekair msihdo ag nabood (bemanche) kari nmikrd

ag true bod yekari kon , ag false bod ham ykare dg kon (velesh nakon)

      shart(True , False)
           |
       --------------
      |True        |false
     Kare 1        Kare2

hatman yechizi run mishe
ch sen


if shart:
    kare1 
    karhaye 2,3,4,.....
    
else:
    kare 5,6,
    kare7,8




3-- if elif else
gahi shoma migi
agha man dorahi kardm
1- True--> kare 1
2- False --> kare 2



1- True --> kare1
2- False --> sharte jadid ---> True Kare2 / false kare 3


      shart1(True , False)
           |
       --------------
      |True        |false
     Kare 1        shart2
                    |
                --------------
                |True       |False
                kare2         kare3




#very evry advanced


      shart1(True , False)
           |
       --------------
      |True        |false
     Kare 1        shart2
                    |
                --------------
                |True       |False
                kare2       shart3(True , False)
                             |
                         --------------
                        |True        |false
                       Kare 3        shart4
                                      |
                                  --------------
                                  |True       |False
                                  kare4        kare5
                              

ddorahi haye to dar too
decision tree besazid (derakhte tasmim)


'''


sen = int(input('senetoon chande?:'))

if sen>18:
    print('salam khosh omadid')



sen =20

if sen>18:
    print('salam khosh omadid')
    a=0
    b=a+10
    print(b)
    
      

sen =10

if sen>18:
    print('salam khosh omadid')
    a=0
    b=a+10
    print(b)
    
    
'''

sen = 20

salam khosh omadid
10


sen = 10 
hichi ejra nmishe

'''

#----


sen = int(input('senet chegahdre?L:'))

if sen>18:
    print('salam')
    print('khosh omadid')
    a=sen
    b=a+10
    c=b*10
    print(c)    
else:
    print('bebakhshid')
    print('sene shoam mojaz nist')
    a=sen
    b = 18 -a
    print(f'{b} sal kam darid ta 18')
    
    
'''
sen = 20
salam
khosh omadid
300


sen = 15
bebakhshid
sene shoam mojaz nist
3 sal kam darid ta 18


'''



sen = int (input('senetoon cheghadre?:'))


if sen>18:
    print('salam khosh omadid') 
    a=sen
    b=a*10
    
elif sen>15:
    print('ye kmatar az se sal sabr kon')
else:
    print('bebakhshid shoam nmtionid vared shid')
    




#----elsi ha hast------
#Onaee k paeen az 18 hastan

if sen>15:
    print('ye kmatar az se sal sabr kon')
else:
    print('bebakhshid shoam nmtionid vared shid')
    


#---------------



'''

farsi --> python 

3 --> [1] built in function
[2] keywords
[3] variables



khodet idea (startup)
karfarma, sherkati 

--> man mikham az user ye adad bgiri , adadde dovom bgiri
taraf biad entekhab kone bad operator ro bege
jam --> adad + adad 2 --> print
......



adad bgirm??


'''


numb1 = float(input('numbere 1 ro vared konid:'))
numb2 = float(input('numbere 2 ro vared konid:'))
operator = input('operatore khod ra vared konid(jam,tafrigh,zarb,taghsim):')

# 3 ta zarf az user miad

#dar soorati k taraf nevesht jam
result = numb1 + numb2
print(result)

#dar soorati k taraf nevesht tafrigh
result = numb1 - numb2
print(result)

#dar soorati k taraf nevesh zarb
result = numb1 * numb2
print(result)

#dar soorati k tatraf nevesht taghsim
result= numb1 / numb2
print(result)



#--copy opaste stepe badi
# az bala b paeen chap b rast

numb1 = float(input('numbere 1 ro vared konid:'))
numb2 = float(input('numbere 2 ro vared konid:'))
operator = input('operatore khod ra vared konid(jam,tafrigh,zarb,taghsim):')
# 3 ta zarf az user miad
#dar soorati k taraf nevesht jam
#operator=='jam' #--. True False
if operator=='jam':
    result = numb1 + numb2
    print(result)

#dar soorati k taraf nevesht tafrigh
if operator=='tafrigh' :
    result = numb1 - numb2
    print(result)

#dar soorati k taraf nevesh zarb
if operator=='zarb':
    result = numb1 * numb2
    print(result)

#dar soorati k tatraf nevesht taghsim
if operator=='taghsim':
    result= numb1 / numb2
    print(result)



#--------




#shoma y application calculator --> karfarma --> Damet garm

#---> devops , senior --> in karet az nazare logic kari kar mikon
#optimize --> behine --> computation (mohaebat)



''''


all users ---> [istgahe 1] ---> [istgahe2] --->[istageh3]



parallel

   all users
     | jam
ejra    | tafrigh?
|    |       | zarb
|    |    |   | taghsim 
|    |   |   |     |
|    |   |   |     |




'''

umb1 = float(input('numbere 1 ro vared konid:'))
numb2 = float(input('numbere 2 ro vared konid:'))
operator = input('operatore khod ra vared konid(jam,tafrigh,zarb,taghsim):')


if operator=='jam':
    result = numb1 + numb2
    print(result)
#Inja jae k jam nis
elif operator=='tafrigh':
    result= numb1 - numb2
    print(result)
elif operator =='zarb':
    result= numb1 * numb2
    print(result)
elif operator =='taghsim':
    rsult = numb1 * numb2
    print(result)
    
#10000 --> 25000 use --> * 6 = 15 million operaton per day sood mikoni



#------------

umb1 = float(input('numbere 1 ro vared konid:'))
numb2 = float(input('numbere 2 ro vared konid:'))
operator = input('operatore khod ra vared konid(jam,tafrigh,zarb,taghsim):')

if operator.lower().strip()=='jam':
    result = numb1 + numb2
    print(result)
#Inja jae k jam nis
elif operator.lower().strip() =='tafrigh':
    result= numb1 - numb2
    print(result)
elif operator.lower().strip() =='zarb':
    result= numb1 * numb2
    print(result)
elif operator.lower().strip() =='taghsim':
    if numb2 == 0 :
        print('numb2 nemitone 0 bashe')
    else:
        rsult = numb1 * numb2
        print(result)
else:
    print('shoma bayad zarb, taghsim , tafrigh ya jam ro entekhab koni, shoma chize dg ee neveshte eed')
    


#---------------
#--------------
a='    salam    '

print('a:',a)
print('after :',a.strip())

'''
a:     salam    
after : salam

'''
    
a =' AliPilehvar'
b=a.lower()
c= b.strip()


a.lower().strip()


'''
IF , else , elif o inaro yad grftim 


---> LOOOPS ---->

halghe ha




'''


print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')


#logicxo beham bznim
#--->
'''
repeat(10):
    print('salam')



repeat(10):
    print('salam')


repeat(100):
    print('salam')


#-----
#print 1 2 3 4 5 6 7 , ... 100
repeat(100):
    print('salam')

'''

'''
a=0
repeat(100):
    print(a)
    a= a+1
'''   
    
'''
0 
1
2
3
4
5
'''

#List varedesh bshj 10 omine onsoresho print konm???
'''
a=0
repeat(100):
    mylist[a]
    a+1
    if a==10:
        mylist[a]
        print()
'''   
        




    




'''
for --> misazam

y manteghi dre ag yadesh bgiri

1-repeat
2-iteration


'''

print('salam')




print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')




#--------------------
#range --> [1,2,3,4,5,6]
for i in [1,2,3,4,5,6]:
    print('salam')
    
    
'''
shoamrande --> zarf 
zarf --> i , j , k esm , salam , ali , ghad, sen ,...
range ---> range() , list() , ....[start,..... payani]

be ezaye chiz haaee k dar in list has --> code zir ro ejra kon



python --> for bznm --> asaee niaz drm --> shomarande (i)










'''

for i in [1,2,3,4,5,6]:
    print('salam')
    
    
'''
for i in [1,2,3,4,5,6]
b ezaye i haeee dar in list hastand
i=1 i=2 i=3 i=4 i=5 i=6
b ezaye done done ina
codi k tooye body(badane) ejra kon


i=1 --> print('salam') --> salam
i=2 --> print('salam') --> salam
i=3 --> print('salam') --> salam
i=4 --> print('salam') -->salam
i=5 --> print('salam') --> salam
i=6 --> print('salam') --> salam

edame



'''



for j in [1,2,3,4,5,6,7]:
    print('by')
    

'''
b ezaye j haee k dar in list hastan done done broo code zir ro run kon

j=1 --> print('by') --> by
...
...
...
...
j=7 --> print('by') -->by

by
by
by
by
by
by
by


'''


for esm in ['ali','vahid','hamid']:
    print('salam')
    
#repeat(3):
#    print('salam')
    
'''
esm --> ali , vahid , hamid

zarf esm 

esm = 'ali' --> print('salam') -- salam
esm = 'vahid' --> print('salam') -->salam
esm = 'hamid' --> print('salam') --> salam




'''
for esm in 10:
    print('salam')
    
#iterable ? --->

'''
list , tuple, set, dictionary 
str --> iterables

iterables --> list --> chanta value 

str --> chanta character tooshe





'''
for esm in 'salam':
    print('salam')

'''
'salam' --> ['s','a','l','a','m']

esm = 's' --> print('salam') --> salam
esm = 'a' --> print('salam') --> salam
esm = 'l' --> print('salam') --> salam
esm = 'a' --> print('salam') --> salam
esm = 'm' --> print('salam') --> salam




'''


for i in [10,20,30,40]:
    print('salam')
    print('by')


'''
i=10 --> print('salam') print('by') --> salam by
i=20 --> print('salam') print('by') -->salam by
i=30 --> print('salam') print('by') --> salam by
i=40 --> print('salam') print('by') -->salam by

salam
by
salam
by
salam
by
salam
by

'''


#i ro hey taghir mdie aya man mitonm az i ham estefad
#az shomareshgaram?
#chera natooni

for i in [1,2,3,4,5,6,7]:
    print(i)

'''
i=1 ,2,3,4,5,6,7 --> code ro ejra mikone


i=1 --> print(i) --> print(1) --> 1
i=2 --> print(i) --> print(2)-->2
i=3 --> print(i) -->print(3)-->3
i=4 --> print(i) -->print(4)-->4
i=5 --> print(i) -->print(5)-->5
i=6 --> print(i) -->print(6)-->6
i=7 -->print(i) --> print(7) -->7





'''


'''


static repeat 
shomarande --> asaye paye python

for i in ['ali','vahid','hamid']:
    print('salam')
    
for i in [1,2,3]:
    print('salam')
    
for i in [100,10,585467]:
    print('salam')


dynamic repeat 
for i in [1,2,3,4,5]:
    print(i)
    
    
for 

'''



for i in ['ali','hamid','vahid']:
    print('salam')
    
'''
static repeat
i=ali --> print('salam') -->salam
i=hamid --> print(salam) -->salam
i=vahud --> print(salam) -->salam


'''
for i in ['ali','hamid','vahid']:
    print('salam' , i)
    
'''
dyamic repeat

i=ali --> print('salam' ,i) --> print('salam' , 'ali') --> salam ali
i=hamid --> print('salam' ,i)--> print('salam' ,'hamid') -->salam hamid
i=vahid --> print('salam' ,i) --> print('salam ', 'vahid') --> salam vahid

salam ali
salam hamid
salam vahid
'''



#static repeat -->
#100 bar salam


#for i in [1,2,3,4,5,6,7,8.......]
#ye tabe ee bod migod az chand ta change --> misakht

#range()

#range(start,end)

#python --> zarf[2:9] exclude
#[1 ,2,3,..........,100]

for i in range(1,101):
    print('salam')
    
    
'''
i -> [1,2,3,......100]

i=1 --> print('salam') --> salam
i=2 --> print('salam') --> salam
i=3 --> print('salam') --> salam
.... pishbini
i=100 -->print('salam') -->salam

100 ta salam



'''


#dynamic repeat

for i in range(1,101):
    print(i)
    
    
    
b=range(1,101)
print(type(b)) #<class 'range'>

'''
range(1,101) -> [1,2,3,....,100]


i=1 --> print(i)-->print(1)-->1
i=2 --> print(i)--> print(2)-->2
....
i=100 --> print(i)-->print(100)-->100

'''
    
    
#---> repeat hast hame gereftim okey?


#yekam sakht beporsma


a=0
for i in range(0,10):
    b=a+1


'''
# ignore
space ignore
a=0 zarfi a =0
b ezaye i [0,1,2,3,4,5,6,7,8,9]

code ro ejra mikone

i=0  --> b = a +1 --> b = 0 +1 --> b=1
i=1 --> b = a + 1 --> b = 0 + 1 --> b=1
i=2 --> b = a+1 --> b = 0 + 1 --> b=1
...

i=9 --> b = a +1 --> b = 0 + 1 --> b=1

#2--> aya man chiz iman 






'''


a =0 

for i in range(0,10):
    a = a + 1
    b= a + 2


print(a)
print(b)


'''
range(0,10)--->[0,1,2,3,4,5,6,7,8,9]

i = 0,1,2,3,4,--->codo ejra mikone

i=0 --> a = 0 + 1 =1 , b = 1 + 2 =3 
i=1 --> a = 1 + 1 = 2 , b = 2 + 2 = 4
i=2 --> a = 2 + 1 = 3 , b = 3 + 2 = 5
i=3 ,4,5,6,7,8,
i=9 --> a=10 , b=12
ta inja chizi print nmeihse


print(a) --->10
print(b)--> 12
'''
#----------

'''

for -->
1-repeat (static, dynamic)
2-iteration --> 

while --> for motefavet [eshtebahate mohem]


list , tuple , set , dictioanry


#---> mesale
price , code , name ... anjam bdim




'''

a =0 

for i in range(0,10):
    a = a + 1
    b= a + 2
    print(a)
    print(b)
    
    
    
'''
a=0
i --> 0,1,2,3,4.....

i=0 --> a=1 , b =3 , print(a) print(b) --> 1    3
i=1 --> a = 1 + 1 = 2 , b = 2 + 2 = 4 --> 2   4 
i=2 --> a = 2 + 1 = 3 , b = 3 + 2 = 5 --> 3  5 
i=3 ,4,5,6,7,8,
i=9 --> a=10 , b=12



1
3
2
4
3
5
4
6
5
7
6
8
7
9
8
10
9
11
10
12
'''









