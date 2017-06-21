

import urllib.request, json, csv

def read_jsonURL(jsonURL):
	with urllib.request.urlopen(jsonURL) as url:
		data = json.loads(url.read().decode())
	return data

rhyme_url = "https://api.datamuse.com/words?rel_rhy="
curr_word = "forgetful"
curr_url = rhyme_url + curr_word
rhyme_data = read_jsonURL(curr_url)

curr_dict = dict()
for element in rhyme_data:
	if ' ' not in element["word"]:
		curr_dict[str(element["word"])] = len(str(element["word"]))

print(curr_dict['fretful'])

