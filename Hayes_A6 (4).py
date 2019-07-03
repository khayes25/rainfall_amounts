"""
See instructions in CSCI111_A6.pdf

Be sure to rename this file Lastname_A6.py, using your last name
in place of "Lastname".

Your name: Keon Hayes

"""

months = 12 								    #A months variable is created to represent the number of months.
rainfall = []                                                               #Creating a list to store monthly rainfall data.

for i in range(1, months + 1) :                                             #Loop 12 times for each of the 12 months.
    print("Please enter the rainfall amount for month", i, end="")          #Prompt user for rainfall amount for the month.
    temp = float(input(": "))                                               #The input will be stored to the temp variable before it can populate the list.
    while temp < 0 :                                                        #The value of the temp variable will be tested for a non-negative number.                            
        print("Invalid amount. Try again.")                                 #If it is negative, an error message will be displayed.
        print("Please enter the rainfall amount for month", i, end="")      #The user will be prompted again for the rainfall amount.
        temp = float(input(": "))                                           #The input will be stored to the temp variable before it can populate the list.
    rainfall.insert(i, temp)                                                #The valid input for each month will populate the list.
									    #Repeats until the user enters a valid answer.

min = 0                                                                     #A min variable is created and set to the first element. This variable is an index.

for i in range(1, len(rainfall)) :                                          #Each element of the list will be tested, starting with the second element.
    if rainfall[i] < rainfall[min] :                                        #Testing if the element is lower than the minimum.
     min = i                                                                #If it is, replace the minimum with the new element.

max = 0                                                                     #A max variable is created and set to the first element. This variable is an index.

for i in range(1, len(rainfall)) :                                          #Each element of the list will be tested, starting with the second element.
    if rainfall[i] > rainfall[max] :                                        #Testing if the element is lower than the minimum.
        max = i                                                             #If it is, replace the minimum with the new element.

								            #The sum is needed to find the average.
sum = 0                                                                     #A sum variable is created and set to 0.

for i in range(len(rainfall)) :                                             #Loop through the entire list, including every element.
    sum = sum + rainfall[i]                                                 #Add each element to the sum.

avg = sum / months                                                          #Dividing the sum by the number of months to get the average.

print("The total rainfall is", format(sum, ".2f"), "inches.")               #The value of the sum variable is printed, rounded to two decimal places.
print("The average monthly rainfall is", format(avg, ".2f"), "inches.")     #The value of the avg variable is printed, rounded to two decimal places.
print("The month with the most rainfall was month ", max + 1, ".", sep="")  #1 is added to the value of the max variable then printed. This is because the index counting starts from 0.
print("The month with the least rainfall was month ", min + 1, ".", sep="") #1 is added to the value of the min variable then printed. This is because the index counting starts from 0.
