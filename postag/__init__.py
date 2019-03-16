import nltk
from nltk.corpus import treebank
from nltk.tag.sequential import UnigramTagger

import postag.resolver

tag_resolver = postag.resolver.Resolver()
def default_resolver(tag):
	return True,tag
tag_resolver.addResolver(default_resolver,-1000)

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")

def singularize(w): return stemmer.stem(w)

def singularize_plurals(tag):
	if tag[1] is not None: return False, None
	w = singularize(tag[0])
	if postag.tagger.tag([w])[0][1] is None: return False, None
	return True, (tag[0],postag.tagger.tag([w])[0][1])
tag_resolver.addResolver(singularize_plurals,0)

def tag_as_noun(tag):
	if tag[1] is not None: return False, None
	return True, (tag[0],"NOUN")
tag_resolver.addResolver(tag_as_noun,-999)

tagger = UnigramTagger(treebank.tagged_sents(tagset="universal"))

def tag(sent):
	tagged = tagger.tag(nltk.word_tokenize(sent))
	ret = []
	for tag in tagged:
		ret.append(tag_resolver.resolve(tag))
	return ret

def tag_sents(sents):
	r = []
	for sent in sents:
		r.append(sent)
	return r
