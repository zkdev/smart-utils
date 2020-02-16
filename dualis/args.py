args = {
    "username": None,
    "password": None
}


def read(argv):
    global args
    for i in range(len(argv)):
        if argv[i] == '--username' or argv[i] == '-u':
            args['username'] = argv[i + 1]
        elif argv[i] == '--password' or argv[i] == '-p':
            args['password'] = argv[i + 1]
