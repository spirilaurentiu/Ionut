import sys
import re
import numpy as np

FN = sys.argv[1]

#print 'Loading data from ' + FN + ' ... ',
data = []
with open(FN, 'r') as inFN:
  for line in inFN:
    words = re.sub(r'[.!,;?]', ' ', line).split()
    if len(words)>1:
      for word in words:
        data.append(float(word))
data = np.array(data)
#print 'Done.'
for d in data:
  print d
