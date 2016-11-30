import sys
import numpy as np
import mat2vec as m2v

# Citeste ID-uri
FN = sys.argv[1]
IDs = m2v.DrugsFile_to_16x24("IDs_16x24.txt")

# Citeste activitati
FN = sys.argv[2]
Activities8x12 = m2v.M8x12File_to_4xm8x12(FN)
for k in range(4):
  m2v.print8x12(Activities8x12[k])

Activities16x24 = m2v._4xm8x12_to_m16x24(Activities8x12)
m2v.print16x24(Activities16x24)
print

# Cherry picking
nrows = 16
ncols = 24
HitList = m2v.intializeHitList(nrows, ncols)
for k in range(5):
  print "Cherry picking", k
  m2v.cherryPick(Activities16x24, HitList, 75.0)
  m2v.print16x24(HitList)
  print
 
# Print hit IDs
for i in range(16):
  for j in range(24):
    if (HitList[i][j][0] != 0) or (HitList[i][j][1] != 0):
      IDs[int(HitList[i][j][0])][int(HitList[i][j][1])].print_params()



