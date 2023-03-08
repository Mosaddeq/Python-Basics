import datetime

u_input = input("enter goal and date separated by :\n")

input_list = u_input.split(":")

goal = input_list[0]

deadline = input_list[1]

deadline_date = (datetime.datetime.strptime(deadline,"%d.%m.%Y"))

#calculate how many days from now till deadline

print("Today is: ",datetime.datetime.today())

print("Deadline is:",deadline_date)

remaining_time = deadline_date - datetime.datetime.today()

print("Remaining time is:", remaining_time)


