#!/usr/bin/env python
import numpy as np

##Here is my change 

class IsingMC(object):
  def __init__(self, Lx, Ly, h, beta, seed = 0):
    self.h = h
    self.beta = beta
    np.random.seed(seed)
    self.data = 2*np.random.randint(low = 0, high = 2, size = (Lx,Ly)) - 1

  def energy(self):
    Lx, Ly = self.data.shape
    e = 0
    for i in range(Lx):
      for j in range(Ly):
        site = self.data[i,j]
        neigh = []
        #Lower neigh
        neigh.append(self.data[i,(Ly-1 if j ==0 else j-1)])
        #Upper neigh
        neigh.append(self.data[i,(0 if j == Ly-1 else j+1)])
        #Left neigh
        neigh.append(self.data[(Lx-1 if i == 0 else i-1),j])
        #Right neigh
        neigh.append(self.data[(0 if i == Lx-1 else i+1),j])
        for n in neigh: # Exchange contribution
          e -= site*n
        e -= site*self.h # Magnetic field contribution

    return e

def test_init():
  mc = IsingMC(2, 2, 0.1, 10)

  assert mc.data.shape == (2, 2)
  assert (np.abs(mc.data) == 1).all()
  assert mc.h == 0.1
  assert mc.beta == 10

def test_energy():
  Lx = 10
  Ly = 10
  h = 0.1
  mc = IsingMC(Lx, Ly, h, 2)
  N = Lx*Ly

  mc.data = np.ones((Lx,Ly), dtype=int)
  assert np.abs(mc.energy() - (-4*N - h*N)) < 1e-10
  mc.data = -np.ones((Lx,Ly), dtype=int)
  assert np.abs(mc.energy() - (-4*N + h*N)) < 1e-10
