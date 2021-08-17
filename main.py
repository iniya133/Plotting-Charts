import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("gravity.csv")

df.head()

mass = df["mass"].to_list()
radius = df["radius"].to_list()
dist = df["distance"].to_list()
gravity = df["gravity"].to_list()

mass.sort()
radius.sort()
gravity.sort()
plt.plot(radius, mass)

plt.title("Radius & Mass of the Star")
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()

plt.plot(mass, gravity)

plt.title("Mass vs Gravity")
plt.xlabel("Mass")
plt.ylabel("Gravity")
plt.show()

plt.scatter(radius, mass)
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()