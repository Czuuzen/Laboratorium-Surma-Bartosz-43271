import webbrowser
user = {
    'admin':'admin',
    'user1':'user1',
    'user2':'user2',
    'user3':'user3',
    'user4':'user4',
    'user5':'user5',
}
login = input('Podaj login: ')
password = input('Podaj hasło: ')

if login in user.keys() and password in user.values():
    print('Logowanie udane!')
    if login == 'admin' and password == 'admin':
        webbrowser.open('wp.pl')
    else:
        webbrowser.open('onet.pl')
else:
    print('Nie udało się zalogować')