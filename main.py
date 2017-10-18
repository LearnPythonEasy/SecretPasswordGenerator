import random
import string

#Password Generating Program
#Created by Nate (http://github.com/ACA30)

adjectives = ['sleepy', 'dopey', 'stupid', 'fat', 'old', 'ugly', 'awesome', 'egotistical', 'brave', 'kind', 'agreeable', 'living', 'dead', 'calm', 'delighted', 'colossal', 'tiny', 'bitter', 'delicious', 'fresh', 'abandoned', 'substantial', 'sparse', 'dank', 'moist', 'weak', 'wet', 'faint', 'hissing', 'puking', 'clever', 'rich', 'magnificent', 'glamorous', 'important', 'different', 'public', 'evil', 'aggressive', 'abiding', 'adhesive', 'alleged', 'addicted', 'acidic', 'helpful']
colours = ['red', 'green', 'blue', 'purple', 'orange', 'pink', 'grey']
nouns = ['banana', 'superhero', 'giraffe', 'dinosaur', 'pillow', 'cloud', 'keyboard', 'human', 'american', 'desk', 'coffee', 'store', 'plant', 'people', 'history', 'way', 'art', 'world', 'information', 'government', 'product', 'product', 'investment', 'technology', 'physics', 'analytics', 'policy', 'series', 'child', 'article', 'department', 'user', 'combination', 'disk', 'energy', 'student', 'wood', 'debt', 'prescription', 'secretary', 'alcohol', 'password', 'engineering']

name = input('What is your name? ')


print('')
print('Welcome to the Secret Password Generator,', name)

while True:
    adjective = random.choice(adjectives)
    colour = random.choice(colours)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)
    password = adjective + colour + noun + str(number) + special_char
    print('')
    print('Your password is %s'% password.upper())

    response = input('Would you like another password? y or n: ')
    if response == 'n':
        print('')
        print('')
        print('Thank you for using the Secret Password Generator')
        print('Created by Nate - http://github.com/ACA30')
        print('License can be found at: https://github.com/LearnPythonEasy/SecretPasswordGenerator/blob/master/LICENSE')
        print('')
        print('')
        break
