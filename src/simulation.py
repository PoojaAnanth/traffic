import pandas as pd  
from traffic_signal import TrafficSignal  
  
# Load data  
data = pd.read_csv('traffic_data.csv')  
  
# Create a traffic signal object  
traffic_signal = TrafficSignal(1)  
  
# Simulate traffic signal control  
for index, row in data.iterrows():  
   traffic_density = row['Traffic_Density']  
   vehicle_count = row['Vehicle_Count']  
   signal = traffic_signal.control_signal(traffic_density, vehicle_count)  
   print(f"Traffic Density: {traffic_density}, Vehicle Count: {vehicle_count}, Signal: {signal}")