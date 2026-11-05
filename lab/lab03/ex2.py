import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

f = 4
fs = 1000
omegas = [1, 2, 4, 7]

t = np.arange(0, 1, 1 / fs)
x = np.sin(2 * np.pi * f * t)
y = x * np.exp(-2j * np.pi * t)


def setup_complex_axis(ax, title=None):
    if title is not None:
        ax.set_title(title)

    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginar")
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_aspect("equal")
    ax.grid(True)


def colored_scatter(ax, x, y, distance):
    return ax.scatter(x, y, c=distance, cmap="turbo", vmin=0, vmax=1, s=2)


# fig 1

fig, axs = plt.subplots(1, 2, figsize=(20, 10))

colored_scatter(axs[0], t, x, np.abs(x))
axs[0].set_xlabel("Timp")
axs[0].set_ylabel("Amplitudine")

colored_scatter(axs[1], y.real, y.imag, np.abs(y))
setup_complex_axis(axs[1])

plt.tight_layout()
plt.savefig("ex2_fig1.pdf")
plt.show()

# fig 2

fig, axs = plt.subplots(2, 2, figsize=(10, 10))

for i, w in enumerate(omegas):
    ax = axs[i // 2, i % 2]

    z = x * np.exp(-2j * np.pi * w * t)

    colored_scatter(ax, z.real, z.imag, np.abs(z))
    setup_complex_axis(ax, f"w = {w}")

plt.tight_layout()
plt.savefig("ex2_fig2.pdf")
plt.show()

# animatie fig 1

fig, axs = plt.subplots(1, 2, figsize=(20, 10))

axs[0].set_xlim(0, 1)
axs[0].set_ylim(-1.1, 1.1)
axs[0].set_xlabel("Timp")
axs[0].set_ylabel("Amplitudine")
axs[0].grid(True)

setup_complex_axis(axs[1])

points0 = colored_scatter(axs[0], [], [], [])
points1 = colored_scatter(axs[1], [], [], [])

current0 = axs[0].plot([], [], "ro", markersize=7)[0]
current1 = axs[1].plot([], [], "ro", markersize=7)[0]


def update_fig1(frame):
    points0.set_offsets(np.column_stack((t[:frame + 1], x[:frame + 1])))
    points0.set_array(np.abs(x[:frame + 1]))

    points1.set_offsets(np.column_stack((y.real[:frame + 1], y.imag[:frame + 1])))
    points1.set_array(np.abs(y[:frame + 1]))

    current0.set_data([t[frame]], [x[frame]])
    current1.set_data([y.real[frame]], [y.imag[frame]])

    return points0, points1, current0, current1


anim_fig1 = FuncAnimation(
    fig,
    update_fig1,
    frames=range(0, len(t), 5),
    interval=40,
    blit=True
)

anim_fig1.save("ex2_fig1_animatie.gif", writer="pillow", fps=25)
plt.show()

# animatie fig 2

fig, axs = plt.subplots(2, 2, figsize=(10, 10))

points = []
current = []
wrapped = []

for i, w in enumerate(omegas):
    ax = axs[i // 2, i % 2]

    z = x * np.exp(-2j * np.pi * w * t)
    wrapped.append(z)

    setup_complex_axis(ax, f"w = {w}")

    points.append(colored_scatter(ax, [], [], []))

    marker, = ax.plot([], [], "ro", markersize=7)
    current.append(marker)


def update_fig2(frame):
    artists = []

    for i, z in enumerate(wrapped):
        points[i].set_offsets(
            np.column_stack((z.real[:frame + 1], z.imag[:frame + 1]))
        )
        points[i].set_array(np.abs(z[:frame + 1]))

        current[i].set_data([z.real[frame]], [z.imag[frame]])

        artists.extend((points[i], current[i]))

    return artists


plt.tight_layout()

anim_fig2 = FuncAnimation(
    fig,
    update_fig2,
    frames=range(0, len(t), 5),
    interval=40,
    blit=True
)

anim_fig2.save("ex2_fig2_animatie.gif", writer="pillow", fps=25)
plt.show()
