#!/usr/bin/env python3
"""
For any two subsets A and B of a set U, where |U| < 10,000,
demonstrate the operations:
   A u B   the union of A and B
   A n B   the intersection of A and B
   A - B   set difference
   B - A   set difference
   A^c     where A^c is the complement of A with respect to U
   B^c     where B^c is the complement of B with respect to U

Input: n {a1, a2, ...} {b1, b2, ...}
 Where n = |U| < 10,000
 {a1, ...} is all elements of A which must be a subset of U
 {b1, ...} is all elements of B which must be a subset of U
"""

class SetOperations():
   def __init__(self, x):
      #cleanup sequences
      s = x.split()
      self.n = int(s[0])
      self.A = s[1].replace('{', '').replace('}', '').split(',')
      self.B = s[2].replace('{', '').replace('}', '').split(',')
      self.U = []
      for i in range(1,self.n+1):
         self.U.append(str(i))   # to match other output

   def union(self):
      u = (list(self.A))
      for x in self.B:
         if x not in u:
            u.append(x)
      print(u)


   def intersection(self):
      i = []
      for x in self.A:
         if x in self.B:
            i.append(x)
      print(i)

   def difference(self, flag = False):
      d = []
      # A - B
      if flag:
         for x in self.A:
            if x not in self.B:
               d.append(x)
      # B - A
      else:
         for x in self.B:
            if x not in self.A:
               d.append(x)
      print(d)

   def complement(self, flag = False):
      c = []
      if flag:
         for x in self.U:
            if x not in self.A:
               c.append(x)
      else:
         for x in self.U:
            if x not in self.B:
               c.append(x)
      print(c)

#get input
setOps = SetOperations(input("Enter input:\n"))
setOps.union()
setOps.intersection()
setOps.difference(True) # A - B
setOps.difference()     # B - A
setOps.complement(True) # A^c
setOps.complement()     # B^c
