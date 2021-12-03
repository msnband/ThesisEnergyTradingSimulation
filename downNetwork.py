import os 
import time
import subprocess


cmd = "/home/moab19/HyperledgerFabric_v1/HyperledgerFabric/fabric-samples/test-network"
os.chdir(cmd)
os.system("./network.sh down")

time.sleep(1)
print()
print("Network is down...Done!")


# netstat -tulnap 
# sudo kill -9 16967

