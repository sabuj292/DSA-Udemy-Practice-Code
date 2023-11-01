
# Calculate Average Temperature

# without using array or list data structure


# numDays = int(input("How many day's temperture? "))
# total = 0
# for i in range(1, numDays+1):
#     nextDay = int(input("Day " +str(i) + "'s high temp: "))
#     total += nextDay

# avg = round(total / numDays, 2)

# print("\nAverage = ",str(avg))



# using List data structure 

numDays = int(input("How many day's temperture? "))
total = 0
temp = []
for i in range(numDays):
    nextDay = input("Day " +str(i+1) + "'s high temp: ")
    nextDay = int(nextDay)
    temp.append(nextDay)
    total += temp[i]

avg = round(total / numDays, 2)

print("\nAverage = ",str(avg))

# number of day's temperature that is above the average value

above = 0
for i in temp:
    if i>avg:
        above +=1

print(str(above), "day(s) above the average")
 