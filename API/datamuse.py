

import urllib, json

def read_jsonURL(jsonURL):
	url_response = urllib.urlopen(jsonURL)
	data = json.loads(url_response.read())
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

