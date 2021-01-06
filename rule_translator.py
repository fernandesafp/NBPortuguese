def get_nb_word(database, gendered_word):
    if gendered_word.lower() in database:
        nb_word = database[gendered_word]
    return nb_word

def nbify(database, word):
    #Remove \n's
    linebreaks = 0
    if word.endswith('\n'):
        word = word[:-2]
        linebreaks += 1

    #Clean word
    last_char = ''
    last_index = 0
    for i in range(len(word) - 1):
        if not word[-i - 1].isalpha() and not word[-i - 1] == '-':
            last_char += word[-i - 1]
            last_index = - i - 1
        else:
            break
    if last_char != '':
        word = word[:last_index]
        last_char = last_char[::-1]

    #Check capitalization
    capitalize = False
    all_caps = False
    if word[0].isupper():
        capitalize = True
        if len(word) > 1:
            if word[1].isupper():
                all_caps = True

    #Check plural
    if word[-1].lower().endswith('s'):
        word = word.lower()[:-1]
        plural = True
    else:
        word = word.lower()
        plural = False

    if word in database:
        nb_word = database[word]
        if all_caps:
            return nb_word.upper()
        elif capitalize:
            return nb_word[0].upper() + nb_word[1:]
        return nb_word
    elif plural and (word + 's') in database:
        nb_word = database[word + 's']
        if all_caps:
            return nb_word.upper()
        elif capitalize:
            return nb_word[0].upper() + nb_word[1:]
        return nb_word


    if len(word) < 2:
        if word.endswith('a') or word.endswith('o'):
            nb_word = '' #will leave blank in cases for 'a(s)' 'o(s)'
            return nb_word

    #Checks rare endings
    n = 2 #most common ending
    rule = ''
    if word.endswith('ista'):
        rule = 'ista'
        n = 4
    elif word.endswith('-la') or word.endswith('-lo'):
        rule = '-le'
    elif word.endswith('la') or word.endswith('le'): #by now if this is the case it should be lu
        rule = 'lu'
    elif word.endswith('ca') or word.endswith('co'):
        rule = 'que'
    elif word.endswith('ga') or word.endswith('go'):
        rule = 'gue'
    elif word.endswith('um'):
        rule = 'ume'
    elif word.endswith('uma'):
        rule = 'ume'
        n = 3
    elif word.endswith('meu'):
        rule = 'minhe'
        n = 3
    elif word.endswith('nha'):
        rule = 'nhe'
        n = 3
    elif word.endswith('lha') or word.endswith('lhe'):
        rule = 'lhu'
        n = 3
    elif word.endswith('ua') or word.endswith('eu'):
        rule = 'ue'
    elif word.endswith('um'):
        rule = 'ume'
    elif word.endswith('un') and plural:
        rule = 'umes'
        plural = False
    elif word.endswith('ça') or word.endswith('ço'):
        rule = 'ce'
    elif word.endswith('ã'):
        rule = 'ã'
        n = 1
    elif word.endswith('ão') or word.endswith('õe'):
        rule = 'ãe'
    elif word.endswith('esa'):
        rule = 'ese'
        n = 3
    elif word.endswith('ê') and plural:
        rule = 'ese'
        plural = False
    elif word.endswith('-a') or word.endswith('-o'):
        rule = '-e'
    elif word.endswith('ora') and not plural:
        rule = 'ore'
        n = 3
    elif word.endswith('or'):
        rule = 'ore'
    elif (word.endswith('ore') or word.endswith('ora')) and plural:
        rule = 'orie'
        n = 3
    elif word.endswith('ª') or word.endswith('º'):
        rule = 'e'
        n = 1
    elif word.endswith('o') or word.endswith('a'):
        rule = 'e'
        n = 1

    if rule != '':
        nb_word = word[:-n] + rule
        if plural:
            nb_word += 's'
    else:
        nb_word = word
    if all_caps:
        nb_word = nb_word.upper()
    elif capitalize:
        nb_word = nb_word[0].upper() + nb_word[1:]

    final_word = nb_word + last_char + '\n'*linebreaks
    return final_word