# -*- coding: utf-8 -*-
'''
# author : Enes Çavuş
# date   : last update - August 19 2021
# subject: Usage of Docker/DockerFile for Machine Learning Projects
'''
# importing base modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('dark_background')
import warnings
warnings.filterwarnings('ignore')

# sklearn all preprocessing, visualization, analysis and traning modules at once
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.utils import shuffle
from sklearn.svm import LinearSVC,SVC
from sklearn.metrics import plot_confusion_matrix, classification_report, plot_roc_curve, accuracy_score
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import plot_confusion_matrix, classification_report, plot_roc_curve, accuracy_score
import os
DIRECTORY_PATH = "/"
DATASET_PATH = "dataset/Dataset"

print("\nAll libraries loaded successfully!\n")

seperated_dataset_files = os.listdir(DATASET_PATH)
#print(len(seperated_dataset_files))
currtent_file = seperated_dataset_files[0]
#print(DATASET_PATH + "/" + currtent_file)

df_list = list()
for data in range(len(seperated_dataset_files)-1):
    path = DATASET_PATH + "/" + seperated_dataset_files[data]
    df = pd.read_csv(path,
                 header=None,
                 names=['time', 'frontal_axis','vertical_axis', 'lateral_axis','antennaID', 'signalStrength','phase', 'Frequency','activity'])
    df_list.append(df)
# print(df_list)
combined_data = pd.concat(df_list,ignore_index=True, sort=False)
print("Dataset Loaded Successfully - > \n")
print(combined_data.head(2))
df = combined_data.copy()

print("Categorical Columns are examining")
df.select_dtypes(include=['object',"category"]).columns

for column in df.select_dtypes(include=['object',"category"]).columns:
    df[column] = pd.to_numeric(df[column],errors="coerce")
print(df.info())
df.activity.value_counts()

print("Dropping unnecessary columns once !!! ")
df.drop(columns=["lateral_axis","phase","Frequency","signalStrength","time","antennaID"],inplace=True)
print("Dropped Successfully")

corr = df.corr()
print("This is Correlation ->> ")
print(corr["activity"].sort_values(ascending=False))

df = df.reset_index()
df = shuffle(df)

np.where(np.isnan(df))
df.fillna(df.mean(), inplace=True)
np.where(np.isnan(df))
print("NaN values handled Successfuly")
print("DownSampling...")
downsample_df = df[:10000]

X = downsample_df.drop(columns=["activity"],axis=1)
y = downsample_df["activity"]

scaler = StandardScaler()
X = scaler.fit_transform(X)

encoder = LabelEncoder()
y = encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

svc = SVC(verbose=0)
svc.fit(X_train,y_train)

y_pred = svc.predict(X_test)
print(accuracy_score(y_test, y_pred))
# print prediction results
predictions = svc.predict(X_test)
print(classification_report(y_test, predictions))

import joblib
 
# Save the model as a pickle in a file
joblib.dump(svc, 'savedModels/savedmodel.pkl')
print("Model Saved into SavedModels Folder...DONE")

savedMlModel = joblib.load('savedModels/savedmodel.pkl')
 
# Use the loaded model to make predictions
savedMlModel.predict(X_test)
print("Saved Model Tested - Succesful")


print("All steps are done.. This is just a quick machine learning project for Docker practice.")
print("If you see this message when you use the original docker image I created then it means it works perfectly. ")

# Enes Çavuş - 2021 August - Docker Practices - DONE