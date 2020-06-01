# -*- coding: utf-8 -*-
"""
Created on Sun May 31 18:34:07 2020

@author: Evgenii
"""


import pandas as pd
import matplotlib.pyplot as plt
import datetime

from sklearn.linear_model import LinearRegression

electricity_data_link = "IPG2211A2N.xls"
electricity_consumption = pd.read_excel(
    electricity_data_link,
    skiprows = 10         #skiprows 10 - описательные данные таблицы
) 
year = '2010'

#electricity_consumption=electricity_consumption.loc[electricity_consumption['observation_date']
#                            >=
#                            datetime.datetime(2016,11,1)]
electricity_consumption_graphic, axis = plt.subplots(2, figsize=(30,15))

trump_energy_consumption = electricity_consumption.loc[
    electricity_consumption['observation_date']
    >=
    datetime.datetime(2016,11,1)
]
for index, ax in enumerate(axis):
    ax.set_title("{0} term".format(index+1))


obama_energy_consumption = list()

obama_energy_consumption.append(electricity_consumption.loc[
    (electricity_consumption['observation_date']>datetime.datetime(2008,11,1))
    &
    (electricity_consumption['observation_date']<=datetime.datetime(2012,11,1))
])

obama_energy_consumption.append(electricity_consumption.loc[
    (electricity_consumption['observation_date']>datetime.datetime(2012,11,1))
    &
    (electricity_consumption['observation_date']<=datetime.datetime(2016,11,1))
])


for i in range(len(obama_energy_consumption)):
    axis[i].plot(
        obama_energy_consumption[i]['observation_date'],
        obama_energy_consumption[i]['IPG2211A2N'].rolling(6).mean()
)

regression_models = list()
for i in range(len(obama_energy_consumption)):
    regression_models.append(LinearRegression())

X=list()
for i in range(len(obama_energy_consumption)):
    X.append( pd.DataFrame(
        list(range(len(obama_energy_consumption[i]['observation_date'])))   
))


for index, regression in enumerate(regression_models):
    regression.fit(X[index],obama_energy_consumption[index]['IPG2211A2N'])

regression_result = [None]*len(obama_energy_consumption)
for index, regression in enumerate(regression_models):
    axis[index].plot(
        obama_energy_consumption[index]['observation_date'],
        regression.predict(X[index])
    )    
    
    
    