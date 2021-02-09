
def tokenization(operation):
    i = 0
    characters = [""]

    for character in operation:
        try:
            int(character)
            characters[i] = characters[i] + character
        except:
            characters.append(character)
            characters.append("")
            i = len(characters) - 1

    return characters