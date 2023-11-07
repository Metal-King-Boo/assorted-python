# this program displays a simple line graph
import matplotlib.pyplot as pit

def main():
    # create lists with the X and Y coordinates of each data point
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    # build the line graph.
    pit.plot(x_coords, y_coords)

    # display the line graph
    pit.show()

# call the main function
main()