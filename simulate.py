"""Reproduce the EN3330 figures and check the analytic results numerically."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent / "figures"
COLORS = ["#164d71", "#c45e22", "#138570", "#884d88"]


def lagrangian(mu, x):
    return x**2 + mu * (1 - x)


def dual(mu):
    return mu - mu**2 / 4


def save(fig, name):
    for ax in fig.axes:
        ax.grid(alpha=0.17)
        ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(OUT / (name + ".pdf"), bbox_inches="tight")
    plt.close(fig)


def main():
    OUT.mkdir(exist_ok=True)
    x = np.linspace(-1, 3, 1601)
    mu = np.linspace(0, 5, 1001)
    primal = np.min(x[x >= 1] ** 2)
    fig, ax = plt.subplots(figsize=(6.8, 2.8))
    print("mu   x_min   grid minimum   dual    primal-dual gap")
    for m, color in enumerate(COLORS):
        values = lagrangian(m, x)
        i = np.argmin(values)
        np.testing.assert_allclose([x[i], values[i]], [m / 2, dual(m)])
        assert dual(m) <= primal
        print(f"{m:2}   {x[i]:5.2f}      {values[i]:5.2f}     {dual(m):5.2f}       {primal-dual(m):5.2f}")
        ax.plot(x, values, color=color, label=rf"$\mu={m}$")
        ax.scatter(x[i], values[i], color=color, zorder=3)
    ax.axvline(1, color="grey", ls=":", lw=1)
    ax.set(xlabel="Decision variable x", ylabel="Lagrangian value")
    ax.legend(ncol=4, fontsize=9)
    save(fig, "curves")

    fig, ax = plt.subplots(figsize=(6.8, 2.35))
    ax.plot(mu, dual(mu), color=COLORS[0])
    k = np.argmax(dual(mu))
    np.testing.assert_allclose([mu[k], dual(mu[k]), primal], [2, 1, 1])
    ax.scatter(2, 1, color=COLORS[1], zorder=3)
    ax.annotate("(2, 1)", (2, 1), xytext=(7, -17), textcoords="offset points")
    ax.set(xlabel=r"Multiplier $\mu$", ylabel=r"Dual bound $d(\mu)$")
    save(fig, "dual")

    fig, ax = plt.subplots(figsize=(6.8, 2.85))
    feasible = x >= 1
    ax.axvspan(-1, 1, color="#faf1e7")
    for cap, color in zip([2, 4, 8], COLORS[1:]):
        capped = np.maximum(lagrangian(0, x), lagrangian(cap, x))
        ax.plot(x[~feasible], capped[~feasible], "--", color=color,
                label=f"Multiplier cap {cap}")
    ax.plot(x[feasible], x[feasible]**2, color=COLORS[0], label=r"Exact $g(x)=x^2$")
    ax.scatter(1, 1, color=COLORS[0])
    ax.text(-0.96, 18, r"$g(x)=+\infty$ throughout $x<1$")
    ax.set(xlim=(-1, 3), ylim=(0, 20), xlabel="Decision variable x", ylabel="Objective value")
    ax.legend(fontsize=8, loc="upper right")
    save(fig, "primal")

    fig, axes = plt.subplots(1, 2, figsize=(7, 2.45), layout="constrained")
    for ax, t, y, label, tstar in [
        (axes[0], mu, lagrangian(mu, 1), r"Multiplier $\mu$ at $x=1$", 2),
        (axes[1], x, lagrangian(2, x), r"Decision variable $x$ at $\mu=2$", 1),
    ]:
        ax.plot(t, y, color=COLORS[0])
        ax.scatter(tstar, 1, color=COLORS[1], zorder=3)
        ax.set(xlabel=label, ylabel="Lagrangian value", ylim=(0, 5.4))
    np.testing.assert_allclose(lagrangian(mu, 1), 1)
    assert np.all(lagrangian(2, x) >= 1)
    save(fig, "saddle")

    fig, ax = plt.subplots(figsize=(6.8, 3))
    lines = np.array([lagrangian(mu, point) for point in (0, 1, 2)])
    for point, line, color in zip((0, 1, 2), lines, COLORS):
        ax.plot(mu, line, color=color, lw=1.2, label=f"x = {point}")
    envelope = lines.min(axis=0)
    assert np.all(envelope + 1e-12 >= dual(mu))
    ax.plot(mu, envelope, "--", color="#262626", lw=2.5, label="Three-point envelope")
    ax.plot(mu, dual(mu), ":", color=COLORS[3], lw=2.5, label="Exact dual")
    ax.set(xlabel=r"Multiplier $\mu$", ylabel="Lagrangian value")
    ax.legend(fontsize=8, ncol=2)
    save(fig, "envelope")


if __name__ == "__main__":
    main()
