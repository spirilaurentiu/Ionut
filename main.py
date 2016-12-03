import sys
import numpy as np
import argparse
import mat2vec as m2v

# Options 
parser = argparse.ArgumentParser()
parser.add_argument("--IDs", default="IDs_16x24.fake.txt", \
  help="Drug ID file")
parser.add_argument('--screen1', nargs='+', default="4xm8x12.txt", \
  help='List of activity files')
parser.add_argument('--screen2', nargs='+', default="4xm8x12.txt", \
  help='List of activity files')
args = parser.parse_args()

nrows = 16
ncols = 24
HitList = m2v.intializeHitList(nrows, ncols)

# Citeste ID-uri
IDs = m2v.DrugsFile_to_16x24(args.IDs)
lenscr = len(args.screen1)
Activities8x12 = lenscr * [None]

screeni = -1
for FN in args.screen1:
  screeni = screeni + 1
  # Citeste activitati
  Activities8x12[screeni] = m2v.M8x12File_to_4xm8x12(FN)

  #for k in range(4):
  #  m2v.print8x12(Activities8x12[screeni][k])

  Activities16x24 = m2v._4xm8x12_to_m16x24(Activities8x12[screeni])
  #m2v.print16x24(Activities16x24)
  #print

  # Cherry picking
  print "Primary cherry picking", screeni + 1
  m2v.cherryPick(Activities16x24, HitList, 75.0)
  #m2v.print16x24(HitList)
  #print
 
# Print hit IDs
print "Hits:"
for i in range(16):
  for j in range(24):
    if (HitList[i][j][0] != 0) or (HitList[i][j][1] != 0):
      IDs[int(HitList[i][j][0])][int(HitList[i][j][1])].print_params()

# Reset IDs
newDrugs = m2v.m16x24_to_Drugs96x24(HitList, IDs)
for i in range(16):
  for j in range(24):
    print "%9s" % (newDrugs[i][j].ID),
  print

lenscr = len(args.screen2)
Activities8x12 = lenscr * [None]
HitList = m2v.intializeHitList(nrows, ncols)

screeni = -1
for FN in args.screen2:
  screeni = screeni + 1
  # Citeste activitati
  Activities8x12[screeni] = m2v.M8x12File_to_4xm8x12(FN)

  for k in range(4):
    m2v.print8x12(Activities8x12[screeni][k])

  Activities16x24 = m2v._4xm8x12_to_m16x24(Activities8x12[screeni])
  m2v.print16x24(Activities16x24)
  print

  # Cherry picking
  print "Secondary cherry picking", screeni + 1
  m2v.cherryPick(Activities16x24, HitList, 75.0)
  #m2v.print16x24(HitList)
  #print


# Print hit IDs
print "Hits:"
for i in range(16):
  for j in range(24):
    if (HitList[i][j][0] != 0) or (HitList[i][j][1] != 0):
      IDs[int(HitList[i][j][0])][int(HitList[i][j][1])].print_params()

# Reset IDs
newDrugs = m2v.m16x24_to_Drugs96x24(HitList, IDs)
for i in range(16):
  for j in range(24):
    print "%9s" % (newDrugs[i][j].ID),
  print


