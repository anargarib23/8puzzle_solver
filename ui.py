def displayTable(state):
    """
    Displays/prints the state, i.e., the 2D array that holds the arrangement of numbers on the console in a neat way.
    :param state: state to be displayed
    """

    print(' _____ _____ _____')
    print('|     |     |     |')
    print('|  '+str(state[0,0])+'  |  ' +str(state[0, 1])+'  |' + '  '+str(state[0, 2])+'  |')
    print('|_____|_____|_____|')
    print('|     |     |     |')
    print('|  '+str(state[1,0])+'  |  ' +str(state[1, 1])+'  |' + '  '+str(state[1, 2])+'  |')
    print('|_____|_____|_____|')
    print('|     |     |     |')
    print('|  '+str(state[2,0])+'  |  ' +str(state[2, 1])+'  |' + '  '+str(state[2, 2])+'  |')
    print('|_____|_____|_____|')


    
    
