from pickle import dump, load

def dumping(var, doc):
	my_dict = globals()
	x = "Variable"
	my_dict[x] = var
	with open(doc, "wb") as fp:   
   		dump(Variable, fp)

def loading(var, doc):
	my_dict = globals()
	with open(doc, "rb") as fp:   
		my_dict[var] = load(fp)
		return my_dict[var]
