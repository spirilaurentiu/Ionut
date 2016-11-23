import sys
import re
import numpy as np
import mat2vec as m2v

if len(sys.argv) <= 1:
  print "Usage: python main.py <input_file>"
  sys.exit(0)
FN = sys.argv[1]

data = m2v.mat2vec(FN)
for d in data:
  print d
