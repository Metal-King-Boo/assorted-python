# problem 1
# allow a user to store the daily sales up to a week
# calculate the total sales from it

def main():
    weeklySales = [0, 0, 0, 0, 0, 0, 0]
    for i in range(7):
        dailySale = float(input("Input Day " +  str(i + 1) + "\'s sales: "))
        weeklySales[i] = dailySale

    weeklyTotal = 0
    for i in weeklySales:
        weeklyTotal += i

    print("The weekly total sales is $" + str(weeklyTotal))

main()