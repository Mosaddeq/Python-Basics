def calculate_days_to_mins(num_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_days} days are {num_days * 24} hours "
    elif conversion_unit == "mins":
        return f"{num_days} days are {num_days * 24 * 60} minuites "
    elif conversion_unit == None:
        return "unsupported unit"
u_input= ""

def validate_input():
    try:
        user_input_number= int (days_to_unit_dict["days"])
                    
        if user_input_number>0:
            calculated_value= calculate_days_to_mins(user_input_number,days_to_unit_dict["units"])
            print(calculated_value)
        elif user_input_number == 0:
            print("number cant be 0")
        elif user_input_number<0:
            print("number cant be negative")
    except:
        print("Enter a integer value")

while True:
    u_input = input("Enter you numbers:\n")

    if u_input == "exit":
        break
    else:
        try:
            days_and_unit = u_input.split(" ")

            days_to_unit_dict = {"days": days_and_unit[0] ,"units": days_and_unit[1] }
            print(days_to_unit_dict) 
            validate_input()
        except:
            print("enter unit of conversion")
              