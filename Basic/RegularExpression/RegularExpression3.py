import re
string = "The quick brown fox jumps over the lazy dog"
string_to_find = r"The"
pattern = re.compile(string_to_find,re.I)
print("Output #40: {:s}".format(pattern.sub("a",string)))