#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:32:12 2019

@author: desir
"""

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectFromModel

#designate input file
#input_file = "../pain/MLpain_icv_control_clean_old.csv"
input_file = "MLpain_old_vol_icvcontrol.csv"

#pandas read input csv
dataset = pd.read_csv(input_file, header = 0,  sep=',')

dataset.shape

dataset.describe()

dataset.isnull().any()

dataset = dataset.fillna(method='ffill')

'''
dataset.plot(x='Chronological_Age', y='mri_GCPS_Disability_Score', style='o')  
plt.title('Chronological Age vs GCPS Disability Score')  
plt.xlabel('Chronological Age')  
plt.ylabel('GCPS Disability Score')  
plt.show()

plt.figure(figsize=(15,10))
plt.tight_layout()
seabornInstance.distplot(dataset['mri_pain_duration'])
'''

#select data
X = dataset[['Left_Cerebellum_White_Matter', 'Left_Cerebellum_Cortex', 'Left_Thalamus_Proper', 'Left_Caudate', 'Left_Putamen', 'Left_Pallidum', 
             'Left_Hippocampus', 'Left_Amygdala', 'Left_Accumbens_area', 'Left_VentralDC', 'Left_vessel', 'Left_choroid_plexus', 
             'Brain_Stem', 'Right_Cerebellum_White_Matter', 'Right_Cerebellum_Cortex', 'Right_Thalamus_Proper', 'Right_Caudate', 
             'Right_Putamen', 'Right_Pallidum', 'Right_Hippocampus', 'Right_Amygdala', 'Right_Accumbens_area', 'Right_VentralDC', 
             'Right_vessel', 'Right_choroid_plexus', 'Optic_Chiasm', 'CC_Posterior', 'CC_Mid_Posterior', 'CC_Central', 'CC_Mid_Anterior', 
             'CC_Anterior', 'lh_bankssts_volume', 'lh_caudalanteriorcingulate_volume', 'lh_caudalmiddlefrontal_volume', 'lh_cuneus_volume', 
             'lh_entorhinal_volume', 'lh_fusiform_volume', 'lh_inferiorparietal_volume', 'lh_inferiortemporal_volume', 
             'lh_isthmuscingulate_volume', 'lh_lateraloccipital_volume', 'lh_lateralorbitofrontal_volume', 'lh_lingual_volume', 
             'lh_medialorbitofrontal_volume', 'lh_middletemporal_volume', 'lh_parahippocampal_volume', 'lh_paracentral_volume', 
             'lh_parsopercularis_volume', 'lh_parsorbitalis_volume', 'lh_parstriangularis_volume', 'lh_pericalcarine_volume', 
             'lh_postcentral_volume', 'lh_posteriorcingulate_volume', 'lh_precentral_volume', 'lh_precuneus_volume', 
             'lh_rostralanteriorcingulate_volume', 'lh_rostralmiddlefrontal_volume', 'lh_superiorfrontal_volume', 
             'lh_superiorparietal_volume', 'lh_superiortemporal_volume', 'lh_supramarginal_volume', 'lh_frontalpole_volume', 
             'lh_temporalpole_volume', 'lh_transversetemporal_volume', 'lh_insula_volume', 'rh_bankssts_volume', 
             'rh_caudalanteriorcingulate_volume', 'rh_caudalmiddlefrontal_volume', 'rh_cuneus_volume', 'rh_entorhinal_volume', 
             'rh_fusiform_volume', 'rh_inferiorparietal_volume', 'rh_inferiortemporal_volume', 'rh_isthmuscingulate_volume', 
             'rh_lateraloccipital_volume', 'rh_lateralorbitofrontal_volume', 'rh_lingual_volume', 'rh_medialorbitofrontal_volume', 
             'rh_middletemporal_volume', 'rh_parahippocampal_volume', 'rh_paracentral_volume', 'rh_parsopercularis_volume', 
             'rh_parsorbitalis_volume', 'rh_parstriangularis_volume', 'rh_pericalcarine_volume', 'rh_postcentral_volume', 
             'rh_posteriorcingulate_volume', 'rh_precentral_volume', 'rh_precuneus_volume', 'rh_rostralanteriorcingulate_volume', 
             'rh_rostralmiddlefrontal_volume', 'rh_superiorfrontal_volume', 'rh_superiorparietal_volume', 'rh_superiortemporal_volume', 
             'rh_supramarginal_volume', 'rh_frontalpole_volume', 'rh_temporalpole_volume', 'rh_transversetemporal_volume', 
             'rh_insula_volume', 'wm_lh_bankssts', 'wm_lh_caudalanteriorcingulate', 'wm_lh_caudalmiddlefrontal', 'wm_lh_cuneus', 
             'wm_lh_entorhinal', 'wm_lh_fusiform', 'wm_lh_inferiorparietal', 'wm_lh_inferiortemporal', 'wm_lh_isthmuscingulate', 
             'wm_lh_lateraloccipital', 'wm_lh_lateralorbitofrontal', 'wm_lh_lingual', 'wm_lh_medialorbitofrontal', 'wm_lh_middletemporal', 
             'wm_lh_parahippocampal', 'wm_lh_paracentral', 'wm_lh_parsopercularis', 'wm_lh_parsorbitalis', 'wm_lh_parstriangularis', 
             'wm_lh_pericalcarine', 'wm_lh_postcentral', 'wm_lh_posteriorcingulate', 'wm_lh_precentral', 'wm_lh_precuneus', 
             'wm_lh_rostralanteriorcingulate', 'wm_lh_rostralmiddlefrontal', 'wm_lh_superiorfrontal', 'wm_lh_superiorparietal', 
             'wm_lh_superiortemporal', 'wm_lh_supramarginal', 'wm_lh_frontalpole', 'wm_lh_temporalpole', 'wm_lh_transversetemporal', 
             'wm_lh_insula', 'wm_rh_bankssts', 'wm_rh_caudalanteriorcingulate', 'wm_rh_caudalmiddlefrontal', 'wm_rh_cuneus', 
             'wm_rh_entorhinal', 'wm_rh_fusiform', 'wm_rh_inferiorparietal', 'wm_rh_inferiortemporal', 'wm_rh_isthmuscingulate', 
             'wm_rh_lateraloccipital', 'wm_rh_lateralorbitofrontal', 'wm_rh_lingual', 'wm_rh_medialorbitofrontal', 'wm_rh_middletemporal', 
             'wm_rh_parahippocampal', 'wm_rh_paracentral', 'wm_rh_parsopercularis', 'wm_rh_parsorbitalis', 'wm_rh_parstriangularis', 
             'wm_rh_pericalcarine', 'wm_rh_postcentral', 'wm_rh_posteriorcingulate', 'wm_rh_precentral', 'wm_rh_precuneus', 
             'wm_rh_rostralanteriorcingulate', 'wm_rh_rostralmiddlefrontal', 'wm_rh_superiorfrontal', 'wm_rh_superiorparietal', 
             'wm_rh_superiortemporal', 'wm_rh_supramarginal', 'wm_rh_frontalpole', 'wm_rh_temporalpole', 'wm_rh_transversetemporal', 
             'wm_rh_insula'
            ]] #.values #.reshape(-1,1) #select column through end predictors
y = dataset['mri_GCPS_Characteristic_Pain_Intensity_Score'] #.values #.reshape(-1,1)   #select column target

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=16, random_state=0) #split 20% of the data to test
X_train, X_test, y_train, y_test = train_test_split( X.values, y.values, train_size=.9, test_size=.1, shuffle=True)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

regr = LinearRegression()  
regr.fit(X_train, y_train) #training the algorithm

coeff_df = pd.DataFrame(regr.coef_, X.columns, columns=['Coefficient'])  #view selected coefficients
coeff_df

#To retrieve the intercept:
print(regr.intercept_)
#For retrieving the slope:
print(regr.coef_)

y_pred = regr.predict(X_test)

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
df1 = df.head(25)
df1.plot(kind='bar',figsize=(10,8))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
df

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
print('R squared:', metrics.r2_score(y_test, y_pred))
