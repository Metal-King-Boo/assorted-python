# this program displays a simple pie chart
import matplotlib.pyplot as pit

def main():
    # create a list of values
    values = [20, 60, 80, 40]

    # create a pie chart from the values
    pit.pie(values)

    # display the pie chart
    pit.show()

# call the main function
main()
