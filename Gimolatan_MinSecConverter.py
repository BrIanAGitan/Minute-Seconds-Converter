# Enter
ammount_time = int(input("Enter an integer in seconds: "))

# Calculate minutes and seconds
minutes = ammount_time // 60
seconds = ammount_time % 60

# Display the result and i dont know why in all letters why F/f is the one able to do like that
print(f"{ammount_time}seconds is {minutes} minutes and {seconds} seconds.")
