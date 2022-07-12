def gas_station(distance, tank_size, stations):
    result = []
    distance_traveled = 80

    for i in range(1, len(stations)):
        if distance_traveled < stations[i]:
            result.append(stations[i - 1])
            distance_traveled = tank_size + stations[i - 1]
    
    if distance_traveled < distance:
        result.append(stations[len(stations) - 1])
    
    return result

print(gas_station(390, 80, [70, 90, 140, 210, 240, 280, 350]))