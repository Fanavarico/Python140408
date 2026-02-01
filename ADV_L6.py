"""
Created on Sun Dec 28 17:55:33 2025

@author: Ali Pilehvar Meibody



L6


"""
#-------------------- L2 Solution-------

text = "PythonProgramming"
print(text[2:10:2]) 

print(text[2:11:2]) #toPor

#toPo

'''
eshtebahatet --->



Yad gerefti--->


'''

nums = [10, 20, 30, 40, 50, 60, 70]
print(nums[2:6:2])
#[30, 50]



'''

eshtebahat -->


yad giri --> list ham mesle str --> 
zarf beraket [shoro : end +1 : step]

: manie az ta az mide

hamishe end +1 exclude 

for i in range(0,10)
yadet bashe too range ham -->oon tahie exlude mishe



'''


mylist = [10, 20, 30, 40, 50, 60, 70]

mylist[:]

#javabe khodam -->  ......

'''

yadgrii --> ag : --> az koja : koja

az 0 : tahesh
'''

mylist[::]

#az 0 ta tahesh yeki yeki
#

mylist[::-1]

#[70, 60, 50, 40, 30, 20, 10]

'''

Yadgiri

'''

#----4

zarf = 'DataScience'

zarf[:4] # 'Data'

zarf[4:] #'Science'



#5----->


#6--->

#--7--
colors = ["red", "green", "blue", "yellow"]


colors[::-1]
#['yellow', 'blue', 'green', 'red']


#*****
reversed(colors)




#---9------



#---10-----


#11--

zarf = "abcdefghijk"

zarf[0:9:2] #'acegi'
zarf[0:10:2] #'acegi'


zarf[:9:2] #'acegi'




#--12












'''
Conclusion Natije giri

**zabano shoro konid --> englisi benevisid

-->nimsat grammar , nimsaat vocab (mortabet b computer) 
---> GPT , Gemeni ---> englisi yad bede -->5 ta grammar 


prompt --> سلام من فلانی درد و دل 




index -->
[start:end]

bydefault
[start:end+1:step(1)]




errror nadarad ...








'''


#-------L3_solutions.py




matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

zarf = matrix[1]



zarf[::-1] #[6, 5, 4]

#vasete hara hazf kon

matrix[1][::-1] #[6, 5, 4]



score = input('ey danesh amoz , nomrato begoo:')

#nomre --> adad , digit --> input() --> str

#int()
#float()


#*** aga y adade k mese ensan , chanta chanta , 
#afrade class 2.5 --> jensan --> int

#ag na , 1.23 ashari --> float




score = float(input('ey danesh amoz , nomrato begoo:'))


'''

---> score 

      |
---------------------
|    |     |   |   |
A    b     c   d   f


Daste bandi --> dorahi --> dorahi haye too dar too 

---> score 

      |
    ---shart1----
    |    |    
    A    |
       --shart2----
       B    |
        ----shart3----
        C      |
             ---shart4----
             D     F




'''


score = float(input('ey danesh amoz , nomrato begoo:'))


if score>18:
    print('A')
    

#(1) -->noe yeke if
#balaye 18 ---> A
#ag paeen --> bikhial baram mohem nist


score = float(input('ey danesh amoz , nomrato begoo:'))


if score>18:
    print('A')
else:
    print('B,XC,DE')
    
   
    
#0--->

score = float(input('ey danesh amoz , nomrato begoo:'))

#20

if score>18:
    #oni k bala 18
    print('A')
elif score>16:
    # beyne 18> va >16
    print('B')
elif score>14:
    #beyne 16 > va > 14
    print('C')
elif score>10:
    #bala 14 > va >10
    print('D')
else:
    print('F')
    

#------ > < --> >=  <=


score = float(input('ey danesh amoz , nomrato begoo:'))

#20


#ag kasi 18 bshe A hast ya B ??/
#dar ch soorati print('A') -->shart True bshe

#18>18
print(18>18) #False

if score>=18:
    #oni k bala 18
    print('A')
elif score>=16:
    # beyne 18> va >16
    print('B')
elif score>=14:
    #beyne 16 > va > 14
    print('C')
elif score>=10:
    #bala 14 > va >10
    print('D')
else:
    print('F')
    

#------ print-->donyaye vaghei
#Inpiut?
#



#---- input --> [BOX]---->khoroji

def score_calculator(score):
    if score>=18:
        #oni k bala 18
        #print('A')
        return 'A'
    elif score>=16:
        # beyne 18> va >16
        #print('B')
        return 'B'
    elif score>=14:
        #beyne 16 > va > 14
        #print('C')
        return 'C'
    elif score>=10:
        #bala 14 > va >10
        #print('D')
        return 'D'
    else:
        #print('F')
        return 'F'
    
    
def score_calculator(score):
    if score>=18:
        #oni k bala 18
        #print('A')
        return 'A +'
    elif score>=16:
        # beyne 18> va >16
        #print('B')
        return 'B +'
    elif score>=14:
        #beyne 16 > va > 14
        #print('C')
        return 'C +'
    elif score>=10:
        #bala 14 > va >10
        #print('D')
        return 'D +'
    else:
        #print('F')
        return 'F +'


score_calculator(19) #'A'

zarf = score_calculator(19)

print(zarf) #A



def score_calculator(score):
    if score>=18:
        #oni k bala 18
        #print('A')
        result= 'A'
    elif score>=16:
        # beyne 18> va >16
        #print('B')
        result=  'B'
    elif score>=14:
        #beyne 16 > va > 14
        #print('C')
        result=  'C'
    elif score>=10:
        #bala 14 > va >10
        #print('D')
        result=  'D'
    else:
        #print('F')
        result=  'F'

    return result
    




#---agah bejaye inke ono bedi +1 bad bede


def score_calculator(score):
    if score>=18:
        #oni k bala 18
        #print('A')
        result= 'A'
    elif score>=16:
        # beyne 18> va >16
        #print('B')
        result=  'B'
    elif score>=14:
        #beyne 16 > va > 14
        #print('C')
        result=  'C'
    elif score>=10:
        #bala 14 > va >10
        #print('D')
        result=  'D'
    else:
        #print('F')
        result=  'F'

    return f'{result} +'






'''

FRONTEND 

html ...









'''



#import fastapi


#@fastapi.get('/calculate/score/')
#tabe *(vorodi)


#input() -->alaki bazi-->shabih sazi
#
def score_calculator(score):
    if score>=18:
        #oni k bala 18
        #print('A')
        result= 'A'
    elif score>=16:
        # beyne 18> va >16
        #print('B')
        result=  'B'
    elif score>=14:
        #beyne 16 > va > 14
        #print('C')
        result=  'C'
    elif score>=10:
        #bala 14 > va >10
        #print('D')
        result=  'D'
    else:
        #print('F')
        result=  'F'
        
    data = {'result':result}

    return data




#-----------------------

score  = int(input('danhs amoz normat chand shode:'))
if score>=18:
    #oni k bala 18
    #print('A')
    result= 'A'
elif score>=16:
    # beyne 18> va >16
    #print('B')
    result=  'B'
elif score>=14:
    #beyne 16 > va > 14
    #print('C')
    result=  'C'
elif score>=10:
    #bala 14 > va >10
    #print('D')
    result=  'D'
else:
    #print('F')
    result=  'F'
    
print(result)





def score_calculator(score):
    if score>=18:
        #oni k bala 18
        #print('A')
        result= 'A'
    elif score>=16:
        # beyne 18> va >16
        #print('B')
        result=  'B'
    elif score>=14:
        #beyne 16 > va > 14
        #print('C')
        result=  'C'
    elif score>=10:
        #bala 14 > va >10
        #print('D')
        result=  'D'
    else:
        #print('F')
        result=  'F'
        
    print(result)
    return result
    


if score>=18:
    #oni k bala 18
    #print('A')
    result= 'A'
elif score>=16:
    # beyne 18> va >16
    #print('B')
    result=  'B'
elif score>=14:
    #beyne 16 > va > 14
    #print('C')
    result=  'C'
elif score>=10:
    #bala 14 > va >10
    #print('D')
    result=  'D'
else:
    #print('F')
    result=  'F'
    
    
    

score=9

if score>=18 :
    #oni k bala 18
    result= 'A'
if score>=16 and 18>score:
    # beyne 18> va >16
    result=  'B'
if  16>score and  score>=14:
    #beyne 16 > va > 14
    result=  'C'
if 14>score and score>=10:
    #bala 14 > va >10
    result=  'D'
if score<10:
    result=  'F'
    
    
print(result)    

#20 --> A
#17-->b
#9 -->F







w = float(input('vazneto begoo'))
h = float(input('ghadeto begoo'))
bmi = w/(h**2)

'''

  ibm
   |
-----------
>35  30  25 18.5  16 15 kamtar




'''

if bmi>35:
    print('kh chagh')
    
elif bmi>30:
    print('chagh')
    
elif bmi>25:
    print('ezafe vazn')
    
elif bmi>18.5:
    print('normal')
    
elif bmi>16:
    print('laghar')
    
elif bmi>15:
    print('kheyli lagahr')
    
else:
    print('sooe taghzie')





def bmi_calculator(h,w):
    bmi = w/(h**2)
    if bmi>35:
        print('kh chagh')
        
    elif bmi>30:
        print('chagh')
        
    elif bmi>25:
        print('ezafe vazn')
        
    elif bmi>18.5:
        print('normal')
        
    elif bmi>16:
        print('laghar')
        
    elif bmi>15:
        print('kheyli lagahr')
        
    else:
        print('sooe taghzie')

    



def bmi_calculator(h,w):
    bmi = w/(h**2)
    if bmi>35:
        result = 'kh chagh'
        
    elif bmi>30:
        result ='chagh' 
        
    elif bmi>25:
        result ='ezafe vazn'
        
    elif bmi>18.5:
        result ='normal'
        
    elif bmi>16:
        result ='laghar'
        
    elif bmi>15:
        result ='kheyli lagahr'
        
    else:
        result ='sooe taghzie'
        
    print(result)
    return result



#-------
score_list=[]
for i in range(0,10):
    score = float(input('score:'))
    score_list.append(score)
    
    

moadel = sum(score_list) / len(score_list)

print(moadel)



#-----------------------------

score_list=[]
while True:
    score = input('score:')
    
    if score =='exit':
        break
    else:
        score_list.append(float(score))
        
        
moadel = sum(score_list) / len(score_list)

print(moadel) #40.0





    
#----------

'''
yek jomle (idea) --> code


agha gharar ta abad hey trf chikar kone
hads bzne






'''

#pip install numpy
import numpy

#--->
    
import numpy
adad_computer = int(numpy.random.randint(1,7))

while True:
    adad_karbar = input('adadeto hads bezan (1,6):')
    
    if adad_karbar=='exit':
        break
    
    adad_karbar= int(adad_karbar)
    
    
    if adad_karbar==adad_computer:
        print('tabrik migam')
        break
    
    elif adad_karbar>adad_computer:
        print('kochik tar hads bzn')
        
    elif adad_karbar<adad_computer:
        print('bozorgtar hads bzn')
        

#======================


mylist = [15,50,70,1,90,20,4,108,6]


lowest_number = 200000000000000000000000000
for numb in mylist:
    if lowest_number>numb:
        lowest_number = numb
        
    
print(lowest_number)
    




mylist = [15,50,70,1,90,20,4,108,6]


larg_numb = 0
for numb in mylist:
    if larg_numb<numb:
        larg_numb = numb
        
    
print(larg_numb)
    

#--------

mylist = [15,50,70,1,90,20,4,108,6]

for i in range(0,len(mylist)):
    if i==0:
        larg_numb =mylist[i]
        
    if larg_numb<mylist[i]:
        larg_numb= mylist[i]
        
  
        
  
    
  
mylist = [15,50,70,1,90,20,4,108,6]
larg_numb = mylist[0]


for numb in mylist:
    if larg_numb>numb:
        larg_numb = numb
        
        
        
        









#bar 2 bakhs pazir has --> i%2==0 --> True -->zoj
#i%2!=0
    
for i in range(0,100):
    
    if i%2==0:
        print(i)
    
    

for i in range(0,100):
    
    if i%2!=0:
        print(i)
    


for i in range(0,100):
    
    if i%3==0:
        print(i)
    
    
#-------

reshte = input('ye kalame begoo:')

if len(reshte)%2==0:
    #zoj
    #.....
    pass

else:
    pass



def calculator(numb1,numb2,operator):
    pass
    
    #if
    #elif
    #result
    
    #return resul

#--------------
#balaye 8 ragham
#horod toosh bashe

#toosh horofe kochik bashe , ahm bzoorg
#ham character 



password = input('password:')


password= '32132131313321'
password= '32132sdds131313321'


password = input('password:')

if len(password)<9:
    print('error')
    
    
if password.isdigit():
    print('lotfan horof ham vared kon')

if password.isalpha():
    print('lotfan adsad ham vared kon')


#regex --> kh behine --> va bekhonid






password = input('password:')
point = 0

#requirement....
if len(password)>9:
    point =  point + 10


    
if not password.isdigit():
    point =  point + 10



if password.isalpha():
    point =  point + 10


#optional




if point>80:
    print('sabz sabz sabz sabz')
    
elif point>60:
    print('zard zard zard')
if point>30:
    print('good')
else:
    #requirement rad krde
    print('na avaz kon')


#====================

while True:
    meghdar = input('meghhdar:')
    
    
    if meghdar =='exit':
        break
    
    
    #if --> bebine adad dar meghdar hast ya an 
    #toosh --> for --> + + + 
    
    #if -->for kochik y abozorge ag horod kochike --> 
    lower_values=''
    upper_values=''
    for value in meghdar:
        if value.islower():
            lower_values= lower_values +value 
        
        else:
            upper_values = upper_values + value
            
            
    #if --> character --> charactera 
    
    
    
#====================
       
meghdar = input('yek meghdar bede:')


for m in meghdar:
    if not m.isdigit():
        print(m)



#------------
print('salam')
print('khobi')

print('salam',end='\n')
print('khobi',end='\n')

print('salam',end='')
print('khobi',end='')

print('salam',end='*')
print('khobi',end='*')
#salam*khobi*



meghdar = input('yek meghdar bede:')

for m in meghdar:
    if not m.isdigit():
        print(m,end='')
        
        
   
meghdar = input('yek meghdar bede:')

str_megdhars = []
for m in meghdar:
    if not m.isdigit():
        str_megdhars.append(m)
        
        
print(str_megdhars) #['a', 'b', 'c', 'd', 'e']

my_str=''
for element in str_megdhars:
    my_str = my_str + element


print(my_str)
        
#abcde
for element in str_megdhars:
    my_str = my_str + element




#----------

meghdar = input('yek meghdar bede:')

str_megdhars = []
for m in meghdar:
    if not m.isdigit():
        str_megdhars.append(m)
        
        

final = ''.join(str_megdhars)
        
print(final) #abcd



