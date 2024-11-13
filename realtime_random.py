import datetime as dt
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from rng import sine_rng

matplotlib.use("TkAgg")
plt.rcParams['toolbar'] = 'None'
plt.rcParams["keymap.quit"] = ['ctrl+c', 'cmd+c', 'q']

fig = plt.figure(frameon=False, figsize=(5, 1))
fig.canvas.manager.window.overrideredirect(1)
ax = fig.add_subplot(1, 1, 1)

fig.patch.set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

xs = []
ys = []

def animate(i, xs, ys):
    sine_rate = sine_rng()

    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(sine_rate)

    xs = xs[-20:]
    ys = ys[-20:]
    
    ax.clear()
    ax.plot(xs, ys)
    ax.axis('off')
    ax.get_xaxis().set_ticks([])
    ax.get_yaxis().set_ticks([])

    # plt.xticks(rotation=45, ha='right')
    fig.subplots_adjust(0,0,1,1)
    # plt.title('Sine Rate')
    # plt.ylabel('?')

ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=40)
plt.show()