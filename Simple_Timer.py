import time
import winsound

print("Set a timer: ")
min = int(input("Enter minutes: "))
sec = int(input("Enter seconds: "))
N = 1 #duration of 1 second. created to manipulate speed.

a = [min,sec] #to store the values before manipulation.

for i in range(min,-1,-1):
    for j in range(sec,-1,-1):
        if i == 0 and j == 0: #case where time is complete. it skips 00:00 it breaks the loop.
            break
        print(str(i).zfill(2)+":"+str(j).zfill(2)) #str(sec and min) is always 2 wide.
        winsound.Beep(1000,150)
        time.sleep(N)
        if j == 0 and i != 0: #case where seconds is 0 but mins is still not 0. secs turn to 59.
            sec = 59
            continue

min,sec = a[0], a[1]
print(str(min)+" minutes "+str(sec)+" seconds complete!.")

for i in range(10):
    winsound.Beep(500,500)
    winsound.Beep(500,500)
    time.sleep(1)








