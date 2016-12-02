from sklearn import metrics
import pandas as pd
prediction = pd.read_csv("D:/MS/ALDA CSC 522/Project/SVMPrediction.csv", header=0, delimiter=",", quoting=3)
print(prediction.shape)

print(prediction.columns.values)

total = prediction["Original classification"].size
correct=0
print("Total number of Webpages:", total)

for i in range( 0, total):
    if prediction["Original classification"][i]==prediction["Prediction"][i]:
        correct=correct+1

print("Number of Webpages Correctly classified :",correct)

print("Accuracy: ",correct/total*100, "%")

print(metrics.accuracy_score(prediction["Original classification"],prediction["Prediction"]))
print(metrics.classification_report(prediction["Original classification"],prediction["Prediction"],digits=4))
print(metrics.confusion_matrix(prediction["Original classification"],prediction["Prediction"]))