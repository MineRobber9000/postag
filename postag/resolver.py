class Resolver:
	def __init__(self):
		self.resolvers = []
	def addResolver(self,res,priority):
		self.resolvers.append(dict(resolver=res,priority=priority))
		self.resolvers.sort(key=lambda x: x["priority"])
	def resolve(self,name):
		for r in [x["resolver"] for x in self.resolvers[::-1]]:
			success,result = r(name)
			if success:
				return result

class GlobalVarResolver:
	def __init__(self,globs):
		self.globs = globs
	def __call__(self,name):
		if name in self.globs:
			return True, self.globs[name]
		elif name in dir(self.globs["__builtins__"]):
			return True, getattr(self.globs["__builtins__"],name)
		return False, None

class FunctionalMapping:
	def __init__(self,get,set):
		self.get = get
		self.set = set
	def __getitem__(self,k):
		return self.get(k)
	def __setitem__(self,k,v):
		self.set(k,v)
