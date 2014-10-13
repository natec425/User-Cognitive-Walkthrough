import datetime
import logging

MENU = '''
1. (goal)   User's immediate goal
2. (action) Atomic action taken
3. (prob)   Problems/comments
4. (note)   Designer Note
5. (menu)   Print menu
6. (quit)   Quit
'''

def init_log(evaluator, interface, task):
    time_stamp = str(datetime.datetime.today())
    logging.basicConfig(
        filename="_".join((evaluator, interface, task, time_stamp)).replace(' ', '_'),
        level=logging.INFO,
        format='%(asctime)s %(message)s',
        datefmt='%H:%M:%S')

def get_command():
    response, _, arg = input('>>> ').partition(' ')
    if response == 'ditto':
        print('saw ditto', 'previous is', get_command.previous)
        return get_command.previous
    else:
        print('updating previous to {}, {}'.format(response, arg))
        get_command.previous = response, arg
        return get_command.previous
    return helper
get_command.previous = 'menu', ''

def main():
    init_log(evaluator=input('Evaluator: '),
             interface = input('Interface: '),
             task = input('Task: '))
    while True:
        choice, arg = get_command()
        if choice == 'goal':
            logging.info('New Goal : ' + arg)
        elif choice == 'action':
            logging.info('New Action Taken : ' + arg)
        elif choice == 'prob':
            logging.info('New Problem/Comment : ' + arg)
        elif choice == 'note':
            logging.info('New Designer Note : ' + arg)
        elif choice == 'menu':
            print(MENU)
        elif choice == 'quit':
            break
        else:
            print('INVALID INPUT', MENU)

if __name__ == '__main__':
    main()
