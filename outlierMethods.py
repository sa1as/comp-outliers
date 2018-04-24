import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import LocalOutlierFactor
from sklearn import svm
import numpy as np


directoryPoc2 = '/home/doltsinis/net_folders/Monsoon/Alluminium data for classification/'
directoryPoc4 = '/home/doltsinis/net_folders/Monsoon/ALDK Electrolysis Optimization Scenario/'
sampleData = pd.read_csv(directoryPoc2 + 'full_POC2_clean_with_stops.csv', sep=';', nrows=2000)


def MAD(data, features=[3, 5], windowSize=200, plots=False):
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

        if plots == True:  # draw data and outlier plots
            plt.figure()
            plt.plot(sampleData[col])
            plt.scatter(outlierIndex, sampleData[col].iloc[outlierIndex], c='r')
            plt.legend(["Time series", "outliers"], loc="upper left")
            plt.title('Time Series Along with MAD outliers')
            plt.show()

    print('*********** MAD ***********' )
    print('There where', len(outlierIndex), 'outliers found in', len(data), 'data points')
    print('Outlier in positions :', outlierIndex)
    print(" ")

    return outlierIndex


def lof(data, features=[3, 5], neighbours=200, trainingSize = 0.1, plots=False):  # parametarize according to desired features
    ''' http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor.fit_predict
    add functionality, define training size and test to the rest of the data set
    this function splits the time series and runs training on part of the data defined by trainingSize
    It tests on the rest of the data set. Retraining can be done using fit
    '''

    fordetection = data.iloc[:, features].as_matrix()

    clf = LocalOutlierFactor(n_neighbors=neighbours, contamination=0.05) #The amount of contamination of the data set, i.e. the proportion of outliers in the data set. When fitting this is used to define the threshold on the decision function.
    clf.fit(fordetection)
    pred = clf.fit_predict(fordetection)
    outlierIndex = np.where(pred == -1)

    print('*********** LOCAL OUTLIER FACTOR ***********')
    print('There where', len(list(outlierIndex[0])), 'outliers found in', len(data), 'data points')
    print('Outlier in positions :', list(outlierIndex[0]))

    if plots == True:  # draw data and outlier plots

        # plot scatter of data points / only first and second feature
        plt.figure()
        plt.scatter(fordetection[:, 0][pred == 1], fordetection[:, 1][pred == 1], c='white', edgecolors='k')
        plt.scatter(fordetection[:, 0][pred == -1], fordetection[:, 1][pred == -1], c='red', edgecolors='k')
        plt.legend(["Normal data", "Outliers"])
        plt.title('Scatter plot of LOF outliers and normal data')
        plt.show(block=False)

        # plot time series along with detected outliers
        plt.figure()
        plt.plot(fordetection)
        legendVector = []

        for num in range(fordetection.shape[1]):  # place outlier marks on each time series
            plt.scatter(outlierIndex, fordetection[:, num][pred == -1], c='b')
            legendVector.append('feature ' + str(num + 1))

        plt.legend(legendVector)
        plt.title('Time Series Along with LOF outliers')
        plt.show()

    print('maximum outlier factor', clf.negative_outlier_factor_.max(), ', minimum outlier factor', clf.negative_outlier_factor_.min())
    print('')

    return 0

def oneSVM(data, trainSplit=0.7, features=[3, 5], plots=False):
    ''' comments
    ToDo: define train and split sets
    '''

    #  pre-process data
    size = len(data)
    data = data.sample(size)
    dataForTraining = data.iloc[0:int(trainSplit*size), features].values
    dataForTesting = data.iloc[int(trainSplit*size):-1, features].values

    #  train and test the SVM model
    clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)  # use clf (model object) for predictions
    clf.fit(dataForTraining)  # train the model
    y_pred_train = clf.predict(dataForTraining)
    y_pred_test = clf.predict(dataForTesting)  # use predict for new data set

    print('*********** One Class SVM ***********')
    print(y_pred_train[y_pred_train == -1].size, 'οutliers out of', len(dataForTraining), 'in the training set')
    print(y_pred_test[y_pred_test == -1].size, 'οutliers out of', len(dataForTesting), 'in the testing set')
    print('')

    if plots == True:  # draw data and outlier plots

        # plot time series along with detected outliers
        plt.figure()
        plt.plot(fordetection)
        legendVector = []

        for num in range(fordetection.shape[1]):  # place outlier marks on each time series
            plt.scatter(outlierIndex, fordetection[:, num][pred == -1], c='b')
            legendVector.append('feature ' + str(num + 1))

        plt.legend(legendVector)
        plt.title('Time Series Along with LOF outliers')
        plt.show()

    return 0


MAD(sampleData, plots=True)
lof(sampleData, features=[3, 5, 7, 9], plots=True)
oneSVM(sampleData, features=[3, 5])
