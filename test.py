import sys
import re
import numpy as np
import mat2vec as m2v

if len(sys.argv) <= 1:
  print "Usage: python tests.py <input_file>"
  sys.exit(0)
FN = sys.argv[1]

print "Testing file2vec..."
data = m2v.file2vec(FN)
for d in data:
  print d
print "Done."

print "Testing Drug class..."
ID = "8014-6229"
pno = 001
ppos = "A03"
w = 0.7
mw = 348.42
cono = 000001

D = m2v.Drug(ID, pno, ppos, w, mw, cono)
D.set_address(4, 5)
print "D.parameters: ", D.ID, D.pno, D.ppos, D.w, D.mw, D.cono
print "D.get_address()", D.get_address()
D.pno = 34
print "D.pno: ", D.pno
print "Done."
