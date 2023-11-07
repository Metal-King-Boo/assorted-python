# this program displays a simple pie chart
import matplotlib.pyplot as pit

def main():
    # create a list of sales amounts
    sales = [100, 400, 300, 600]

    # create a list of labels for the slices
    slice_labels = ['1st Qtr', '2nd Qtr', '3rd Qtr', '4th Qtr']

    # create a pie chart from the valies
    pit.pie(sales, labels=slice_labels)

    # add a title
    pit.title('Sales by Quarter')

    # display the pie chart
    pit.show()

# call the main function
main()