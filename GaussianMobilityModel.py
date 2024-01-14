import random
import matplotlib.pyplot as plt
import math
# Initialize parameters
alpha = 0.5  # Tuning parameter
s_mean = 5  # Mean speed
d_mean = 1  # Mean direction
s = s_mean  # Initial speed
d = d_mean  # Initial direction
x, y = 0, 0  # Initial position


# Function to update speed
def update_speed(s_prev):
    sx = random.gauss(0, math.sqrt(1 - alpha**2))  # Gaussian noise for speed
    return alpha * s_prev + (1 - alpha) * s_mean + sx

# Function to update direction
def update_direction(d_prev):
    dx = random.gauss(0, math.sqrt(1 - alpha**2))  # Gaussian noise for direction
    return alpha * d_prev + (1 - alpha) * d_mean + dx

# Arrays to store the positions
x_positions = [x]
y_positions = [y]

# Simulate movement for 100 time steps
for t in range(100):
    s = update_speed(s)
    d = update_direction(d)

    # Update position
    x += s * math.cos(d)
    y += s * math.sin(d)

    x_positions.append(x)
    y_positions.append(y)

# Plot the path
plt.plot(x_positions, y_positions)
plt.title("Gauss–Markov Mobility Model Simulation")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.grid(True)
plt.show()
