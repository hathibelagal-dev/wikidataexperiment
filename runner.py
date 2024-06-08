import requests as r
import json
import time

language_code = "en"

words = {}

with open("concepts.txt") as c:
    lines = c.read().split("\n")
    for l in lines:
        if not l:
            continue
        item = l.split("=")
        words[item[0]] = item[1]

headers = {
    'User-Agent': 'HathiWikiExp 0.01',    
}

def handle_word(word, concept):
    query_str = f"https://query.wikidata.org/sparql?query=SELECT%20distinct%20%3Fx%20%3FxLabel%0AWHERE%0A%7B%0A%20%20%3Fx%20wdt%3AP31%2Fwdt%3AP279*%20wd%3A{concept}.%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22{language_code}%22.%20%7D%0A%7D&format=json"
    query = r.get(
        query_str, 
        headers=headers).json()
    for item in query["results"]["bindings"]:
        try:
            i = item["xLabel"]["value"]
            if not i.startswith("Q"):
                print(f"{word} = {i}")
        except:
            pass

for word in words:
    try:
        time.sleep(3)
        concept = words[word]
        handle_word(word, words[word])
    except:
        pass
