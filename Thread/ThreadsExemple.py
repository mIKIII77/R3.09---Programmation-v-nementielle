import threading
import time 

# ------------------------------------------------------------
def task(i): # i is the thread number
    print(f"Task {i} started") # print the thread number when it starts
    time.sleep(2) # sleep for 2 seconds to simulate a long-running task
    print(f"Task {i} finished") # print the thread number when it finishes
# ------------------------------------------------------------

start = time.perf_counter() # start time variable
end = time.perf_counter() # end time variable

t1 = threading.Thread(target=task, args=[1]) # Create a thread
t2 = threading.Thread(target=task, args=[2]) # Create a thread

t1.start() # start the thread
t2.start() # start the thread

t1.join() # wait for the thread to finish
t2.join() # wait for the thread to finish

end = time.perf_counter() # end time variable

print(f"Total time taken: {round(end-start, 2)} second(s)") # print the total time taken 

if __name__ == "__main__":
    pass