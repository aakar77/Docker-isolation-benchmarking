import docker
from itertools import izip
import json



# Method 1 of creating and running the containers without docker run command.

#client = docker.APIClient(base_url='unix://var/run/docker.sock')

clientAPI = docker.from_env()

cLogFileObj = open("pyProContainerOutput.txt", "w+")
containerStat = open("pyProContainerStat", "w+")

containerObj = clientAPI.containers.create('python-prog') # Creating a container with an image
containerObj.start()


while(containerObj.start)

cLogString = containerObj.logs() # Getting Container output as a string
print cLogString

cLogFileObj.write(cLogString)
cLogFileObj.close()

"""

cLogDict = containerObj.logs(stdout=True, stderr=True, stream=True)


while(containerObj.status != "exited"):

  try:
    for tup in izip(cLogDict):
      text = "".join(tup)
      text.replace("\r", "\n")
      cLogFileObj.write(d)
     
  except KeyboardInterrupt:
    cLogFileObj.close()
    containerObj.stop()
    containerObj.remove() 

cStatsDict = containerObj.stats(decode=True)

#Dumping the stats api method output for a docker container

while(containerObj.status != "exited" and containerObj.status == "running"):

  try:
    for a in izip(cStatsDict):
      json.dump(a,containerStat,indent = 4)
      
  except KeyboardInterrupt:
    containerStat.close()
    
'''
	



containerObj.remove() 



'''
#print ''.join(z)
#for x in z:
#       yield z
#      next(z)

#print(x)

#container_id = 
# Starting the container
# y = containerObj.top()
#

#for z in y:
#	print z
#print(y)



#client = docker.from_env()
# containerLog = client.containers.run('python-prog')
# containerObj = client.containers.get(containerId)
#f = open("docker-mplayer-logs.txt","w+")
#f.write(log)
"""