# this program displays a sales chart
import matplotlib.pyplot as pit

def main():
    # create a list with the X coordinates of each bar's left edge
    left_edge = [0, 10, 20, 30, 40]

    # create a list with the height of each bar
    heights = [100, 200, 300, 400, 500]

    # create a variable for the bar width
    bar_width = 10

    # build the bar chart
    pit.bar(left_edge, heights, bar_width, color=('r', 'g', 'b', 'w', 'k'))

    # add a title
    pit.title('Sale by Year')

    # add labels to the axes
    pit.xlabel('Year')
    pit.ylabel('Sales')

    # customize the tick marks
    pit.xticks([5, 15, 25, 35, 45], ['2016', '2017', '2018', '2019', '2020'])
    pit.yticks([0, 100, 200, 300, 400, 500], ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m',])

    # display the bar chart
    pit.show()

# call the main function
main()