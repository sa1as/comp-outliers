import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import LocalOutlierFactor
import numpy as np

directory = '/home/doltsinis/net_folders/Monsoon/ALDK Electrolysis Optimization Scenario/'
sampleData = pd.read_csv(directory + 'aldk_tab_1mn.csv', sep=';', nrows=2000)


def MAD(data, features=[3, 5], windowSize=200, noplots=False):
    ''' Median Absolute Deviation (MAD) outlier detection function
    the function calculates outliers based on the MAD value of every
    new data point compared to the MAD values of the previous window.

    Rule: windowsMedian + 3 * MAD < newdatapoint < windowsMedian - 3 * MAD
    windowSize: training set size

    '''

    outlierIndex = []

    for col in data.columns[features]:  # check in every data column
        for i in range(0, len(data) - windowSize):  # check data of a time series
            try:  # try if data median can be calculated (avoids non numerical data)
                windowsMedian = data[col].iloc[i: i + windowSize - 1].median()  # calculate window median for training
            except Exception:
                print('exception on : ', col)
            else:
                MAD = data[col].iloc[i: i + windowSize - 1].mad() # calculate MAD of a window
                if (windowsMedian + 3 * MAD < data[col].iloc[i + windowSize]) or (  # test next value, after the window
                        windowsMedian - 3 * MAD > data[col].iloc[i + windowSize]):
                    outlierIndex.append(i + windowSize)

        if noplots == True:  # draw data and outlier plots
            plt.figure()
            plt.plot(sampleData[col])
            plt.scatter(outlierIndex, sampleData[col].iloc[outlierIndex], c='r')
            plt.legend(["Time series", "outliers"], loc="upper left")
            plt.show()

    print('*********** MAD ***********' )
    print('There where', len(outlierIndex), 'outliers found in', len(data), 'data points')
    print('Outlier in positions :', outlierIndex)
    print(" ")

    return outlierIndex


def lof(data, features=[3, 5], neighbours=200, trainingSize = 0.1, noplots=False):  # parametarize according to desired features
    ''' http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor.fit_predict
    add functionality, define training size and test to the rest of the data set
    this function splits the time series and runs training on part of the data defined by trainingSize
    It tests on the rest of the data set. Retraining can be done using fit
    '''

    fordetection = data.iloc[:, features].as_matrix()

    clf = LocalOutlierFactor(n_neighbors=neighbours, contamination=0.05) #The amount of contamination of the data set, i.e. the proportion of outliers in the data set. When fitting this is used to define the threshold on the decision function.
    pred = clf.fit_predict(fordetection)
    outlierIndex = np.where(pred == -1)

    print('*********** LOCAL OUTLIER FACTOR ***********')
    print('There where', len(list(outlierIndex[0])), 'outliers found in', len(data), 'data points')
    print('Outlier in positions :', list(outlierIndex[0]))

    if noplots == True:  # draw data and outlier plots

        plt.figure()
        plt.scatter(fordetection[:, 0][pred == 1], fordetection[:, 1][pred == 1], c='white', edgecolors='k')
        plt.scatter(fordetection[:, 0][pred == -1], fordetection[:, 1][pred == -1], c='red', edgecolors='k')
        plt.legend(["Normal data", "Outliers"])
        plt.show(block=False)

        plt.figure()
        plt.plot(fordetection)
        plt.scatter(outlierIndex, fordetection[:, 0][pred == -1], c='r')
        plt.scatter(outlierIndex, fordetection[:, 1][pred == -1], c='b')
        plt.legend(["feature One", "feature Two"])
        plt.show()

    print('maximum outlier factor', clf.negative_outlier_factor_.max(), ', minimum outlier factor', clf.negative_outlier_factor_.min())
    print('')

    return 0

def oneSVM(data, features=[3, 5]):
    ''' comments '''

    from sklearn import svm

    dataForTraining = data.iloc[0:1000, features].values
    dataForTesting = data.iloc[1001:2000, features].as_matrix()
    print(dataForTraining.shape)

    clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
    clf.fit(dataForTraining)
    y_pred_train = clf.predict(dataForTraining)
    y_pred_test = clf.predict(dataForTesting)

#    #y_pred_outliers = clf.predict(X_outliers)
    print('*********** One Class SVM ***********')
    print(y_pred_train[y_pred_train == -1].size, 'οutliers out of', len(dataForTraining), 'in the training set')
    print(y_pred_test[y_pred_test == -1].size, 'οutliers out of', len(dataForTesting), 'in the testing set')
#    n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
    print('')

    return 0


MAD(sampleData, noplots=True)
lof(sampleData, features=[3, 5, 7, 9])
oneSVM(sampleData, features=[3, 5])
