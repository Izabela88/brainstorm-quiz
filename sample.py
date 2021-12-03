from sys import stdout
from time import sleep, time


print("START")


# for i in range(1,25):
#     stdout.write("\r%d" % i)
#     stdout.flush()
#     sleep(1)
# stdout.write("\n") # move the cursor to the next line
start_time = time()
# your code
sleep(1)
elapsed_time = time() - start_time

print("TIME IS UP!")
print(start_time)
print(elapsed_time)


