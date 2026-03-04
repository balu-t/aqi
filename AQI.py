def read_sensor_data(filename):
    data = {}

    with open(filename, 'r') as file:
        for line in file:
            key, value = line.strip().split("=")
            data[key] = float(value)

    return data


def calculate_aqi(data):
    values = list(data.values())
    return sum(values) / len(values)


def reflex_agent(aqi):

    if aqi <= 50:
        return "Good"

    elif aqi <= 100:
        return "Moderate"

    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups"

    elif aqi <= 200:
        return "Unhealthy"

    elif aqi <= 300:
        return "Very Unhealthy"

    else:
        return "Hazardous"


sensor_data = read_sensor_data("sensor_data.txt")

aqi = calculate_aqi(sensor_data)

result = reflex_agent(aqi)

print("Sensor Data:", sensor_data)
print("Calculated AQI:", aqi)
print("Air Quality:", result)