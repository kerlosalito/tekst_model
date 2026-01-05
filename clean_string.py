# Deel van de methode #clean_string, WIP

words = {}
tekst = "Ik ben Kerlos! ik ben een grapjas."
for word in tekst.split():
    sentence = word.lower()
    if word[-1] in "?!.,":
        word = word[:-1]
        
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1
print(words)