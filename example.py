import postag

def determiner_to_num(tag):
	"""Converts a/an to 1."""
	if tag[1] != "DET": return False, None
	if tag[0].lower() in ("a","an"): return True, ("1","NUM")
	return False, None
postag.tag_resolver.addResolver(determiner_to_num,1)

def filter_tag(tagged,filt,exclude_tags=[]):
	"""Scans tagged for a sequence of tokens with types matching filt. Optionally ignores tags in exclude_tags."""
	if exclude_tags:
		tagged = list(filter(lambda x: x[1] not in exclude_tags,tagged))
	for i in xrange(len(tagged)):
		if [x[1] for x in tagged[i:i+len(filt)]]==filt:
			return tagged[i:i+len(filt)]

tagged=postag.tag(raw_input("> "))
print(tagged)
info = filter_tag(tagged,"VERB NUM NOUN".split(),["PRON"])
print(info)
data = {x[1]: x[0] for x in info}
print("action =",data["VERB"])
print("count  =",data["NUM"])
print("object =",data["NOUN"])
