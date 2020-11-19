import matplotlib.pyplot as ptl
import sympy as sp

def matplotlibPlot(x: str, y: str):

    x = x.replace(']', '').replace('[', '')
    x = x.split(',')
    for i in range(len(x)):
        x[i] = int(x[i])

    y = y.replace(']', '').replace('[', '')
    y = y.split(',')
    for i in range(len(y)):
        y[i] = int(y[i])

    print(type(x))
    print(type(y))

    if len(x) != len(y):
        return False

    ptl.plot(x, y)
    ptl.savefig('wolfy_plot.png')
    ptl.close()
    return True


def sympyPlot(y:str):
    y = sp.sympify(y)
    sp.plot(y,show=False).save('wolfy_plotf.png')
    print(y)
    return True