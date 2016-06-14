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


# function to generate keypoints; to be used in map_area() below
def gen_keypoints(dataset):
    '''
    accept pandas df; try to coerce if not and throw error if unable
    examine some stats around each dimension
    need to consider what format is acceptable for the return --
        list of ndim tuples, of whatever length is sufficient to cover the area?
    '''
    keypoints = []

    return keypoints


# function to map the area into "localities" which will be indivisually used
# to train local models; this is just an ID for datapoints that are "near"
# to each other in whatever sense works best
def map_area(dataset, method = 'basic_keypoints'):
    '''
    Parameters
    ==========

    dataset : expects pandas dataframe object with 1 row per observation
    method : how to map the area (start with custom keypoint algo)
        allowable methods are 'keypoints', ...

    Internal vars
    =============

    df : local copy of dataset to manipulate and return
    DIMS : dimensions along which to generate keypoint data, etc.

    TODO:
    =====

    add other locality methods (clustering - try kmeans for speed, and
        affinity propagation for robustness)
    add method to list allowable locality methods
    try to coerce to df if passed some other object
    error handling for bad input
    error handling for other things
    '''
    allowable_methods = ['basic_keypoints']
    df = dataset
    DIMS = len(dataset.columns)
    df['LOCALITY'] = np.zeros(len(df))

    if method not in allowable_methods:
        print('Unrecognized method; use default or refer to docstring')
        return

    elif method == 'basic_keypoints':
        # do things
        # this is more about distribution of points to the "best" places, rather
        # than localities as such -- localities would be centered around
        # keypoints and should have overlapping coverage of the whole dataset
        # new / unrecognized values can be clustered to closet keypoint and
        # tested against the local model built around that keypoint

        # as such this is basically a 2-step process:
        # 1) generate keypoints using "terrain similarity" in certain regions
        #       of the existing dataset
        # 2) define the boundaries of the localities around each keypoint
        #
        # these may need to be divided into 2 functions for better reuse;
        # if so, "method" of "keypoints" should be renamed to something else
        # and any / all methods that require keypoints can use them

        # part 1:
        kps = gen_keypoints(df.drop('LOCALITY', 1))

        # part 2:
        # using the keypoints, define some areas in nD space around them
        # assign each point to a locality in df under LOCALITY
        # pass output (to new function I guess?) to use each locality as
        # the basis for modeling

        return df


# function to do some useful modeling with the locality data
def build_local_models(dataset):
    '''
    things to do here:
    use the labeled data with locality per observation
    based on points within each locality (just an index), try a bunch of models
    analyze the data within each locality to check properties suggesting
        what models may fit best, and only try those
        (or, to start, just try a small set for each locality)
    return a dict of trained models per locality
    then need function to map a new / unobserved input into the correct locality
        (based on closest euclidean keypoint, e.g. to start, then maybe
        something more sophisticated)
        once mapped, that new observation can be predicted by the LOCAL models
            (which is supposed to be the best fit for its local terrain)
    '''
    output = {'TBD' : 'some_model'}

    return output
