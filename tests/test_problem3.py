import numpy as np
import unittest

# import pytest
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

from fdm import visualization as vis


class Test_1D_advection(unittest.TestCase):
    # @pytest.mark.skip(reason="how to skip test")
    def test_test(self):  # function's name have to start with "test_"
        a = 1.0
        tmax = 10
        Lx = 1
        nx = 99
        hx = Lx / (nx + 1)
        # ht = 0.005
        ht = 0.01
        nt = int(tmax / ht) + 1
        x = np.linspace(0, Lx, nx + 1)
        c = a * ht / hx
        u0 = np.sin(2 * np.pi * x)

        uEuler, uLax, uRK3 = map(np.copy, (u0, u0, u0))
        u2DEuler, u2DLax, u2DRK3, uExact = map(
            np.zeros,
            ((nt + 1, nx + 1), (nt + 1, nx + 1), (nt + 1, nx + 1), (nt + 1, nx + 1)),
        )
        u2DEuler[0], u2DLax[0], u2DRK3[0] = map(np.copy, (u0, u0, u0))

        for n in range(nt):
            uEuler = Euler(uEuler, nx, c)
            uLax = LaxWendroff(uLax, nx, c)
            uRK3 = rungeKutta(uRK3, nx, c)
            u2DEuler[n + 1] = uEuler
            u2DLax[n] = uLax
            u2DRK3[n] = uRK3

        time = np.arange(0, tmax + ht / 10, ht)
        for n in range(nt):
            uExact[n] = exactSol(x, time[n], a)

        """
        figNum = 1
        fileName = "t1c1"
        plotTitle = "t = 1s and c = 1"
        label1 = "Euler"
        label2 = "Lax Wendroff"
        label3 = "Runge Kutta 3th"
        label4 = "Exact Solution"
        ind = 100
        # vis.plot(figNum, fileName, plotTitle, label1, label2, label3, label4, x, u2DEuler[ind], u2DLax[ind], u2DRK3[ind], uExact[ind])

        figNum = 2
        fileName = "t10c1"
        plotTitle = "t = 10s and c = 1"
        ind = 1000
        """
        # vis.plot(figNum, fileName, plotTitle, label1, label2, label3, label4, x, u2DEuler[ind], u2DLax[ind], u2DRK3[ind], uExact[ind])

        # animPlot(x, u2DEuler)
        # animPlot(x, u2DLax)
        # animPlot(x, u2DRK3)
        # animPlot(x, uExact)
        vis.animPlotE(x, u2DRK3, uExact)


def exactSol(x, t, a):
    return np.sin(2 * np.pi * (x - a * t))


def Euler(u, nx, c):

    un = np.copy(u)
    for i in range(nx, 0, -1):
        u[i] = un[i] - c * (un[i] - un[i - 1])
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
