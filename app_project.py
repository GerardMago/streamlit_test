import matplotlib.pyplot as plt
import streamlit as st
import operator
import pandas as pd
import numpy as np
from PIL import Image       # this package is used to put images within streamlit
from recull_dades import recull_dades       # keep this commented if not using it otherwise brakes the app


# PAGE SETTING
st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

a1, a2 = st.columns(2)
a1.title('Final Project CAPUEE')
a1.header('Group 1. PV panel control and monitoring')
a1.text('The purpose of this page is to show hourly production throughout the day.\nThe ambient temperature, PV panel temperature, energy produced, bus volta-\nge and generated current are displayed. In addition, it shows the economic\nsavings that the user can have for every 10 W of installed power.')
a2.image(Image.open('upc_logo.png'))
st.header('PV panel control and monitoring')
st.text('The table below shows the obtained values for January 2nd, 2023:')

## PROCESS OF THE DATA OBTAINED FROM THE PV PANEL
PV_data = pd.read_csv('Project1_dia.csv', sep = ';')

Mean_T_amb_00 = sum(PV_data.iloc[0:719,2])/720
Mean_T_amb_01 = sum(PV_data.iloc[720:1439,2])/720
Mean_T_amb_02 = sum(PV_data.iloc[1440:2159,2])/720
Mean_T_amb_03 = sum(PV_data.iloc[2160:2879,2])/720
Mean_T_amb_04 = sum(PV_data.iloc[2880:3599,2])/720
Mean_T_amb_05 = sum(PV_data.iloc[3600:4319,2])/720
Mean_T_amb_06 = sum(PV_data.iloc[4320:5039,2])/720
Mean_T_amb_07 = sum(PV_data.iloc[5040:5759,2])/720
Mean_T_amb_08 = sum(PV_data.iloc[5760:6479,2])/720
Mean_T_amb_09 = sum(PV_data.iloc[6480:7199,2])/720
Mean_T_amb_10 = sum(PV_data.iloc[7200:7919,2])/720
Mean_T_amb_11 = sum(PV_data.iloc[7920:8639,2])/720
Mean_T_amb_12 = sum(PV_data.iloc[8640:9359,2])/720
Mean_T_amb_13 = sum(PV_data.iloc[9360:10079,2])/720
Mean_T_amb_14 = sum(PV_data.iloc[10080:10799,2])/720
Mean_T_amb_15 = sum(PV_data.iloc[10800:11519,2])/720
Mean_T_amb_16 = sum(PV_data.iloc[11520:12239,2])/720
Mean_T_amb_17 = sum(PV_data.iloc[12240:12959,2])/720
Mean_T_amb_18 = sum(PV_data.iloc[12960:13679,2])/720
Mean_T_amb_19 = sum(PV_data.iloc[13680:14399,2])/720
Mean_T_amb_20 = sum(PV_data.iloc[14400:15119,2])/720
Mean_T_amb_21 = sum(PV_data.iloc[15120:15839,2])/720
Mean_T_amb_22 = sum(PV_data.iloc[15840:16559,2])/720
Mean_T_amb_23 = sum(PV_data.iloc[16560:17279,2])/720

Mean_T_amb = [Mean_T_amb_00, Mean_T_amb_01, Mean_T_amb_02, Mean_T_amb_03, Mean_T_amb_04, Mean_T_amb_05, Mean_T_amb_06, Mean_T_amb_07, Mean_T_amb_08, Mean_T_amb_09, Mean_T_amb_10, Mean_T_amb_11, Mean_T_amb_12, Mean_T_amb_13, Mean_T_amb_14, Mean_T_amb_15, Mean_T_amb_16, Mean_T_amb_17, Mean_T_amb_18, Mean_T_amb_19, Mean_T_amb_20, Mean_T_amb_21, Mean_T_amb_22, Mean_T_amb_23]

V_bus_00 = sum(PV_data.iloc[0:719,3])/720
V_bus_01 = sum(PV_data.iloc[720:1439,3])/720
V_bus_02 = sum(PV_data.iloc[1440:2159,3])/720
V_bus_03 = sum(PV_data.iloc[2160:2879,3])/720
V_bus_04 = sum(PV_data.iloc[2880:3599,3])/720
V_bus_05 = sum(PV_data.iloc[3600:4319,3])/720
V_bus_06 = sum(PV_data.iloc[4320:5039,3])/720
V_bus_07 = sum(PV_data.iloc[5040:5759,3])/720
V_bus_08 = sum(PV_data.iloc[5760:6479,3])/720
V_bus_09 = sum(PV_data.iloc[6480:7199,3])/720
V_bus_10 = sum(PV_data.iloc[7200:7919,3])/720
V_bus_11 = sum(PV_data.iloc[7920:8639,3])/720
V_bus_12 = sum(PV_data.iloc[8640:9359,3])/720
V_bus_13 = sum(PV_data.iloc[9360:10079,3])/720
V_bus_14 = sum(PV_data.iloc[10080:10799,3])/720
V_bus_15 = sum(PV_data.iloc[10800:11519,3])/720
V_bus_16 = sum(PV_data.iloc[11520:12239,3])/720
V_bus_17 = sum(PV_data.iloc[12240:12959,3])/720
V_bus_18 = sum(PV_data.iloc[12960:13679,3])/720
V_bus_19 = sum(PV_data.iloc[13680:14399,3])/720
V_bus_20 = sum(PV_data.iloc[14400:15119,3])/720
V_bus_21 = sum(PV_data.iloc[15120:15839,3])/720
V_bus_22 = sum(PV_data.iloc[15840:16559,3])/720
V_bus_23 = sum(PV_data.iloc[16560:17279,3])/720

V_bus = [V_bus_00, V_bus_01, V_bus_02, V_bus_03, V_bus_04, V_bus_05, V_bus_06, V_bus_07, V_bus_08, V_bus_09, V_bus_10, V_bus_11, V_bus_12, V_bus_13, V_bus_14, V_bus_15, V_bus_16, V_bus_17, V_bus_18, V_bus_19, V_bus_20, V_bus_21, V_bus_22, V_bus_23]

V_00 = sum(PV_data.iloc[0:719,4])/720
V_01 = sum(PV_data.iloc[720:1439,4])/720
V_02 = sum(PV_data.iloc[1440:2159,4])/720
V_03 = sum(PV_data.iloc[2160:2879,4])/720
V_04 = sum(PV_data.iloc[2880:3599,4])/720
V_05 = sum(PV_data.iloc[3600:4319,4])/720
V_06 = sum(PV_data.iloc[4320:5039,4])/720
V_07 = sum(PV_data.iloc[5040:5759,4])/720
V_08 = sum(PV_data.iloc[5760:6479,4])/720
V_09 = sum(PV_data.iloc[6480:7199,4])/720
V_10 = sum(PV_data.iloc[7200:7919,4])/720
V_11 = sum(PV_data.iloc[7920:8639,4])/720
V_12 = sum(PV_data.iloc[8640:9359,4])/720
V_13 = sum(PV_data.iloc[9360:10079,4])/720
V_14 = sum(PV_data.iloc[10080:10799,4])/720
V_15 = sum(PV_data.iloc[10800:11519,4])/720
V_16 = sum(PV_data.iloc[11520:12239,4])/720
V_17 = sum(PV_data.iloc[12240:12959,4])/720
V_18 = sum(PV_data.iloc[12960:13679,4])/720
V_19 = sum(PV_data.iloc[13680:14399,4])/720
V_20 = sum(PV_data.iloc[14400:15119,4])/720
V_21 = sum(PV_data.iloc[15120:15839,4])/720
V_22 = sum(PV_data.iloc[15840:16559,4])/720
V_23 = sum(PV_data.iloc[16560:17279,4])/720

V = [V_00, V_01, V_02, V_03, V_04, V_05, V_06, V_07, V_08, V_09, V_10, V_11, V_12, V_13, V_14, V_15, V_16, V_17, V_18, V_19, V_20, V_21, V_22, V_23]

mA_00 = sum(PV_data.iloc[0:719,5])/720000
mA_01 = sum(PV_data.iloc[720:1439,5])/720000
mA_02 = sum(PV_data.iloc[1440:2159,5])/720000
mA_03 = sum(PV_data.iloc[2160:2879,5])/720000
mA_04 = sum(PV_data.iloc[2880:3599,5])/720000
mA_05 = sum(PV_data.iloc[3600:4319,5])/720000
mA_06 = sum(PV_data.iloc[4320:5039,5])/720000
mA_07 = sum(PV_data.iloc[5040:5759,5])/720000
mA_08 = sum(PV_data.iloc[5760:6479,5])/720000
mA_09 = sum(PV_data.iloc[6480:7199,5])/720000
mA_10 = sum(PV_data.iloc[7200:7919,5])/720000
mA_11 = sum(PV_data.iloc[7920:8639,5])/720000
mA_12 = sum(PV_data.iloc[8640:9359,5])/720000
mA_13 = sum(PV_data.iloc[9360:10079,5])/720000
mA_14 = sum(PV_data.iloc[10080:10799,5])/720000
mA_15 = sum(PV_data.iloc[10800:11519,5])/720000
mA_16 = sum(PV_data.iloc[11520:12239,5])/720000
mA_17 = sum(PV_data.iloc[12240:12959,5])/720000
mA_18 = sum(PV_data.iloc[12960:13679,5])/720000
mA_19 = sum(PV_data.iloc[13680:14399,5])/720000
mA_20 = sum(PV_data.iloc[14400:15119,5])/720000
mA_21 = sum(PV_data.iloc[15120:15839,5])/720000
mA_22 = sum(PV_data.iloc[15840:16559,5])/720000
mA_23 = sum(PV_data.iloc[16560:17279,5])/720000

mA = [mA_00, mA_01, mA_02, mA_03, mA_04, mA_05, mA_06, mA_07, mA_08, mA_09, mA_10, mA_11, mA_12, mA_13, mA_14, mA_15, mA_16, mA_17, mA_18, mA_19, mA_20, mA_21, mA_22, mA_23]

mW_00 = sum(PV_data.iloc[0:719,6])/720
mW_01 = sum(PV_data.iloc[720:1439,6])/720
mW_02 = sum(PV_data.iloc[1440:2159,6])/720
mW_03 = sum(PV_data.iloc[2160:2879,6])/720
mW_04 = sum(PV_data.iloc[2880:3599,6])/720
mW_05 = sum(PV_data.iloc[3600:4319,6])/720
mW_06 = sum(PV_data.iloc[4320:5039,6])/720
mW_07 = sum(PV_data.iloc[5040:5759,6])/720
mW_08 = sum(PV_data.iloc[5760:6479,6])/720
mW_09 = sum(PV_data.iloc[6480:7199,6])/720
mW_10 = sum(PV_data.iloc[7200:7919,6])/720
mW_11 = sum(PV_data.iloc[7920:8639,6])/720
mW_12 = sum(PV_data.iloc[8640:9359,6])/720
mW_13 = sum(PV_data.iloc[9360:10079,6])/720
mW_14 = sum(PV_data.iloc[10080:10799,6])/720
mW_15 = sum(PV_data.iloc[10800:11519,6])/720
mW_16 = sum(PV_data.iloc[11520:12239,6])/720
mW_17 = sum(PV_data.iloc[12240:12959,6])/720
mW_18 = sum(PV_data.iloc[12960:13679,6])/720
mW_19 = sum(PV_data.iloc[13680:14399,6])/720
mW_20 = sum(PV_data.iloc[14400:15119,6])/720
mW_21 = sum(PV_data.iloc[15120:15839,6])/720
mW_22 = sum(PV_data.iloc[15840:16559,6])/720
mW_23 = sum(PV_data.iloc[16560:17279,6])/720

mW = [mW_00, mW_01, mW_02, mW_03, mW_04, mW_05, mW_06, mW_07, mW_08, mW_09, mW_10, mW_11, mW_12, mW_13, mW_14, mW_15, mW_16, mW_17, mW_18, mW_19, mW_20, mW_21, mW_22, mW_23]

Mean_T_panell_00 = sum(PV_data.iloc[0:719,7])/720
Mean_T_panell_01 = sum(PV_data.iloc[720:1439,7])/720
Mean_T_panell_02 = sum(PV_data.iloc[1440:2159,7])/720
Mean_T_panell_03 = sum(PV_data.iloc[2160:2879,7])/720
Mean_T_panell_04 = sum(PV_data.iloc[2880:3599,7])/720
Mean_T_panell_05 = sum(PV_data.iloc[3600:4319,7])/720
Mean_T_panell_06 = sum(PV_data.iloc[4320:5039,7])/720
Mean_T_panell_07 = sum(PV_data.iloc[5040:5759,7])/720
Mean_T_panell_08 = sum(PV_data.iloc[5760:6479,7])/720
Mean_T_panell_09 = sum(PV_data.iloc[6480:7199,7])/720
Mean_T_panell_10 = sum(PV_data.iloc[7200:7919,7])/720
Mean_T_panell_11 = sum(PV_data.iloc[7920:8639,7])/720
Mean_T_panell_12 = sum(PV_data.iloc[8640:9359,7])/720
Mean_T_panell_13 = sum(PV_data.iloc[9360:10079,7])/720
Mean_T_panell_14 = sum(PV_data.iloc[10080:10799,7])/720
Mean_T_panell_15 = sum(PV_data.iloc[10800:11519,7])/720
Mean_T_panell_16 = sum(PV_data.iloc[11520:12239,7])/720
Mean_T_panell_17 = sum(PV_data.iloc[12240:12959,7])/720
Mean_T_panell_18 = sum(PV_data.iloc[12960:13679,7])/720
Mean_T_panell_19 = sum(PV_data.iloc[13680:14399,7])/720
Mean_T_panell_20 = sum(PV_data.iloc[14400:15119,7])/720
Mean_T_panell_21 = sum(PV_data.iloc[15120:15839,7])/720
Mean_T_panell_22 = sum(PV_data.iloc[15840:16559,7])/720
Mean_T_panell_23 = sum(PV_data.iloc[16560:17279,7])/720

Mean_T_panell = [Mean_T_panell_00, Mean_T_panell_01, Mean_T_panell_02, Mean_T_panell_03, Mean_T_panell_04, Mean_T_panell_05, Mean_T_panell_06, Mean_T_panell_07, Mean_T_panell_08, Mean_T_panell_09, Mean_T_panell_10, Mean_T_panell_11, Mean_T_panell_12, Mean_T_panell_13, Mean_T_panell_14, Mean_T_panell_15, Mean_T_panell_16, Mean_T_panell_17, Mean_T_panell_18, Mean_T_panell_19, Mean_T_panell_20, Mean_T_panell_21, Mean_T_panell_22, Mean_T_panell_23]

## API DATA SPOT MARKET PRICES [€/MWh]

json = recull_dades()
spot_market_prices = json['included'][0]
values = spot_market_prices['attributes']['values']
prices = []
hours = []

for time_period in values:
    #print(time_period['value'])
    prices.append(time_period['value'])
    hours.append(time_period['datetime'])

## SAVINGS CALCULATION
savings = list(map(operator.mul, prices, mW))       
savings_real=np.divide(savings, 10000000)

## OBTAINED VALUES DATAFRAME
b1, b2 = st.columns(2)
table = pd.DataFrame({'Hour':[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],'PV panel temperature [ºC]':Mean_T_panell,'Ambient temperature [ºC]': Mean_T_amb,'Voltage [V]': V_bus,'Current [A]': mA,'Energy [mWh]': mW,'Savings [c€]': savings_real})
table = table.set_index('Hour')
b1.dataframe(table)

## ENERGY PRODUCED vs PV PANEL TEMPERATURE
plt.style.use('ggplot')   
fig,ax = plt.subplots(figsize=(20,10)) #It gives the size of the figure 
ax.plot(mW, marker='.', linewidth=0.9, color='red',label='Power generated') # plot first the x, then the y and then the plot
ax.set_ylabel('Energy produced [mWh]', color='red', fontsize=18)
ax2=ax.twinx()
ax2.plot(Mean_T_panell, marker='.', linewidth=0.9, color= 'blue',label='PV panel temperature') # plot first the x, then the y and then the plot
ax2.set_ylabel('Temperature [°C]', color='blue', fontsize=18)
plt.title('Energy produced by the PV panel vs PV panel temperature', fontsize=20) 
plt.xlabel('Hour')
b2.pyplot(fig)

## SELECT BOX
dades = {
    '0:00':savings_real[0],
    '1:00':savings_real[1],
    '2:00':savings_real[2],
    '3:00':savings_real[3],
    '4:00':savings_real[4],
    '5:00':savings_real[5],
    '6:00':savings_real[6],
    '7:00':savings_real[7],
    '8:00':savings_real[8],
    '9:00':savings_real[9],
    '10:00':savings_real[10],
    '11:00':savings_real[11],
    '12:00':savings_real[12],
    '13:00':savings_real[13],
    '14:00':savings_real[14],
    '15:00':savings_real[15],
    '16:00':savings_real[16],
    '17:00':savings_real[17],
    '18:00':savings_real[18],
    '19:00':savings_real[19],
    '20:00':savings_real[20],
    '21:00':savings_real[21],
    '22:00':savings_real[22],
    '23:00':savings_real[23],
}
valors = dades.values()
llista = list(valors)
if __name__ == "__main__":
    # adding "select" as the first and default choice
    hour = a2.selectbox('Select the desired hour to know the savings you will obtain for each 10 Wp installed capacity', options=['select']+list(dades.keys()))
    # display selectbox 2 if manufacturer is not "select"
    if hour != 'select':
        a2.write('You selected ' + hour + ' and the savings obtained are 0.0504 c€')


