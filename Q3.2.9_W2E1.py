# There are a few methods.
# This is a nice method adapted from a student solution
# Note you could also use: from datetime import datetime
# To make your imports shorter

current_hour = datetime.datetime.now().hour
current_minute = datetime.datetime.now().minute
current_time = int(str(current_hour)+str(current_minute))

print("The current time is:", current_time)
if current_time >= 100 and current_time < 400:
    print("Go to sleep!")
elif current_time >= 800 and current_time < 900:
    print("Eet je hagelslag!")
else:
    print("Gut gemacht!")