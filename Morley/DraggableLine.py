# from https://stackoverflow.com/questions/34855074/interactive-line-in-matplotlib

from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import numpy as np
import TemporaryImport as ti

# add a gui
# import tkinter
# top = tkinter.Tk()
# # Code to add widgets will go here...
# top.mainloop()


def main():
    print('Entering main()')

    # subplots can do a LOT...but in this case, it just returns
    #   the Figure object and the Axes object.  We defined one Figure (fig)
    #   containing one Axes (a plot, ax).
    fig, ax = plt.subplots()

    # creates the line object, with the x-data and y-data in sequences
    line1 = Line2D([0,1], [0,1], marker = 'o', markersize = 15, markerfacecolor = 'red')
    #line2 = Line2D([1,1], [1,-2], marker = 'o', markersize = 15, markerfacecolor = 'red')

    # adds a Line2D to the list of plot lines
    ax.add_line(line1)
    #ax.add_line(line2)

    print('Before call to LineBuilder')
    linebuilder = LineBuilder(line1)
    #linebuilder = LineBuilder(line2)
    print('After call to LineBuilder')

    #  set title and axis limits
    ax.set_title('Draggable lines')
    ax.set_xlim(-2,2)
    ax.set_ylim(-2,2)


    print('Before plt.show')
    plt.show()
    print('After plt.show')



class LineBuilder(object):
    'An explanantion of the class goes right after the declaration...note the single quotes'
    print('Entering class LineBuilder')

    # this is a class variable....shared between all instances of LineBuilder
    #  can access as LineBuilder.epsilon
    epsilon = 0.2


    def __init__(self, line):
        ' this is the class constructor...always called'
        ' first argument must be self'
        ' python adds the self parameter for you... do not need to add when calling'
        ' note that the second parameter is line...which is how LineBuilder was called from main()'
        print('Entering __init__')
        # I think these are instance variables...because of the
        #     self.whatever format
        canvas = line.figure.canvas
        self.canvas = canvas
        self.line = line
        self.axes = line.axes
        self.xs = list(line.get_xdata())
        self.ys = list(line.get_ydata())

        self.ind = None

        canvas.mpl_connect('button_press_event', self.button_press_callback)
        canvas.mpl_connect('button_release_event', self.button_release_callback)
        canvas.mpl_connect('motion_notify_event', self.motion_notify_callback)


    def get_ind(self, event):
        print('Entering get_ind')
        x = np.array(self.line.get_xdata())
        y = np.array(self.line.get_ydata())
        d = np.sqrt((x-event.xdata)**2 + (y - event.ydata)**2)
        if min(d) > self.epsilon:
            return None
        if d[0] < d[1]:
            return 0
        else:
            return 1

    def button_press_callback(self, event):
        print('Entering button_press_callback')
        if event.button != 1:
            return
        self.ind = self.get_ind(event)
        print(self.ind)

        self.line.set_animated(True)
        self.canvas.draw()
        self.background = self.canvas.copy_from_bbox(self.line.axes.bbox)

        self.axes.draw_artist(self.line)
        self.canvas.blit(self.axes.bbox)

    def button_release_callback(self, event):
        print('Entering button_release_callback')
        if event.button != 1:
            return
        self.ind = None
        self.line.set_animated(False)
        self.background = None
        self.line.figure.canvas.draw()

    def motion_notify_callback(self, event):
        print('Entering motion_notify_callback')
        if event.inaxes != self.line.axes:
            return
        if event.button != 1:
            return
        if self.ind is None:
            return
        self.xs[self.ind] = event.xdata
        self.ys[self.ind] = event.ydata
        self.line.set_data(self.xs, self.ys)

        self.canvas.restore_region(self.background)
        self.axes.draw_artist(self.line)
        self.canvas.blit(self.axes.bbox)

class Temporary(object):
    print('Entering class Temporary')

if __name__ == '__main__':
    main()
