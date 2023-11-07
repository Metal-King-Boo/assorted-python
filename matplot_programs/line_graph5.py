# this program displays a simple line graph
import matplotlib.pyplot as pit

def main():
    # crete lists with the X and Y coordinates of each data point
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    # build the line graph
    pit.plot(x_coords, y_coords)

    # add a title
    pit.title('Sales by Year')

    # add a labels to the axes
    pit.xlabel('Year')
    pit.ylabel('Sales')

    # customize the tick marks
    pit.xticks([0, 1, 2, 3, 4], ['2016', '2017', '2018', '2019', '2020'])
    pit.yticks([0, 1, 2, 3, 4, 5], ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])

    # add a grid
    pit.grid(True)

    # display the line graph
    pit.show()

# call the main function
main()