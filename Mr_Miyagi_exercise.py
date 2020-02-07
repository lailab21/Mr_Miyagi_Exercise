while True:
    User_response = input('Say something  ').capitalize()
    if '?' in User_response:
        print('questions are wise, but for now.Wax on, Wax off!')
    elif 'sensie' not in User_response:
        print('You are smart, but not wise - address me as Sensie please')
    elif 'block' in User_response or 'blocking' in User_response:
        print('Remember, best block, not be there..')
    elif 'Sensie i am at peace' in User_response:
        print('Sometimes, what heart knows, head forgets')
        break
    else:
        print('do not lose focus.Wax on, wax off.')