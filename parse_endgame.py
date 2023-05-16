import csv

def checkExist(name):
    characters = ["TONY", "STEVE", "PEGGY", "HOWARD", "NEBULA", "NATASHA",
                  "CLINT BARTON", "HULK", "THOR", "SCOTT", "PETER", "QUILL",
                  "GAMORA", "SOCKET", "WANDA", "THANOS", "GROOT"]
    for c in characters:
        if c in name:
            return c
    return ""

if __name__ == '__main__':

    with open('Avengers_Endgame_parsed.txt', 'r') as f:
        file_contents = f.read()

    dialogue_dict = {}
    # characters = ["ELSA", "ANNA", "OLAF", "HANS", "KRISTOFF"]

    i = 0
    lines = file_contents.split('\n')
    # print(len(lines))
    while i < len(lines):
        # Try to match the line to a character name
        if lines[i].startswith("C:"):
            name = lines[i].split(": ")[1]
            # print(name)
            character = checkExist(name)
            # print("chater:" + character)
            if len(character) > 0:
                # print(lines[i + 1])
                if lines[i + 1].startswith("D:"):
                    dialogue = lines[i + 1].split(": ")[1]
                    if character in dialogue_dict:
                        dialogue_dict[character].append(dialogue)
                    else:
                        dialogue_dict[character] = [dialogue]
                    i = i + 1
            name = ""
        i = i + 1
    # Print the dialogue for each character
    for c, d in dialogue_dict.items():
        # print(f"{character}: {dialogue}")
        print(c + ": \n")
        print(d)
        print("-------\n")

    filename = 'endgame_output.csv'

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['character', 'script'])
        for key, values in dialogue_dict.items():
            writer.writerow([key, ','.join(values)])