filename='mail_list.txt'

# def email_list():
#     with open(filename) as fopen:
#         email = fopen.readlines()
#     return email

def search(my_email, email_list):
    for email in email_list:
        if email == my_email:
            return True

    return False

def main():
   # users_emails = email_list()
    users_emails = ['nouquomayanno-9094@yopmail.com','crejayolletoi-1857@yopmail.com','rekoukuttappa-2741@yopmail.com','nossorafitre-1734@yopmail.com','beilleyemappe-8692@yopmail.com','kyle@interia.eu']
    wanted_email = 'kyle@interia.eu'

    result = search(wanted_email,users_emails)
    print('Email on list:',result)

if __name__ == '__main__':
    main()


# mail = 'kyle@interia.eu'
#
# if mail in get_quotes():
#     print('Tutaj jest ten e-mail!')
# else:
#     print('Tutaj nie ma tego e-mail :( ')
