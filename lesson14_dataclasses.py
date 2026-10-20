from dataclasses import dataclass

@dataclass
class SensorReading:
    sensor_name: str
    value: float
    unit: str
    
temperature = SensorReading(
    sensor_name="Temperature",
    value=28.5,
    unit="Celsius"
)

soil_moisture = SensorReading(
    sensor_name="Soil Moisture",
    value=35.0,
    unit="percent"
)

print(temperature)
print(soil_moisture)
print(temperature.value)