import re
import sys

file = sys.argv[1]

author = list(filter(lambda x: len(x) > 0,[re.findall(r"\\author{.*}", line) for line in open(file)]))[0][0][8:-1]
title = list(filter(lambda x: len(x) > 0,[re.findall(r"\\title{.*}", line) for line in open(file)]))[0][0][7:-1]
subtitle = list(filter(lambda x: len(x) > 0,[re.findall(r"\\subtitle{.*}", line) for line in open(file)]))[0][0][10:-1]

print(author, title, subtitle)
