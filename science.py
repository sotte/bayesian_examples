"""
Default imports for pretty much every scientific thing I do.

"""
from __future__ import division
from __future__ import print_function

import os
import random
import math
from collections import namedtuple
from collections import OrderedDict
from pprint import pprint

# numpy, scipy, pandas
import numpy as np
from numpy import dot
from numpy import linalg
from numpy.linalg import inv
import scipy as sp
from scipy import stats
import pandas as pd

# import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns


arr = np.array


def mdot(*args):
    """Multi argument dot function.

    http://wiki.scipy.org/Cookbook/MultiDot

    >>> mdot(a, b, c, d)
    """
    return reduce(np.dot, args)


# ipython notebook magic
# %load_ext autoreload
# %autoreload 2
# %matplotlib notebook
%matplotlib inline
