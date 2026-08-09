#az hamon file dataabse  , Base
from database import Base 


#dar har jadval, column 
#too column (type )
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship



'''
yadavari

----esme_jadval----
soton1  | soton2 | soton3 |




class esm(Base):
    __tablename__ = ''
    esme_jadval = Column(type , ) null, foreignkey , relation
    ....
    ...
    
    
    
'''



class User(Base):
    __tablename__ = 'users' #esmesh 
    
    '''
    id    name    email  ... 
    

    '''
    id = Column(Integer, primary_key=True, index=True)
    #--soton haye bade
    name = Column(String, nullable=False) #null khali bashe
    email = Column(String , nullable=False)
    
    
    
    


'''
Questions --> table esh ro besazim
'''
class Questions(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)

    choice = relationship('Choice', back_populates='question')
    #answer = relationship('answers', back_populates='questions')





class Choice(Base):
    __tablename__  ='choice'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    is_correct = Column(Boolean, nullable=False)
    question_id = Column(Integer, ForeignKey('questions.id'))
    question = relationship('Questions', back_populates='choice')
    #answer = relationship('answers', back_populates='choice')



'''
class answers(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    question_id = Column(Integer, ForeignKey('questions.id'))
    choice_id = Column(Integer, ForeignKey('choice.id'))

    user = relationship('User', back_populates='answer')
    question = relationship('Questions', back_populates='answer')
    choice = relationship('Choice', back_populates='answer')

'''




