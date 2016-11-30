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

def print8x12(data):
  """
  :param data:
  :param type: 8x12x3 numpy array 
  """
  for i in range(8):
    for j in range(12):
      print "%6.3f" % (data[i][j][2]),
    print
  print
#

def print16x24(data):
  """
  :param data:
  :param type: 16x24x3 numpy array 
  """
  for i in range(16):
    for j in range(24):
      print "%6.3f" % (data[i][j][2]),
    print
  print
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

def M8x12File_to_4xm8x12(FN):
  """
  Reads activity info from a file and turns it into
  four 8x12x3 numpy array. Sets the addresses as if they were
  taken from a 16x24 plate.
  :param FN: File
  :type string
  :return type: 8x12x3 array
  """
  nrows = 8
  ncols = 12
  D = np.zeros((nrows, ncols, 3)) # 16 x 24 x [i, j, activity]
  data = [copy.deepcopy(D) for x in range(4)]
  mi = 0
  di = dj = 0
  read_flag = 0
  with open(FN, 'r') as inFN:
    i = -1
    for line in inFN:
      words = re.sub(r'[!,;?\t]', ' ', line).split()
      if (len(words) == 0) and (read_flag == 1): # Read the next matrix
        read_flag = 0
        i = -1
        mi = mi + 1
      if (len(words) > 1):
        read_flag = 1
        if (len(words) != ncols):
          print "Wrong number of columns:", len(words)
          return None
        i = i + 1
        j = -1
        for word in words:
          j = j + 1
          #print str(i) + "," + str(j) + "|", # testing
          di = (i * 2) + np.floor(mi/2)
          dj = (j * 2) + (mi % 2)
          (data[mi])[i][j] = np.array([di, dj, float(word)])
        #print # testing

  for mi in range(4):
    for i in range(nrows):
      if (i == 0) or (i == 7):
        for j in range(12): # all cols
          if (j == 1) or (j == 10):
            (data[mi])[i][j][2] = -1
    for i in range(nrows):
      for j in range(12):
        if (j == 0) or (j == 11):
          (data[mi])[i][j][2] = -1

  return data
#

def copyAddressInfo(m_src, m_dest):
  """
  Designed to copy only address info ([i][j][0, 1]) 
  from a 8x12 matrix to another 8x12.
  :param m_src: 8 x 12 x 3 numpy array
  :param m_dest: 8 x 12 x 3 array
  """
  if m_src.shape != m_dest.shape:
    print "Matrices don't have the same shape:", m_src.shape, m_dest.shape 
    sys.exit(1)
  for i in range(m_src.shape[0]):
    for j in range(m_src.shape[1]):
      m_dest[i][j][0] = m_src[i][j][0]
      m_dest[i][j][1] = m_src[i][j][1]
  #TODO: test
#

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

def _4xm8x12_to_m16x24(input):
  """
  Turns four 8x12 matrices into one 16x24 matrix
  :param list(m8x12_0, m8x12_1, m8x12_2, m8x12_3): List of four input matrices
  :type 8x12 numpy bidimensional array
  :return type: 16x24 numpy bidimensional array
  """
  nrows = 16
  ncols = 24
  data = np.zeros((nrows, ncols, 3)) # 16 x 24 x [i, j, activity]
  for mi in range(4):
    for i in range(8):
      for j in range(12):
        data[(input[mi])[i][j][0]][(input[mi])[i][j][1]][0] = (input[mi])[i][j][0]
        data[(input[mi])[i][j][0]][(input[mi])[i][j][1]][1] = (input[mi])[i][j][1]
        data[(input[mi])[i][j][0]][(input[mi])[i][j][1]][2] = (input[mi])[i][j][2]
  return data
#

def intializeHitList(nrows, ncols):
  """
  :param nrows: # of rows 
  :param type: int
  :param ncols: # of columns
  :param type: int
  :return type: 16x24x3
  """
  data = np.zeros((nrows, ncols, 3))
  for i in range(nrows):
    for j in range(ncols):
      data[i][j][0] = 0
      data[i][j][1] = 0
      data[i][j][2] = -1.0
  return data
#

def cherryPick(input, hitlist, cutoff):
  """
  :param input: input 16x24 matrix
  :param type: 16x24x3 numpy array
  :return type: 16x24x3 numpy array with top2 bot2 left4 right4 margins
  """
  nrows = 16
  ncols = 24
  lm = rm = 4
  tm = bm = 2
  dnrows = nrows - tm - bm
  dncols = ncols - lm - rm
  toti = -1
  alreadyIn = 0
  foundHitFlag = False
  noHitFlag = False

  # Shift and place after the hits
  for i in range(nrows):
    for j in range(ncols):
      if (hitlist[i][j][0] != 0) or (hitlist[i][j][1] != 0):
        foundHitFlag = True
        break
    if foundHitFlag:
      break
  for ai in range(tm, nrows-bm): # Start reading hits already in place
    for aj in range(lm, ncols-rm):
      if (hitlist[ai][aj][0] == 0) and (hitlist[ai][aj][1] == 0):
        noHitFlag = True
        break
      else:
        alreadyIn = alreadyIn + 1
    if noHitFlag:
      break

  toti = toti + alreadyIn
  for i in range(nrows): # Place the hits
    for j in range(ncols):
      if input[i][j][2] >= cutoff:
        toti = toti + 1
        di = np.floor(toti/16) + tm
        if di > nrows:
          print "Too many hits: ", toti, ">", (16 - 2 - 2) * (24 - 4 - 4), 
          print ".You may consider changing the margins"
        dj = (toti % 16) + lm
        #print "%.0f %.0f|" % (di, dj), # testing
        hitlist[di][dj] = input[i][j]
    #print # Testing
  return hitlist
# 


