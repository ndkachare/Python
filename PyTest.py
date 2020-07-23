command = ""
started = False
while True:
    command = input('>').upper()
    if command == 'START':
        if started:
            print('Car  is already started')
        else:
            started = True
        print('Car started.....Ready to go!')
    elif command == 'STOP':
        if not started:
            print('Car is already stopped')
        else:
            started = False
            print('Car stopped.')
    elif command == 'HELP':
        print('''
start - to start the car
stop - to stop the car
quit - to exit''')
    elif command == 'QUIT':
        break
    else:
        print('Sorry, i dont understand that')