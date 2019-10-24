import numpy as np
from sklearn.svm import LinearSVC
import time as tm
import random
from matplotlib import pyplot as plt


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


def randsplit(ratio,Z):
    np.random.shuffle(Z)
    y = Z[:,0]
    X = Z[:,1:]
    X_train = X[:int(ratio*(X.shape[0])),:]
    y_train = y[:int(ratio*(X.shape[0]))]
    X_validate = X[int(ratio*(X.shape[0])):,:]
    y_validate = y[int(ratio*(X.shape[0])):]
    return X_train,X_validate,y_train,y_validate


def SDCMD2(X,y,C,d):
    (n,) = y.shape
#     C = 1
    def getStepLength( grad, t ):
        return eta/(t+2)

    def hingelossSq(theta):
        w = theta[0:-1]
        b = theta[-1]

    #     print("Nai")
        hingesq = np.square(np.maximum(1-np.multiply((X.dot(w) + b), y), 0))
        return np.sum(hingesq)

    def ObjVal( theta ):
        w = theta[0:-1]
        b = theta[-1]
        Loss = hingelossSq(theta)
        return 0.5 * w.dot( w ) + C * Loss


    ##Takes an element i and gives the value of derivative w.r.t it
    def SqGrad(theta,i):
        w = theta[0:-1]
        b = theta[-1]
        n = y.size
        x = X[i,:]
        discriminant = 1 - ((x.dot( w ) + b) * y[i])
        g = 0
    #     print(x*np.maximum(discriminant,0)*y[i])
        if discriminant < 1:
            g = -1
        delb = C * y[i] * (-2) * np.maximum(discriminant,0)
        delw = w + C *(x * n * np.maximum(discriminant,0)) * y[i] * (-2)
        return np.append( delw, delb )
    # print(discriminant)
    # SqGrad(-1*np.ones(21),2)

    def getCyclicCoord( currentCoord ):
        if currentCoord >= n-1 or currentCoord < 0:
            return 0
        else:
            return (currentCoord + 1)%n

    def getRandCoord( currentCoord ):
        return random.randint( 0, n -1 )

    def getRandpermCoord( currentCoord ):
        global randperm, randpermInner
        if currentCoord < 0 or randpermInner >= n-1 or randpermInner < 0 :
            randpermInner = 0
            randperm = np.random.permutation( y.size )
            return randperm[randpermInner]
        else:
            randpermInner = randpermInner + 1
            return randperm[randpermInner]

    def doSDCM( getCoordFunc, init, horizon = 10 ):
        primalObjValSeries = np.zeros( (int(horizon/200),) )
        #     dualObjValSeries = np.zeros( (horizon,) )
        timeSeries = np.zeros( (int(horizon/200),) )
        totTime = 0
        # Initialize model as well as some bookkeeping variables
        alpha = init
        alphay = np.multiply( alpha, y )
        # Initialize the model vector using the equations relating primal and dual variables
        w = X.T.dot( alphay )
        # Recall that we are imagining here that the data points have one extra dimension of ones
        # This extra dimension plays the role of the bias in this case
        b = alpha.dot( y )
        # Calculate squared norms taking care that we are appending an extra dimension of ones
        normSq = np.square( np.linalg.norm( X, axis = 1 ) ) + 1
        # We have not made any choice of coordinate yet
        i = -1
        tic = tm.perf_counter()
        for t in range( horizon ):
            i = getCoordFunc( i )
            x = X[i,:]
        #         print(x.shape)
            # Find the unconstrained new optimal value of alpha_i
            newAlphai =  (1 + alpha[i]*normSq[i] - y[i] * (x.dot(w) + b)) / (normSq[i] + 0.5*C)
            # Make sure that the constraints are satisfied
        #         if newAlphai > C:
        #             newAlphai = C
            if newAlphai < 0:
                newAlphai = 0

            # Update the model vector and bias values
            # Takes only O(d) time to do so :)
            w = w + (newAlphai - alpha[i]) * y[i] * x
            b = b + (newAlphai - alpha[i]) * y[i]

            alpha[i] = newAlphai


            if t%200 == 0:
#                 print(t)
                toc = tm.perf_counter()
                totTime = totTime + (toc - tic)
#                 primalObjValSeries[int(t/200)] = ObjVal( np.append( w, b ) )
                tic = tm.perf_counter()
                        #         dualObjValSeries[t] = ObjValDual( alpha, w, b )
                timeSeries[int(t/200)] = totTime

        print( "nSV = ", np.sum( alpha > C/100 ), " out of ", y.size, "data points" )
        return (np.append( w, b ), primalObjValSeries, timeSeries)

#     d=20
    (theta_SCD, obj_P1, time_SCD) = doSDCM( getRandpermCoord, np.zeros( (n,) ), horizon = 600000 )
#     plt.figure(figsize =(6,6))
#     plt.plot( time_SCD, obj_P1, color = 'r', linestyle = '-', label = "SCD" )
#     plt.xlabel( "Elapsed time (sec)" )
#     plt.ylabel( "P1 Objective value" )
#     plt.legend()
#     plt.show()
#     print(min(obj_P1))
    print("Time elapsed = {} sec".format(time_SCD[-1]))
    return ObjVal(theta_SCD)

Z = np.loadtxt( "data" )
# Z = Z[0:2, :]
# Z[1,0] = 1
finalans = []
(X,_,y,_) = randsplit(1,Z)
(n,) = y.shape

darray = [13,14,15,16,17,18,19,20,21,22,23,24,25,26]
darray = np.array(darray)
finaltruevalues = []
for i in range(len(darray)):
    (X,_,y,_) = randsplit(1,Z)
    (n,) = y.shape
    print('Running for',i)
    D = darray[i]
    if(D > 20):
        X = np.hstack((X,X[:,np.random.choice(20,D-20,replace = False)]))
        print(X.shape)
    else:
        X = X[:,np.random.choice(20,D,replace = False)]
    X = np.hstack((X, np.ones((n, 1))))
    w = np.zeros(X.shape[1]+1)
    finalans.append(SDCMD2(X,y,1.0,D))

    y.reshape(y.shape[0],1)
    # print(y.shape, X.shape)
    finaltruevalues.append(checkoriginal(y,X,1.0))

print('Final values',finalans)
print('Values of d',darray)
plt.figure()
plt.scatter( darray,finaltruevalues, color = 'r', label = "Sklearn" )
plt.scatter( darray,finalans, color = 'g', label = "SDCM" )
plt.xlabel( "Value of d" )
plt.ylabel( "P1 objective value" )
plt.legend()
plt.show()