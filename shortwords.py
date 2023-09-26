words = ['blah', 'boo', 'water', 'drink', 'coding', 'building', 'build', 'e/acc', 'a', 'b', 'dd', 'ss']

for shortwords in words:
    if len(shortwords) <= 2 or len(shortwords) >= 5:
        print(f'\nCongrats {shortwords} you are short enough!')
    else:
        print(f'\n{shortwords} does not meet the criteria.')
