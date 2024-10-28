import re
import json

alice_znaky = {}

with open("alice.txt", mode="r", encoding="utf-8") as alice_file:
    for row in alice_file:
        row = re.sub(r"[\n\t\s]*", "", row)
        for character in row:
            character = character.lower()
            if character in alice_znaky:
                alice_znaky[character] += 1
            else:
                alice_znaky[character] = 1

alice_znaky_sorted = dict(sorted(alice_znaky.items()))
del alice_znaky

with open("hw01_output.json", mode="w", encoding="utf-8") as out_file:
    json.dump(alice_znaky_sorted, out_file, ensure_ascii=False, indent=4)
