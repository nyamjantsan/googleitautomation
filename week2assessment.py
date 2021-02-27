#!/usr/bin/env python
from multiprocessing import Pool
import subprocess
def run(task):
 src = "/home/student-01-d2fda15c29ec/data/prod/{}/".format(task)
 dest = "/home/student-01-d2fda15c29ec/data/prod_backup/{}/".format(task)
 #print(src)
 #print(dest)
 subprocess.call(["rsync", "-arq", src, dest])
if __name__ == "__main__":
  tasks = ['alpha', 'beta', 'delta', 'gamma', 'kappa', 'omega', 'sigma']
  # Create a pool of specific number of CPUs
  p = Pool(len(tasks))
  # Start each task within the pool
  p.map(run, tasks)
