# seed.py --> jaee k shoma question haro tarahi mikonid

from database import Base, engine, get_db

# tabe shoma tooye crud minevisi inja import mishe
from crud import create_user, create_question, add_choice, list_questions


print('Tables created successfully')

# database shoma tooye yek zarfe
db = get_db()


print('Creating questions...')


# Question 1
q1 = create_question(
    db,
    text='Which component is known as the brain of the computer?'
)

add_choice(db, q1, text='CPU', is_correct=True)
add_choice(db, q1, text='RAM', is_correct=False)
add_choice(db, q1, text='SSD', is_correct=False)
add_choice(db, q1, text='Power Supply', is_correct=False)


# Question 2
q2 = create_question(
    db,
    text='Which hardware component temporarily stores data while programs are running?'
)

add_choice(db, q2, text='Hard Disk', is_correct=False)
add_choice(db, q2, text='RAM', is_correct=True)
add_choice(db, q2, text='GPU', is_correct=False)
add_choice(db, q2, text='Motherboard', is_correct=False)


# Question 3
q3 = create_question(
    db,
    text='Which component is mainly responsible for processing graphics?'
)

add_choice(db, q3, text='CPU', is_correct=False)
add_choice(db, q3, text='RAM', is_correct=False)
add_choice(db, q3, text='GPU', is_correct=True)
add_choice(db, q3, text='SSD', is_correct=False)


# Question 4
q4 = create_question(
    db,
    text='Which storage device is generally faster than a traditional HDD?'
)

add_choice(db, q4, text='SSD', is_correct=True)
add_choice(db, q4, text='DVD', is_correct=False)
add_choice(db, q4, text='Floppy Disk', is_correct=False)
add_choice(db, q4, text='CD-ROM', is_correct=False)


# Question 5
q5 = create_question(
    db,
    text='What is the main function of the motherboard?'
)

add_choice(
    db,
    q5,
    text='To connect and allow communication between computer components',
    is_correct=True
)
add_choice(
    db,
    q5,
    text='To permanently store all user files',
    is_correct=False
)
add_choice(
    db,
    q5,
    text='To display images on the monitor',
    is_correct=False
)
add_choice(
    db,
    q5,
    text='To provide internet access',
    is_correct=False
)


# python seed.py
print('Questions created successfully')
print('finalizing...')
