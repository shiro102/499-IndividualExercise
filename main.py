from searchFeature import search
from statFeature import stat


def main():
    end_point = True
    input_main = input('Enter something: ')
    while end_point:
        x = input('\nWhat do you want to do with your string? \n '
                  '1: Find occurrence of a certain keyword \n '
                  '2: Find occurrences for all keywords \n '
                  '3: Exit \n Your choice : ')
        if x == '1':
            input_key = input('\nEnter the keyword or substring '
                              'you want to count in your string: ')
            print('Number of occurrence for "{:s}" is {:d}'
                  .format(input_key, search(input_main, input_key)))
        elif x == '2':
            print('\nHere is the stat of all the words in your string:')
            for s in stat(input_main):
                print(s)

        elif x == '3':
            print('Thanks for using the software. Have a good day')
            end_point = False
        else:
            print('Cannot understand the answer, please try again\n')


main()
