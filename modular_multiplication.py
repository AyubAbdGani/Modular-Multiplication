import numpy as np 
import matplotlib.pyplot as plt 

# Modular Multiplication By Ayub AG

jumlah_titik = 150
radius_lingkaran = 3

fig = plt.figure(facecolor='black')
ax = fig.add_axes([0,0,1,1], aspect='equal', facecolor='black')
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(-radius_lingkaran - 0.2, radius_lingkaran + 0.2)
ax.set_ylim(-radius_lingkaran - 0.2, radius_lingkaran + 0.2)

gmbr, = ax.plot([], [], lw=1, color='white', antialiased=True)

sudut_titik = np.linspace(0, 2 * np.pi, jumlah_titik + 1)
titikX = radius_lingkaran * np.sin(sudut_titik)
titikY = radius_lingkaran * np.cos(sudut_titik)

x = np.empty(0)
y = np.empty(0)
for i in np.arange(jumlah_titik):
    modulo = (i * 1.2) % jumlah_titik
    x = np.append(x, [titikX[i], titikX[int(modulo)], np.nan])
    y = np.append(y, [titikY[i], titikY[int(modulo)], np.nan])
    gmbr.set_data(x, y)
    fig.canvas.draw()
    plt.pause(10/1000)

for j in np.arange(1.2, 10, 0.01):
    x = np.empty(0)
    y = np.empty(0)
    for i in np.arange(jumlah_titik):
        modulo = (i * j) % jumlah_titik
        x = np.append(x, [titikX[i], titikX[int(modulo)], np.nan])
        y = np.append(y, [titikY[i], titikY[int(modulo)], np.nan])
    gmbr.set_data(x, y)
    fig.canvas.draw()
    plt.pause(10/1000)