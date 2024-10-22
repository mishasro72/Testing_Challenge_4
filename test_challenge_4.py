from datetime import datetime
import random 

control_number = '279146358279'
def get_date(date):
    try:
        birth_date = datetime.strptime(date, "%Y-%m-%d")
        day = (str(birth_date.day) if birth_date.day >=10 else '0' + str(birth_date.day))
        month = (str(birth_date.month) if birth_date.month >= 10 else '0' + str(birth_date.month))
        year = birth_date.year
    except ValueError:
        return 'Time data does not match format "%Y-%m-%d" Please check your data format'
    return day, month, year

def create_number(date_of_birth):
    number = ''
    try: 
        if 'foreign' in date_of_birth:
            number += str(random.randint(7 ,8))
            date_of_birth = (date_of_birth.replace('foreign', '')).strip()
            day, month, year = get_date(date_of_birth)
        elif 'non-resident' in date_of_birth:
            number += '9'
            date_of_birth = (date_of_birth.replace('non-resident', '')).strip()
            day, month, year = get_date(date_of_birth)
        else:
            day, month, year = get_date(date_of_birth)
            if year >= 1900 and year <= 1999:
                number += str(random.randint(1,2))
            elif year < 1900 and year >= 1800:
                number += str(random.randint(3, 4))
            else:
                number += str(random.randint(5, 6))
        number += (str(year))[-2:] + month + day + str(random.randint(10, 52)) + str(random.randint(100, 999))
        return number
    except ValueError:
        return 'Time data does not match format "%Y-%m-%d" Please check your date format'
        

def get_control(number, control_number):
    result = 0
    for i, y in zip(number, control_number):
        result += int(i) * int(y)
    number_new = number + str(1 if (result%11) == 10 else (result%11))    
    return number_new

date_of_birth = input('Enter your date of birth (yy-mm-dd) or foreign/non-resident and date of birth (yy-mm-dd): ')
print(get_control(number=create_number(date_of_birth), control_number=control_number))
