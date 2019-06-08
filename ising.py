#!/usr/bin/env python
import numpy as np

class IsingMC(object):
  def __init__(self, Lx, Ly, h, beta, seed = 0):
    self.h = h
    self.beta = beta
    np.random.seed(seed)
    self.data = 2*np.random.randint(low = 0, high = 2, size = (Lx,Ly)) - 1


def test_init():
    mc = IsingMC(2, 2, 0.1, 10)

    assert mc.data.shape == (2, 2)
    assert (np.abs(mc.data) == 1).all()
    assert mc.h == 0.1
    assert mc.beta == 10
