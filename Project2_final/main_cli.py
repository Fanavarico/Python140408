#ooni k mikhad estefade kone
from database import Base , engine, get_db
from crud import create_user, create_question, add_choice, list_questions
from models import User, Questions, Choice

db = get_db()



print('=======================================')
print('=======================================')
print('=======================================')
print('=======================================')
print('==============Mini Quiz demo================')

print('first you must insert your name')

name = input('enter your name: ')

email = input('enter your email:')


usr1 = create_user(db, name = name , email = email)

questions = list_questions(db)

user1_answers_scores=[]




'''
Bayad in tabe haro dar CRUD benevisijm 

inja fgth seda konim


'''


for q in questions:
    print(f'{q.id} - {q.text}')

    #q.choice
    choices =[]
    choice_true=0
    
    for c in q.choice:
        print(f'{c.id} - {c.text}')
        choices.append(c.id)
        
        if c.is_correct==True:
            choice_true = c.id
        

    #answer = input('entery your answer:')
    answer= int(input('enter your answer (id):'))
    
    while True:
        if answer in choices:
            
            if answer == choice_true:
                user1_answers_scores.append(5)
                
            else:
                user1_answers_scores.append(0)

            break
        
        
        print('Your id is not in questions')
        answer= input('enter your answer (id):')
    
    
        
    

SCORE = sum(user1_answers_scores)/25 * 100 



print('Your score is :',SCORE , 'out of 100')


