#capacity, numBikesAvailable, demand, threshold

def calculate_necessity(capacity, numBikesAvailable, demand, threshold):
    target = capacity * threshold
    return target - (numBikesAvailable - demand)


print(calculate_necessity(25, 12, 2, 0.8))