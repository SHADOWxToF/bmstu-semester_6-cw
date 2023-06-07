from random import random, choice


PROBABILITY = {
    'noun': 40,
    'subAction': 20,
    'obAction': 20,
    'adjective': 20
}


def read_lorem(filename: str):
    f = open(filename, "r")
    text = f.readline().split()
    f.close()
    for i, word in enumerate(text):
        if word[-1] == ',' or word[-1] == '.':
            word = word[:-1]
        text[i] = word.lower()
    text = list(set(text))[:100]
    noun = []
    subAction = []
    obAction = []
    adjective = []
    for word in text:
        prob = choice(range(1, 101))
        if 0 < prob <= PROBABILITY['noun']:
            noun.append(word)
        prob -= PROBABILITY['noun']
        
        if 0 < prob <= PROBABILITY['subAction']:
            subAction.append(word)
        prob -= PROBABILITY['subAction']

        if 0 < prob <= PROBABILITY['obAction']:
            obAction.append(word)
        prob -= PROBABILITY['obAction']
        
        if 0 < prob <= PROBABILITY['adjective']:
            adjective.append(word)
    
    query = ""
    for word in noun:
        query += f"CREATE ({word}:noun {{text: '{word}', image: 'images/{word}.png'}})\n"
    for word in subAction:
        query += f"CREATE ({word}:subAction {{text: '{word}', image: 'images/{word}.png'}})\n"
    for word in obAction:
        query += f"CREATE ({word}:obAction {{text: '{word}', image: 'images/{word}.png'}})\n"
    for word in adjective:
        query += f"CREATE ({word}:adjective {{text: '{word}', image: 'images/{word}.png'}})\n"
    
    for word in adjective:
        used_words = []
        count = choice(range(1, 6))
        for i in range(count):
            relation = choice(range(1, 4))
            if relation == 1:
                new_word = choice(noun)
                while new_word in used_words:
                    new_word = choice(noun)
                used_words.append(new_word)
            if relation == 2:
                new_word = choice(subAction)
                while new_word in used_words:
                    new_word = choice(subAction)
                used_words.append(new_word)
            if relation == 3:
                new_word = choice(obAction)
                while new_word in used_words:
                    new_word = choice(obAction)
                used_words.append(new_word)
            query += f"CREATE ({used_words[-1]})-[:have]->({word})\n"

    for word in subAction:
        used_words = []
        count = choice(range(1, 11))
        for i in range(count):
            new_word = choice(noun)
            while new_word in used_words:
                new_word = choice(noun)
            used_words.append(new_word)
            query += f"CREATE ({used_words[-1]})-[:is_done]->({word})\n"
    
    for word in obAction:
        used_words = []
        count = choice(range(1, 11))
        for i in range(count):
            new_word = choice(noun)
            while new_word in used_words:
                new_word = choice(noun)
            used_words.append(new_word)
            query += f"CREATE ({used_words[-1]})-[:doing]->({word})\n"

    query += "CREATE (user:owner {name: 'Lorem ipsum', date: datetime('2005-02-15'), desease: 'Lorem ipsum dolor sit amet'});\n"
    query += "MATCH (n), (m:owner) where n<>m create (m)-[:own]->(n)\n"
    f = open("dictionary100.cypher", "w")
    f.write(query)
    f.close()
    # print(text, len(text))


def main():
    read_lorem("lorem_ipsum.txt")



if __name__=="__main__":
    main()