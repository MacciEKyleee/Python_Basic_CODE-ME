def students_data():
    with open('Students.csv') as f:
        students_data = f.readlines()
    return students_data

def clean_column_value(value):
    return value.strip()

def main():
    students_class = []
    students_name = []
    students_surname = []
    students_missing_task = []
    students_rating = []

    for line in students_data():
        splitted_line = line.split(',')
        students_class.append(clean_column_value(splitted_line[0]))
        students_name.append(clean_column_value(splitted_line[1]))
        students_surname.append(clean_column_value(splitted_line[2]))
        students_missing_task.append(clean_column_value(splitted_line[3]))
        students_rating.append(clean_column_value(splitted_line[4]))

    for element in students_missing_task:
        try:
            students_missing_task[element] == 'nieobecność'
        except ValueError:
            students_missing_task.insert(element,'0')


    message_for_students = []

    counter = len(students_rating)

    for i in range(1,counter):
        if (students_rating[i] != '5'):
            message = f"Hi {students_name[i]} {students_surname[i]},\n\nThis is a reminder that you have ({students_missing_task[i]}) tasks left to submit before you can graduate. \nYou're current grade is {students_rating[i]} and can increase to 5 if you submit all assignments before the due date.\n\n"

            print(message)

            with open('message.txt','a+') as f:
                f.write(message)
                f.write('*****************************\n\n')


        else:
            message = f"Hi {students_name[i]} {students_surname[i]},\n\nThis is a reminder that you have ({students_missing_task[i]}) tasks left to submit before you can graduate. \nYou're current grade is {students_rating[i]} - CONGRATULATIONS ! ! !.\n\n"

            print(message)

            with open('message.txt','a+') as f:
                f.write(message)
                f.write('------------------------------\n\n')

if __name__ == '__main__':
    main()
