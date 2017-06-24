

import urllib, json, random, os

def read_jsonURL(jsonURL):
	url_response = urllib.urlopen(jsonURL)
	data = json.loads(url_response.read())
	return data



def find_rhymes(word):
	rhyme_url = "https://api.datamuse.com/words?rel_rhy=" + str(word)
	rhyme_data = read_jsonURL(rhyme_url)

	rhyme_dict = dict()
	for element in rhyme_data:
		if ' ' not in element["word"]:
			rhyme_dict[str(element["word"])] = len(str(element["word"]))
	return rhyme_dict



def get_word():
	word_file = os.getcwd() + "/../words"
	word_list = open(word_file).read().splitlines()
	return random.choice(word_list)


def find_rhymable_word():
	done = False
	word = ""
	while(not done):
		word = get_word()
		rhyme_dict = find_rhymes(word)
		done = bool(rhyme_dict)
	return word, rhyme_dict			



curr_word, curr_rhymes_dict = find_rhymable_word()
print(curr_word)
print(curr_rhymes_dict)

