import os 
import time
import subprocess


cmd = "/home/moab19/HyperledgerFabric/fabric-samples/test-network"
os.chdir(cmd)
os.system("./network.sh down")

time.sleep(3)
print()
print("Network is down...Done!")
