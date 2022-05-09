import numpy as np
import unittest

# import pytest
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

from fdm import visualization as vis


class Test_1D_advection(unittest.TestCase):
    # @pytest.mark.skip(reason="how to skip test")
    def test_(self):  # function's name have to start with "test_"
        a = 2.0
        tmax = 1.0
        Lx = 1.0
        nx = 99  # tune
        hx = Lx / (nx + 1)
        ht = 0.003
        nt = int(tmax / ht) + 1
        x = np.linspace(0, Lx, nx + 1)
        c = a * ht / hx
        u0 = np.exp(-600 * (x - 0.5) ** 2)

        u2DEuler, u2DLax, u2DLaxF, u2DBW, u2DRK3, uExact = map(
            np.zeros,
            (
                (nt + 1, nx + 1),
                (nt + 1, nx + 1),
                (nt + 1, nx + 1),
                (nt + 1, nx + 1),
                (nt + 1, nx + 1),
                (nt + 1, nx + 1),
            ),
        )
        u2DEuler[0], u2DLax[0], u2DRK3[0], u2DLaxF[0], u2DLaxF[0] = map(
            np.copy, (u0, u0, u0, u0, u0)
        )

        for n in range(nt):
            u2DEuler[n + 1] = Euler(u2DEuler[n], nx, c)
            u2DLax[n + 1] = LaxWendroff(u2DLax[n], nx, c)
            u2DLaxF[n + 1] = LaxFriedrichs(u2DLaxF[n], nx, c)
            u2DRK3[n + 1] = rungeKutta(u2DRK3[n], nx, c)
            u2DBW[n + 1] = BeamWarming(u2DBW[n], nx, c)

        time = np.arange(0, tmax + ht / 10, ht)
        for n in range(nt):
            uExact[n] = exactSol(x, time[n], a)

        vis.animPlotE(x, u2DLax, uExact)


def exactSol(x, t, a):
    return np.exp(-600 * (x - a * t - np.floor(x - a * t) - 0.5) ** 2)


def Euler(u, nx, c):

    un = np.copy(u)
    for i in range(nx, 0, -1):
        u[i] = un[i] - c * (un[i] - un[i - 1])
    u[0] = u[nx]
    return u


def BeamWarming(u, nx, c):
    un = np.copy(u)
    i = nx
    a = un[i] - 0.5 * c * (3 * un[i] - 4 * un[i - 1] + un[i - 2])
    b = 0.5 * (c ** 2) * (un[i] - 2 * un[i - 1] + un[i - 2])
    u[i] = a + b
    for i in range(nx - 1, 0, -1):
        a = un[i] - 0.5 * c * (3 * un[i] - 4 * un[i - 1] + un[i - 2])
        b = 0.5 * (c ** 2) * (un[i] - 2 * un[i - 1] + un[i - 2])
        u[i] = a + b
    u[0] = u[nx]
    return u


def LaxWendroff(u, nx, c):
    un = np.copy(u)
    i = nx
    a = un[i] - 0.5 * c * (un[0] - un[i - 1])
    b = 0.5 * (c ** 2) * (un[0] - 2 * un[i] + un[i - 1])
    u[i] = a + b
    for i in range(nx - 1, 0, -1):
        a = un[i] - 0.5 * c * (un[i + 1] - un[i - 1])
        b = 0.5 * (c ** 2) * (un[i + 1] - 2 * un[i] + un[i - 1])
        u[i] = a + b
    u[0] = u[nx]
    return u


def LaxFriedrichs(u, nx, c):
    un = np.copy(u)
    i = nx
    a = un[i] - 0.5 * c * (un[0] - un[i - 1])
    b = 0.5 * (un[0] - 2 * un[i] + un[i - 1])
    u[i] = a + b
    for i in range(nx - 1, 0, -1):
        a = un[i] - 0.5 * c * (un[i + 1] - un[i - 1])
        b = 0.5 * (un[i + 1] - 2 * un[i] + un[i - 1])
        u[i] = a + b
    u[0] = u[nx]
    return u


def rungeKutta(u, nx, c):

    un = np.copy(u)
    u1, u2 = map(np.zeros_like, (u, u))

    for i in range(nx - 1, -1, -1):
        u1[i] = un[i] - 0.5 * c * (un[i + 1] - un[i - 1])
    i = nx
    u1[i] = un[i] - 0.5 * c * (un[0] - un[i - 1])

    for i in range(nx - 1, -1, -1):
        u2[i] = 0.75 * un[i] + 0.25 * u1[i] - 0.125 * c * (u1[i + 1] - u1[i - 1])
    i = nx
    u2[i] = 0.75 * un[i] + 0.25 * u1[i] - 0.125 * c * (u1[0] - u1[i - 1])

    for i in range(nx - 1, -1, -1):
        u[i] = (un[i] + 2 * u2[i] - c * (u2[i + 1] - u2[i - 1])) / 3
    i = nx
    u[i] = (un[i] + 2 * u2[i] - c * (u2[0] - u2[i - 1])) / 3

    return u


if __name__ == "__main__":
    unittest.main()
