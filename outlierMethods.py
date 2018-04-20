import pandas as pd
import matplotlib.pyplot as plt

directory = '/home/doltsinis/net_folders/Monsoon/ALDK Electrolysis Optimization Scenario/'
sampleData = pd.read_csv(directory + 'aldk_tab_1mn.csv', sep=';', nrows=10000)


def MAD(data, windowSize=100):
    outlierIndex = []

    for col in data.columns:
        for i in range(0, len(data) - windowSize):
            try:
                windowsMedian = data[col].iloc[i: i + windowSize - 1].median()  # if data median can be calculated
            except Exception:
                print('exception on : ', col)
            else:
                MAD = data[col].iloc[i: i + windowSize - 1].mad()
                if (windowsMedian + 3 * MAD < data[col].iloc[i + windowSize]) or (
                        windowsMedian - 3 * MAD > data[col].iloc[i + windowSize]):
                    outlierIndex.append(i)
                    #print(windowsMedian - 3 * MAD, data[col].iloc[i + windowSize], windowsMedian + 3 * MAD)
                    #print('outlier in ',col , ', position : ', i)
    return outlierIndex


outliers = MAD(sampleData.iloc[:, 5:6])
print(len(outliers))