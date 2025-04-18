from matplotlib import pyplot as plt


def ERPlot(model):
    for i in range(len(model.depth_model)):
        plt.plot(model.depth_model[i])
    plt.gca().invert_yaxis()
    plt.show()
