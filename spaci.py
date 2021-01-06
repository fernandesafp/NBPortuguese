from rule_translator import nbify

def organize_text(sentence):
    sentence = sentence.replace('  ', ' ').replace('\n ','\n') #removes double spaces from deleting 'o(s)' or 'a(s)'
    for i in enumerate(sentence):
        if sentence[i] != ' ':
            sentence = sentence[i:]
            break #in case sentence contains empty spaces

    stoppers = ['. ', '! ', '? ']
    for stopper in stoppers:
        lines = sentence.split(stopper)

        for index, line in enumerate(lines):
            try:
                lines[index] = line[0].upper() + line[1:]
            except Exception as ex:
                lines[index] = line[0] + line[1:]
                print('Could not capitalize first letter. ' + ex)

        sentence = stopper.join(lines)

    return sentence

def run_model(database, nlp, sentence):
    if len(sentence.split()) == 1: #if it's only a word, it will try to nbify it.
        return nbify(database, sentence)

    sentence = sentence.replace('\r\n','\n')
    doc = nlp(sentence)

    start_char = []
    end_char = []
    words = []
    for ent in doc.ents:
        words.append(ent.text)
        start_char.append(ent.start_char)
        end_char.append(ent.end_char)

    tmp = sentence
    while len(words) > 0:
        next_word_index = start_char.index(max(start_char)) #starts from last to first (eases coordinate replacement)
        word_start = start_char[next_word_index]
        word_end = end_char[next_word_index]

        gendered_word = tmp[word_start:word_end]
        nb_word = nbify(database, gendered_word) #translates gendered word into non-binary

        new_sentence = tmp[:word_start] + nb_word + tmp[word_end:]
        tmp = new_sentence

        start_char.pop(next_word_index)
        end_char.pop(next_word_index)
        words.pop(next_word_index)
    nb_text = organize_text(tmp).replace('\n','<br/>')
    nb_text = nb_text.replace('ume pessoa','uma pessoa').replace('ume Pessoa','uma Pessoa').replace('minhe pessoa','minhe parceire').replace('minhe Pessoa','minhe Parceire').replace('minhe figura parental','minha figura parental').replace('minhe Figura parental','minha Figura parental')
    return nb_text