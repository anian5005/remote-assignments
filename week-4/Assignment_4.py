import time
import threading
import queue

job_queue = queue.Queue()

# We create 9 jobs with job_index 1 ~ 9
for job_index in range(1, 10): 
    job_queue.put(job_index)

class Worker(threading.Thread):
    def __init__(self, worker_num):
        threading.Thread.__init__(self)
        self.worker_num = worker_num

    def run(self):
        while job_queue.qsize() !=0: #cant use for loop with  job_queue ,size of job_queue changes with time, it decrease because 3 worker do-job together
            self.do_job(job_queue.get())

    def do_job(self, index):
         # Simulate a job (you can image it as doing something which need to take 1 second)
        print(f"worker {self.worker_num} start job {index}")
        time.sleep(1)
        print(f"worker {self.worker_num} finish job {index}")


workers = []
worker_count = 3 # We have 3 workers

for i in range(worker_count):
    worker = Worker(i+1)
    workers.append(worker)
    
    
# Do the job
for worker in workers:
    worker.start()


for worker in workers:
    worker.join()

print("Done.")