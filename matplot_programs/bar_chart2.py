# this program displays a simple bar chart
import matplotlib.pyplot as pit

def main():
    # create a list with the X coordinates of each bar's left edge
    left_edges = [0, 10, 20, 30, 40]

    # create a list with the heights of each bar
    heights = [100, 200, 300, 400, 500]

    # create a variable for the bar width
    bar_width = 5

    # build the bar chart
    pit.bar(left_edges, heights, bar_width)

    # display the bar chart
    pit.show()

# call the main function
main()