with open('file.txt', 'r') as file:
    # Open the file
    file_content = file.read()
    to_exclude = """,!;{}|[]^@\`*$/.?&~"'"""
    
    for x in to_exclude:
        file_content = file_content.replace(x, '')

    # Remove special characters
    file_content = file_content.strip(',*')
    # Split words around spaces
    words = file_content.split(' ')
    words = [w for w in words if w != '']
    count = len(words)
    if count == 1:
        out = 'mot'
    else:
        out = 'mots'
    print(f'Ce texte compte {count} {out} !') 



