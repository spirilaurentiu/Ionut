import sys
import re
import numpy as np
import copy

class Drug:
  """
  Holds information about a drug
  """
  def __init__(self, ID, pno, ppos, w, mw, cono):
    """
    :param ID: Company ID :type string
    :param pno: Original Plate number :type int
    :param ppos: Original plate position :type string
    :param w: Original Weight :type float
    :param mw: Molecular Weight :type float
    :param cono: Company number :type int
    """
    self.ID = ID
    self.pno = pno
    self.ppos = ppos
    self.w = w
    self.mw = mw
    self.cono = cono
    self.address = np.array([0, 0])

  def set_address(self, i, j):
    self.address = np.array([i, j])
  def get_address(self):
    return self.address
  def print_params(self):
    print self.address, self.ID, self.pno, self.ppos, self.w, self.mw, self.cono
#

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

def DrugsFile_to_16x24(FN):
  """
  Reads drugs info from a file and turns it into
  a 16x24 bidim array
  :param FN: File
  :type string
  :return type: 16x24 matrix of IDs
  """
  nrow = 16
  ncol = 24
  D = Drug("-1", -1, "-1", -1., -1., -1)
  data = [[copy.deepcopy(D) for x in range(ncol)] for y in range(nrow)] 
  with open(FN, 'r') as inFN:
    nr = -1
    for line in inFN:
      words = re.sub(r'[!,;?\t]', ' ', line).split()
      if (len(words) > 1): 
        if (len(words) != ncol):
          print "Wrong number of columns:", len(words)
          return None
        nr = nr + 1
        i = int(nr/6)
        j = -1
        for word in words:
          j = j + 1
          #print str(i) + "," + str(j) + "|", # testing
          data[i][j].set_address(i, j)
          if (nr % 6) == 0:
            data[i][j].ID = word
          if (nr % 6) == 1:
            data[i][j].pno = int(word)
          if (nr % 6) == 2:
            data[i][j].ppos = word
          if (nr % 6) == 3:
            data[i][j].w = float(word)
          if (nr % 6) == 4:
            data[i][j].mw = float(word)
          if (nr % 6) == 5:
            data[i][j].cono = int(word)
        #print # testing
  return data
#

def M16x24File_to_16x24(FN):
  """
  Reads activity info from a file and turns it into
  a 16x24x3 numpy array
  :param FN: File
  :type string
  :return type: 16x24x3 array
  """
  nrows = 16
  ncols = 24
  data = np.zeros((nrows, ncols, 3)) # 16 x 24 x [i, j, activity]
  with open(FN, 'r') as inFN:
    i = -1
    for line in inFN:
      words = re.sub(r'[!,;?\t]', ' ', line).split()
      if (len(words) > 1):
        if (len(words) != ncols):
          print "Wrong number of columns:", len(words)
          return None
        i = i + 1
        j = -1
        for word in words:
          j = j + 1
          #print str(i) + "," + str(j) + "|", # testing
          data[i][j] = np.array([i, j, float(word)])
        #print # testing
  return data

def m16x24_to_4xm8x12(m16x24):
  """
  Turns 16x24 matrix into four 8x12 matrices
  :param m16x24: input matrix
  :type 16x24 numpy bidimensional array 
  :return type: list of 4 8x12 numpy bidimensional array
  """
  nrows = 16
  ncols = 24
  D = np.zeros((8, 12, 3))
  data = [copy.deepcopy(D) for x in range(4)]
  for j in range(ncols):
    for i in range(nrows):
      (data[((i%2) + (j%2)) + (i%2)])[np.floor(i/2)][np.floor(j/2)] = m16x24[i][j]
  return data
#

def _4xm8x12_to_m16x24(m8x12_0, m8x12_1, m8x12_2, m8x12_3):
  """
  Turns four 8x12 matrices into one 16x24 matrix
  :param m8x12_0, m8x12_1, m8x12_2, m8x12_3: four input matrices
  :type 8x12 numpy bidimensional array
  :return type: 16x24 numpy bidimensional array
  """
  print "Not implemented."
#


