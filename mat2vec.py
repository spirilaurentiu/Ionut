import sys
import re
import numpy as np

def file2vec(FN):
  """
  Reads matrix from file and turns it into numpy array
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
#

def m16x24_to_m4x8x12(m16x24):
  """
  Turns 16x24 matrix into four 8x12 matrices
  :param m16x24: input matrix
  :type 16x24 numpy bidimensional array 
  :return type: list of 4 8x12 numpy bidimensional array
  """
  print "Not implemented."
#

def m4x8x12_to_m16x24(m8x12_0, m8x12_1, m8x12_2, m8x12_3):
  """
  Turns four 8x12 matrices into one 16x24 matrix
  :param m8x12_0, m8x12_1, m8x12_2, m8x12_3: four input matrices
  :type 8x12 numpy bidimensional array
  :return type: 16x24 numpy bidimensional array
  """
  print "Not implemented."
#


