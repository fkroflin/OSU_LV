import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt

#a
file = np.loadtxt("data.csv", delimiter=',', skiprows=1)
print("Broj osoba na koliko je izvrseno mjerenje: ",len(file))

#b
x=np.array(file[:,2])
y=np.array(file[:,1])
plt.scatter(x,y)
plt.xlabel("masa(kg)")
plt.ylabel("visina(cm)")
plt.title("Odnos visine i mase natjecatelja")
# plt.show()

#c
x1=np.array(file[::50,2])
y1=np.array(file[::50,1])
plt.scatter(x1,y1)
plt.xlabel("masa(kg)")
plt.ylabel("visina(cm)")
plt.title("Odnos visine i mase svakog 50 natjecatelja")
# plt.show()

#d
print("Najmanja visina:", y.min(), "cm")
print("Najvisa visina:", y.max(), "cm")
print("Srednja vrijednost visine:", y.mean(), "cm")

#e
men=file[np.where(file[:,0]==1)]
women=file[np.where(file[:,0]==0)]
print("Najmanja visina kod muskaraca:", men[:,1].min(), "cm", "a kod zena:", women[:,1].min(), "cm")
print("Najvisa visina kod muskaraca:", men[:,1].max(), "cm", "a kod zena:", women[:,1].max(), "cm")
print("Srednja visina kod muskaraca:", men[:,1].mean(), "cm", "a kod zena:", women[:,1].mean(), "cm")
