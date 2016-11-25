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

print "Testing Reading IDs..."
nrows = 16
ncols = 24
with open("IDs_16x24.fake.txt", 'w') as f:
  for row in range(nrows*6):
    if (row % 6) == 0:
      for col in range(ncols):
        f.write( " ID" + str(col))
      f.write("\n")
    elif (row % 6) == 1:
      for col in range(ncols):
        f.write( " 00" + str(col))
      f.write("\n")
    elif (row % 6) == 2:
      for col in range(ncols):
        f.write( " A" + str(col))
      f.write("\n")
    elif (row % 6) == 3:
      for col in range(ncols):
        f.write( " %.1f" % (float(col) / 10.0))
      f.write("\n")
    elif (row % 6) == 4:
      for col in range(ncols):
        f.write( " %.2f" % (float(col) * 10.0))
      f.write("\n")
    elif (row % 6) == 5:
      for col in range(ncols):
        f.write( " 00000" + str(col))
      f.write("\n")

data = m2v.DrugsFile_to_16x24("IDs_16x24.fake.txt")
for i in range(nrows):
  for j in range(ncols):
    data[i][j].print_params()


print "Done."




