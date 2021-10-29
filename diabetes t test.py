# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 10:30:55 2021

@author: chels
"""

import pandas as pd
from scipy.stats import ttest_ind

diabetes = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Datasets/Diabetes/DB1_Diabetes/diabetic_data.csv')



# Is there a difference between sex (M:F) (IV)
# and the number of lab procedures (DV) performed?

Female = diabetes[diabetes['gender']=='Female']
Male = diabetes[diabetes['gender']=='Male']
ttest_ind(Female['num_lab_procedures'], Male['num_lab_procedures'])

# Ttest_indResult(statistic=0.9766138954321905, pvalue=0.3287626588477933)
# Since the p-value is greater than 0.05, the difference betwen sex 
# and number of lab procedures is not statistically significant.



# Is there a difference between RACE (Caucasian and African American)
# and the number of days in hospital?
Caucasian = diabetes[diabetes['race']=='Caucasian']
AfricanAmerican = diabetes[diabetes['race']=='AfricanAmerican']
ttest_ind(Caucasian['time_in_hospital'], AfricanAmerican['time_in_hospital'])

# Ttest_indResult(statistic=-5.0610017032095325, pvalue=4.178330085585203e-07)
# Since the p-value is less than 0.05, the difference between race (caucasian and
# african american) and the number of days in hospital is statistically significant.



# Is there a difference between RACE (Asian and African American) 
# and the number of lab procedures performed?
Asian = diabetes[diabetes['race']=='Asian']
ttest_ind(Asian['num_lab_procedures'], AfricanAmerican['num_lab_procedures'])

# Ttest_indResult(statistic=-3.9788715315360292, pvalue=6.948907528800307e-05)
# Since the p-value is less than 0.05, the difference between race (asian and
# african american) and the number of lab procdures is statistically significant.