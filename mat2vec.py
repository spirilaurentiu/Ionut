import sys
import re
import numpy as np

class Drug(self):
  """
  Holds information about a drug
  """
  def _init_(self, ID, pno, ppos, w, mw, cono):
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
  with open(FN, 'r') as inFN:
    for line in inFN:
      words = re.sub(r'[.!,;?]', ' ', line).split()
      if (len(words) > 1) and (len(words) != 24):
        print "Wrong number of columns:", len(words)
        return None
      for word in words:
        data.append(word)
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


