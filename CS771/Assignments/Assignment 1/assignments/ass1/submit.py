import numpy as np
import random as rnd
import time as tm

# You may define any new functions, variables, classes here
# For example, functions to calculate next coordinate or step length

################################
# Non Editable Region Starting #
################################
def solver( X, y, C, timeout, spacing ):
	(n, d) = X.shape
	t = 0
	totTime = 0

	# w is the normal vector and b is the bias
	# These are the variables that will get returned once timeout happens
	w = np.zeros( (d,) )
	b = 0
	w_run = np.zeros( (d,) )
	b_run = 0
	tic = tm.perf_counter()
################################
#  Non Editable Region Ending  #
################################

	eta = 0.00004
	B = 100
	i = -1
	theta = np.append(w, b)


	# You may reinitialize w, b to your liking here
	# You may also define new variables here e.g. eta, B etc

################################
# Non Editable Region Starting #
################################
	while True:
		t = t + 1
		if t % spacing == 0:
			toc = tm.perf_counter()
			totTime = totTime + (toc - tic)
			if totTime > timeout:
				return (w, b, totTime)
			else:
				tic = tm.perf_counter()
################################
#  Non Editable Region Ending  #
################################

		# Write all code to perform your method updates here within the infinite while loop
		# The infinite loop will terminate once timeout is reached
		# Do not try to bypass the timer check e.g. by using continue
		# It is very easy for us to detect such bypasses - severe penalties await

		# Please note that once timeout is reached, the code will simply return w, b
		# Thus, if you wish to return the average model (as we did for GD), you need to
		# make sure that w, b store the averages at all times
		# One way to do so is to define two new "running" variables w_run and b_run
		# Make all GD updates to w_run and b_run e.g. w_run = w_run - step * delw
		# Then use a running average formula to update w and b
		# w = (w * (t-1) + w_run)/t
		# b = (b * (t-1) + b_run)/t
		# This way, w and b will always store the average and can be returned at any time
		# w, b play the role of the "cumulative" variable in the lecture notebook
		# w_run, b_run play the rol e of the "theta" variable in the lecture notebook
		delta = getCSVMMBGrad( theta, X, y, B, C )
		theta = theta - getStepLength( eta, t, 0.9 ) * delta
		w_run = theta[0:-1]
		b_run = theta[-1]
		w = (w * (t-1) + w_run)/t
		b = (b * (t-1) + b_run)/t

	return (w, b, totTime) # This return statement will never be reached

def getRandCoord( currentCoord, n ):
	return rnd.randint( 0, n-1 )

def getCSVMMBGrad( theta, X, y, B, C):
    w = theta[0:-1]
    b = theta[-1]
    n = y.size
    if B <= n:
        samples = rnd.sample( range(0, n), B )
        X_ = X[samples,:]
        y_ = y[samples]
    else:
        X_ = X
        y_ = y
    discriminant = 1 - np.multiply( (X_.dot( w ) + b), y_ )
    delb = C * np.maximum(discriminant,0).dot( y_ ) * (-2) * n/B
    delw = w + C * n/B * (X_.T * np.maximum(discriminant,0)).dot( y_ )* (-2)
    return np.append( delw, delb )

def getStepLength(eta, t ,power = 0.5):
    return eta/pow(t,0.5)
