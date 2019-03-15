import nltk
from nltk.corpus import brown
from nltk.tag.sequential import UnigramTagger

tagger = UnigramTagger(brown.tagged_sents(tagset="universal"))

def tag(sent):
	return tagger.tag(nltk.word_tokenize(sent))

def tag_sents(sents):
	r = []
	for sent in sents:
		r.append(sent)
	return r
