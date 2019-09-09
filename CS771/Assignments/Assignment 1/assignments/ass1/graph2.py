
import numpy as np
from sklearn.svm import LinearSVC
import time as tm
import random
from matplotlib import pyplot as plt


def randsplit(ratio,Z):
    np.random.shuffle(Z)
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


Z = np.loadtxt( "data" )

eta = 0.0006
C = 1
(X,_,y,_) = randsplit(1,Z)
(n,) = y.shape
X = np.hstack((X, np.ones((n, 1))))
w = np.zeros(X.shape[1]+1)
d=20
randperm = np.random.permutation( y.size )
randpermInner = -1

def CDGradient(w,y,X,C,j):
    Discriminant = 1 - np.multiply( (X.dot( w )), y )
    return (w[j] - 2*C*(np.sum(np.maximum(Discriminant,0)*y*X[:,j])))



def checkoriginal(Z,c):
    y = Z[:,0]
    X = Z[:,1:]
    clf = LinearSVC(C=c,penalty = 'l2',loss = 'squared_hinge')
    clf.fit(X,y)
    final = np.matmul(X,clf.coef_.T) + clf.intercept_
    y.reshape(y.shape[0],1)
    for i in range(y.shape[0]):
        final[i] = y[i] * final[i]
    final = 1-final
    for i in range(final.shape[0]):
        if(final[i] <= 0):
            final[i] = 0
    for i in range(final.shape[0]):
        final[i] = final[i] * final[i]
    finalans = (np.sum(final)+0.5*np.matmul(clf.coef_,clf.coef_.T))
    return finalans


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


def Coorinate_descent( gradFunc, CoordFunc, stepFunc, init, w,X,y,C, horizon = 10):
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
        w[j] = w[j] - stepFunc(delta,t+1)*delta
        toc = tm.perf_counter()
        totTime = totTime + (toc - tic)
        objValSeries[t] = ObjVal(w)
        timeSeries[t] = totTime

    return (w, objValSeries, timeSeries)

def CDP1(X,y,C):

  (theta_SGD, obj_SGD, time_SGD) = Coorinate_descent( CDGradient, getRandCoord, getStepLength, np.random.random_sample( (d+1,) ), w,X,y,C ,horizon = 10000)
  # plt.figure()
  # plt.plot( time_SGD, obj_SGD, color = 'r', linestyle = '-', label = "SGD" )
  # plt.xlabel( "Elapsed time (sec)" )
  # plt.ylabel( "P1 Objective value" )
  # plt.legend()
  # print(ObjVal(theta_SGD), min(obj_SGD))4
  return ObjVal(theta_SGD)
  #plt.show()
finaltruevalues = []

numc = np.random.random_sample((50,))
# numc = numc/2 + 1
finalval = []
for i in range(len(numc)):
    print('Running for ' ,i)
    finalval.append(CDP1(X,y,numc[i]))
    finaltruevalues.append(checkoriginal(Z,numc[i]))
#
print('Final values',finalval)
print('Values of C',numc)
plt.figure()
plt.scatter( numc,finaltruevalues, color = 'r', label = "Sklearn" )
plt.scatter( numc,finalval, color = 'g', label = "Coordinate Descent" )
plt.xlabel( "Value of C" )
plt.ylabel( "P1 objective value" )
plt.legend()
plt.show()

#
# Z = np.loadtxt( "data" )
# finalans = []
# (X,_,y,_) = randsplit(1,Z)
# (n,) = y.shape
# X = np.hstack((X, np.ones((n, 1))))
# darray = {13,14,15,16,17,18,19,20,21,22,23,24,25,26}
# for i in range(len(darray)):
#     D = darray[i]
#     if(D > 20):
#         X = np.append(X,X[:,np.random.choice(20,D-20,replace = False)])
#     else:
#         X = X[:,np.random.choice.choice(20,D,replace = False)]
#     finalans.append()
