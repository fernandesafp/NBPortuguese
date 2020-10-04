from configs import database_file

def load_database():
    print('Loading database...')
    database = {}
    with open(database_file) as db:
        lines = db.readlines()
    for line in lines:
        words = line.replace('\n','').split('\t')
        pt = words[0] #gendered portuguese
        nb = words[1] #nb portuguese
        database[pt] = nb
    print('Loading complete.')
    return database

def save_to_database(pt_word, nb_word):
    print('Saving {} and {}...'.format(pt_word, nb_word))
    with open(database_file) as db:
        db.write('{}\t{}\n'.format(pt_word, nb_word))
    with open(database_file) as db:
        sorted_unique_words = {r[1]: r for r in sorted(db)}.values()
    new_database = ''.join(sorted_unique_words)
    with open(database_file, 'w') as db:
        db.write(new_database)
    database = load_database()
    print('Saved.')
    return database