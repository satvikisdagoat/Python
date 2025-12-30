import time

alarm = input("set alarm in HH:MM:SS format:")

while True:
    current_time = time.strftime("%H:%M:%S")
    print ("current time is:", current_time)
    if current_time == alarm:
        print("Wake up kid")
        break
    time.sleep(1)
