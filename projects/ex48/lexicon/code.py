DICTIONARY = {
    'direction': ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back'],
    'verb': ['go', 'stop', 'kill', 'eat'],
    'stop': ['the', 'in', 'of', 'from', 'at', 'it'],
    'noun': ['door', 'bear', 'princess', 'cabinet']
}


def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None


def scan(user_input: str):

    sentence = []
    for word in user_input.split():
        found = False
        if convert_number(word):
            sentence.append(('number', convert_number(word)))
            found = True
        else:
            for item in DICTIONARY:
                if word in DICTIONARY[item]:
                    sentence.append((item, word))
                    found = True
        if not found:
            sentence.append(('error', word))
    return sentence
