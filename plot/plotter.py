from mpl_toolkits.mplot3d import axes3d
import mpl_toolkits.mplot3d as mpl3d
import matplotlib.pyplot as plt

class Plotter:
    """Wrapper class for pyplot"""

    def __init__(self):

        plt.style.use(['dark_background'])
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot()
        # self.ax.xaxis.pane.set_edgecolor('black')
        # self.ax.yaxis.pane.set_edgecolor('black')
        # self.ax.zaxis.pane.set_edgecolor('black')
        self.ax.grid(False)
        self.ax.set_title('Delauney Trangulation')

    def plotPoints(self, ps):
        """takes an 2d array [[xs], [ys]] and scatterplots is on the plane"""
        self.ax.scatter(ps[0], ps[1],
                color='w')

    def plotLines(self, ls):
        """takes an array [[xs], [ys] for qe in qes] and lineplots is on the plane"""
        for l in ls:
            self.ax.plot(l[0], l[1]
                    , color='grey'
                    , alpha=0.8
                    , linewidth=0.7
                    )

    def save(self, savePath=None):

        if not savePath:
            plt.show()
        else:
            plt.savefig(savePath, dpi=100)
        # plt.show()
        plt.close()
