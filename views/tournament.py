def new_tournament_form():
    print('Enter a tournament name:')
    name = str(input())

    return {
        'name': name
    }
