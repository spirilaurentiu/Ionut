import sys
import re
import numpy as np

if len(sys.argv) <= 1:
  print "Usage: python mat2vec.py <input_file>"
  sys.exit(0)
FN = sys.argv[1]

def mat2vec(FN):
  """
  Turns a matrix into numpy array
  :param FN: matrix imput filename
  :type string
  :return type: numpy array
  """
  data = []
  with open(FN, 'r') as inFN:
    for line in inFN:
      words = re.sub(r'[.!,;?]', ' ', line).split()
      if len(words)>1:
        for word in words:
          data.append(float(word))
  data = np.array(data)
  return data


for d in data:
  print d
