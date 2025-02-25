"""
Merge Mail | Send Emails Automation
"""

def main():
    starting_letter = read_starting_letter()
    with open('./Input/Names/invited_names.txt' ,mode='r') as invited_names_txt:
        invited_names = invited_names_txt.readlines()

    for name in invited_names:
        write_letter(starting_letter, name)

    print('\n\nAll Guests has been sent an invitation letter Master Cyril.')


def read_starting_letter():
    with open('./Input/Letters/starting_letter.txt', mode='r') as starting_letter_txt:
        starting_letter = starting_letter_txt.read()
    return starting_letter

def write_letter(starting_letter,name):
    clean_name = name.split('\\')[0].strip()
    path = f'./Output/ReadyToSend/letter_to_{clean_name}.txt'
    print(path)
    with open(path,mode='w') as new_letter:
        edited_letter = starting_letter.replace('[name]', clean_name)
        new_letter.write(edited_letter)


if __name__ == "__main__":
    main()

