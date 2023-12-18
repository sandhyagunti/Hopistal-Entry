# New project, multispecility hospital.
# Takes the details from the patient and incharges the available doctor with the respective day and problem
# Built using basic programming and later it will be developed on the completition of the project
import datetime

print("         WELCOME TO THE MULTISPECIALITY HOSPITAL     ")
date = datetime.datetime.now()
print(f'Date: {date}')
name = input("Name : ")
age = int(input("Age : "))
gender = input("Gender : ")
while gender.lower() !='male' or 'female':
    break
mobile_number: int(input("Mobile Number : "))
place = input("Place : ")    
#H
choice = input('''
                1. Fever
                2. Cough
                3. Cold
                4. Stomach Pain
                5. Nothing

Enter your problem: ''')
another_problem = input("Is any other problem?: ")
def message():
    print(f'Dear {name.upper()} is suffering with {choice.upper()} {another_problem.upper()}.')

def male_doctors():
     print('''
                The available doctors are:
                    1. Ramchand
                    2. Ram Krishna 
            ''')
     doctor_name = input("Enter the doctor name: ")
     print(f'Dear {name.upper()} is appointed with doctor {doctor_name.upper()} for {choice.upper()} {another_problem.upper()} consultation. ')
def female_doctors():
     print('''
                The available doctors are:
                    1. Sharadha
                    2. Kavya
            ''')
     doctor_name = input("Enter the doctor name: ")
     print(f'Dear {name.upper()} is appointed with doctor {doctor_name.upper()} for {choice.upper()} {another_problem.upper()} consultation. ')

def fever():
    message()  
    if gender.lower() == 'male':
        male_doctors()
            
    elif gender.lower() == 'female':
        female_doctors()
    else:
        print("You have entered incorrect gender.")
def cough():
    message()
    if gender.lower() == 'male':
        male_doctors()
    elif gender.lower() == 'female':
        female_doctors()
    else:
        print("You have entered incorrect gender.")
def cold():
    message()
    if gender.lower() == 'male':
        male_doctors()
    elif gender.lower() == 'female':
        female_doctors()
    else:
        print("You have entered incorrect gender.")
def stomach_pain():
    message()
    if gender.lower() == 'male':
        male_doctors()
    elif gender.lower() == 'female':
        female_doctors()
    else:
        print("You have entered incorrect gender.")
def another():
    pass
def problem():
    if choice.lower() == 'fever':
        fever()
        if another_problem.lower() == 'cold':
            #print(f'Dear {name.upper()} is also having {another_problem.upper()}')
            pass
        elif another_problem.lower() == 'cough':
            #print(f'Dear {name.upper} is also having {another_problem.upper()}')
            pass
        elif another_problem.lower() == 'stomach_pain':
            #print(f'Dear {name.upper()} is also having {another_problem.upper()}')
            pass
        else:
            pass
    elif choice.lower() == 'cough':
        cough()
        if another_problem.lower() == 'fever':
            #print(f'Dear {name.upper()} is also having {another_problem.upper()}')
            pass
        elif another_problem.lower() == 'cold':
            #print(f'Dear {name.upper} is also having {another_problem.upper()}')
            pass
        elif another_problem.lower() == 'stomach_pain':
            #print(f'Dear {name.upper()} is also having {another_problem.upper()}')
            pass
        else:
            pass
    elif choice.lower() == 'cold':
        cold()
        if another_problem.lower() == 'fever':
            #print(f'Dear {name.upper()} is also having {another_problem.upper()}')
            pass
        elif another_problem.lower() == 'cough':
           # print(f'Dear {name.upper} is also having {another_problem.upper()}')
           pass
        elif another_problem.lower() == 'stomach_pain':
            #print(f'Dear {name.upper()} is also having {another_problem.upper()}')
            pass
        else:
            pass
    if choice.lower() == 'stomach_pain':
        stomach_pain()
        if another_problem.lower() == 'fever':
            #print(f'Dear {name.upper()} is also having {another_problem.upper()}')
            pass
        elif another_problem.lower() == 'cold':
            #print(f'Dear {name.upper} is also having {another_problem.upper()}')
            pass
        elif another_problem.lower() == 'cough':
            #print(f'Dear {name.upper()} is also having {another_problem.upper()}')
            pass
        else:
            pass
problem()
