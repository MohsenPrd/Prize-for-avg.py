## Mohsen Pourdehghan

toys = ['ball', 'robot', 'sword', 'gun']
print(toys)

print('\nhey kid, show me your lessons scores...')

math = int(input('Math score: '))
while math > 20 or math < 0 :
    math = int(input('Invalid! Math score: '))

    
science = int(input('Science score: '))
while science > 20 or science < 0 :
    science = int(input('Invalid! Science score: '))

    
sports = int(input('Sports score: '))
while sports > 20 or sports < 0 :
    sports = int(input('Invalid! Sports score: '))


art = int(input('Art score: '))
while art > 20 or art < 0 :
    art = int(input('Invalid! Art score: '))

    
geography = int(input('Geography score: '))
while geography > 20 or geography < 0 :
    geography = int(input('Invalid! Geography score: '))

scores = math + science + sports + art + geography
avg = scores / 5

if avg >= 18 :
    print(f'\nYour avg: {avg}, Here is your prize!!!\n')
    toys.append('Playstation')
    print(toys)
else:
    print(f'\nYour avg: {avg}, you missed a good prize :(')
