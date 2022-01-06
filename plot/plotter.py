import matplotlib.pyplot as plt


class Plotter:
    """Wrapper class for pyplot"""

    def __init__(self):

        # plt.style.use(["dark_background"])
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot()
        self.ax.grid(False)
        # self.ax.set_title("Delaunay Trangulation")

    def plotPoints(self, ps):
        """takes an 2d array [[xs], [ys]] and scatterplots is on the plane"""
        self.ax.scatter(ps[0], ps[1], color="w")

    def plotLines(self, ls):
        """
        takes an array [[xs], [ys] for qe in qes]
        and lineplots is on the plane
        """

        for line in ls:
            self.ax.plot(line[0],
                         line[1],
                         color="darkgrey",
                         alpha=0.8,
                         linewidth=0.7)

    def save(self, savePath=None):

        if not savePath:
            plt.show()
        else:
            plt.savefig(savePath, dpi=300)
        # plt.show()
        plt.close()
