import numpy as np
from matplotlib import pyplot as plt
import time as tm
import numpy as np
import random

Z = np.loadtxt( "data" )


def randsplit(ratio,Z):
    np.random.shuffle(Z)
def randsplit(ratio,Z):
    np.random.shuffle(Z)
    y = Z[:,0]
    X = Z[:,1:]
    X_train = X[:int(ratio*(X.shape[0])),:]
    y_train = y[:int(ratio*(X.shape[0]))]
    X_validate = X[int(ratio*(X.shape[0])):,:]
    y_validate = y[int(ratio*(X.shape[0])):]
    return X_train,X_validate,y_train,y_validate

def StratifiedSplit(ratio, Z):
    np.random.shuffle(Z)
    y = Z[:,0]
    X = Z[:,1:]
    Z_true = Z[y == 1]
    Z_false = Z[y == -1]
    X1_train,X1_validate,y1_train,y1_validate = randsplit(ratio,Z_true)
    X2_train,X2_validate,y2_train,y2_validate = randsplit(ratio,Z_false)
    X_train = np.concatenate((X1_train,X2_train))
    y_train = np.concatenate((y1_train,y2_train))
    X_validate = np.concatenate((X1_validate,X2_validate))
    y_validate = np.concatenate((y1_validate,y2_validate))
    return X_train,X_validate,y_train,y_validate
def getStepLength( grad, t , power = 0.25):
     return eta/pow(t+1, power)


    y = Z[:,0]
    X = Z[:,1:]
    X_train = X[:int(ratio*(X.shape[0])),:]
    y_train = y[:int(ratio*(X.shape[0]))]
    X_validate = X[int(ratio*(X.shape[0])):,:]
    y_validate = y[int(ratio*(X.shape[0])):]
    return X_train,X_validate,y_train,y_validate

def CSVMgradient( theta ):
    w = theta[0:-1]
    b = theta[-1]
    discriminant = 1 - np.multiply( (X.dot( w ) + b), y )
    delb = C * np.maximum(discriminant,0).dot( y ) * (-2)
    delw = w + C * (X.T * np.maximum(discriminant,0)).dot( y ) * (-2)
    return np.append( delw, delb )

def CDGradient(w,y,X,C,j):
    Discriminant = 1 - np.multiply( (X.dot( w )), y )
    return (w[j] - 2*C*(np.sum(np.maximum(Discriminant,0)*y*X[:,j])))


eta = .0006
C = 1
(X,_,y,_) = randsplit(1,Z)
(n,) = y.shape
X = np.hstack((X, np.ones((n, 1))))
w = np.zeros(X.shape[1]+1)
d=20
randperm = np.random.permutation( y.size )
randpermInner = -1


def getStepLength( grad, t , power = 0.25):
     return eta/pow(t+1, power)


def hingelossSq(theta):
    w = theta
    hingesq = np.square(np.maximum(1-np.multiply((X.dot(w)), y), 0))
    return np.sum(hingesq)

def ObjVal( theta ):
    w = theta[0:-1]
    b = theta[-1]
    Loss = hingelossSq(theta)
    return 0.5 * w.dot( w ) + C * Loss

def getCyclicCoord( currentCoord ):
    if currentCoord >= d or currentCoord < 0:
        return 0
    else:
        return currentCoord + 1

def getRandCoord( currentCoord ):
    return random.randint( 0, d )

def getRandpermCoord( currentCoord ):
    global randperm, randpermInner
    if randpermInner >= d or randpermInner < 0 or currentCoord < 0:
        randpermInner = 0
        randperm = np.random.permutation( d )
        return randperm[randpermInner]
    else:
        randpermInner = randpermInner + 1
        return randperm[randpermInner]

def Coorinate_descent( gradFunc, CoordFunc, stepFunc, init, w, horizon = 10):
    objValSeries = np.zeros( (horizon,) )
    timeSeries = np.zeros( (horizon,) )
    totTime = 0
    cumulative = init
    w=init
    j=-1
    for t in range( horizon ):
        tic = tm.perf_counter()
        j = CoordFunc( j )
        delta = CDGradient(w,y,X,C,j)
        w[j] = w[j] - stepFunc(delta,t+1,0.25)*delta
        toc = tm.perf_counter()
        totTime = totTime + (toc - tic)
        objValSeries[t] = ObjVal(w)
        timeSeries[t] = totTime
        if(t % 500 == 0):
            print(t)

    return (w, objValSeries, timeSeries)

def CDP1():

  (theta_SGD, obj_SGD, time_SGD) = Coorinate_descent( CDGradient, getRandCoord, getStepLength, np.random.random_sample( (d+1,) ), w, horizon = 50000)
  plt.figure()
  plt.plot( time_SGD, obj_SGD, color = 'r', linestyle = '-', label = "SGD" )
  plt.xlabel( "Elapsed time (sec)" )
  plt.ylabel( "P1 Objective value" )
  plt.legend()
  print(ObjVal(theta_SGD), min(obj_SGD))
  plt.show()

CDP1()
