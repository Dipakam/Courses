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

def getStepLength( eta, t , power = 0.25):
     return eta/pow(t+1, power)


Z = np.loadtxt( "data" )

eta = 0.0006
C = 1
(X,_,y,_) = randsplit(1,Z)
(n,) = y.shape

randperm = np.random.permutation( y.size )
randpermInner = -1

def CDGradient(w,y,X,C,j):
    Discriminant = 1 - np.multiply( (X.dot( w )), y )
    return (w[j] - 2*C*(np.sum(np.maximum(Discriminant,0)*y*X[:,j])))



def checkoriginal(y,X,c):
    # y = Z[:,0]
    # X = Z[:,1:]
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

def getRandCoord( currentCoord ,d):
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


def Coorinate_descent( gradFunc, CoordFunc, stepFunc, init, w,X,y,C,d,eta, horizon = 10):
    objValSeries = np.zeros( (horizon,) )
    timeSeries = np.zeros( (horizon,) )
    totTime = 0
    cumulative = init
    w=init
    j=-1
    for t in range( horizon ):
        tic = tm.perf_counter()
        j = CoordFunc( j ,d)
        delta = CDGradient(w,y,X,C,j)
        w[j] = w[j] - stepFunc(eta,t+1)*delta
        toc = tm.perf_counter()
        totTime = totTime + (toc - tic)
        objValSeries[t] = ObjVal(w)
        timeSeries[t] = totTime

    return (w, objValSeries, timeSeries)

def CDP1(X,y,C,d, eta):

  (theta_SGD, obj_SGD, time_SGD) = Coorinate_descent( CDGradient, getRandCoord, getStepLength, np.random.random_sample( (d+1,) ), w,X,y,C,d ,eta, horizon = 10000)
  return ObjVal(theta_SGD)


Z = np.loadtxt( "data" )
# Z = Z[0:2, :]
# Z[1,0] = 1
finalans = []
(X,_,y,_) = randsplit(1,Z)
(n,) = y.shape
D = 20
num_eta = np.random.random_sample((50,))
num_eta = num_eta*0.003
finaltruevalues = []
for i in range(len(num_eta)):
    (X,_,y,_) = randsplit(1,Z)
    (n,) = y.shape
    print('Running for',i)
    if(D > 20):
        X = np.hstack((X,X[:,np.random.choice(20,D-20,replace = False)]))
        print(X.shape)
    else:
        X = X[:,np.random.choice(20,D,replace = False)]
    X = np.hstack((X, np.ones((n, 1))))
    w = np.zeros(X.shape[1]+1)
    finalans.append(CDP1(X,y,1.0,20, num_eta[i]))

    y.reshape(y.shape[0],1)
    # print(y.shape, X.shape)
    #finaltruevalues.append(checkoriginal(y,X,1.0))

print('Final values',finalans)
print('Values of eta',eta)
plt.figure()
#plt.scatter( eta,finaltruevalues, color = 'r', label = "Sklearn" )
plt.scatter( eta,finalans, color = 'g', label = "Coordinate Descent" )
plt.xlabel( "Value of eta" )
plt.ylabel( "P1 objective value" )
plt.legend()
plt.show()
