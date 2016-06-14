## toolkit for generalized local area modeling
##
## general idea: rather than using a hyperplane-of-best-fit for modeling,
## use a series of simpler local models based on clustering and/or other form of
## locality analysis on a complicated high-dimensional dataset
##
## reasoning: save computation (hopefully) vs. very complex / hard-to-fit
## hyperplanes; local models may also perform better in general if one does not
## know anything about the underlying causality behind data relationships -- a
## universal model / single hyperplane may not in fact describe the
## relationships between dimensions well -- causality may vary locally (of
## course, it may not, so performance should be tested vs. single models
## as well)

## imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from __future__ import division

## test block of data to use for clustering / keypoint generation
np.random.seed(100)
tester = pd.DataFrame({'x1' : np.random.randn(100), 'x2' : np.random.randn(100) * 2})

# function to map the area into "localities" which will be indivisually used
# to train local models; this is just an ID for datapoints that are "near"
# to each other in whatever sense works best
def map_area(dataset, method = 'keypoints'):
    '''
    Parameters
    ==========

    dataset : expects pandas dataframe object with 1 row per observation
    method : how to map the area (start with custom keypoint algo)

    Internal vars
    =============

    df : local copy of dataset to manipulate and return
    DIMS : dimensions along which to generate keypoint data, etc.

    TODO:
    =====

    add other methods (clustering - try kmeans for speed, and
        affinity propagation for robustness)
    try to coerce to df if passed some other object
    error handling for bad input
    error handling for other things
    '''
    df = dataset
    DIMS = len(dataset.columns)
    df['LOCALITY'] = np.zeros(len(df))

    ## do analysis - try clustering algos (canned), or some more complex thing

    return df
