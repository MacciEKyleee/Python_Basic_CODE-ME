def students_data():
    # Function that retrieves data from a .csv file (data downloaded from excel)
    with open('Students.csv') as f:
        students_data = f.readlines()
    return students_data

def clean_column_value(value):
    # Function that clears whitespace for us
    return value.strip()

def save_txt(value):
    # Function that will save finished messages to the message.txt file
    with open('message.txt', 'a+') as f:
        f.write(value)
        f.write('*****************************\n\n')


def main():
    # we create lists with in turn: class, surnames and first names of students, grades which they do not have and the average of the obtained grades.

    students_class = []
    students_name = []
    students_surname = []
    students_missing_task = []
    students_rating = []

    for line in students_data():
        # We fill the created lists with data taken from the .csv file

        splitted_line = line.split(',')
        students_class.append(clean_column_value(splitted_line[0]))
        students_name.append(clean_column_value(splitted_line[1]))
        students_surname.append(clean_column_value(splitted_line[2]))
        students_missing_task.append(clean_column_value(splitted_line[3]))
        students_rating.append(clean_column_value(splitted_line[4]))

    message_for_students = []

    counter = len(students_rating)

    # We must offer students the opportunity to improve their grades if they return any missing papers
    # Students who have submitted all their work receive the highest grade - they do not have to correct / report anything anymore
    for i in range(1,counter):

        # if the student was absent, it will display an error
        # if he reports an error - the e-mail with the grade will not be sent to the student
        # we will create a file called 'blacklist' where students with absences will be collected
        try:
            if not students_rating[i].isdigit():
                raise ValueError('Incorrect rating')
        except:
            with open('blacklist.txt', 'a+') as f:
                f.write(f'{students_name[i]} {students_surname[i]} --> Nieobecność na zajęciach. \nProsimy zgłosić się do wykładowcy.\n')
                f.write('\n')

        if (students_rating[i] != '5'):

            message = f"Hi {students_name[i]} {students_surname[i]},\n\nThis is a reminder that you have ({students_missing_task[i]}) tasks left to submit before you can graduate. \nYou're current grade is {students_rating[i]} and can increase to 5 if you submit all assignments before the due date.\n\n"

            save_txt(message)

        else:
            message = f"Hi {students_name[i]} {students_surname[i]},\n\nThis is a reminder that you have ({students_missing_task[i]}) tasks left to submit before you can graduate. \nYou're current grade is {students_rating[i]} - CONGRATULATIONS ! ! !.\n\n"

            save_txt(message)

if __name__ == '__main__':
    main()
