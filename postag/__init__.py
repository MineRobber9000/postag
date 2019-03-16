import nltk
from nltk.corpus import treebank
from nltk.tag.sequential import UnigramTagger

import postag.resolver

tag_resolver = postag.resolver.Resolver()
def default_resolver(tag):
	return True,tag
tag_resolver.addResolver(default_resolver,-1000)

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
