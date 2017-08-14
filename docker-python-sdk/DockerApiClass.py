'''
Author: 
  Aakar Jinwala

Description: 
  This class is an abstraction layer over Docker Python methods and its methods.
  It provides automating the tasks for docker container methods using Docker API.
  Get the log stream from the container.
  Get the log from the container.
  Get the container ID.
  Get the statistics regarding a container.

Important Note:
  This class is not full creating the containers and Not for creating docker images.
  Docker images can also be created using the Python Docker SDK. It is not my focus currently.
  For more Information about the Docker SDk for python: https://docker-py.readthedocs.io/en/stable/

Special Note:
  Three ways for creating a docker container
  1) Use Docker SDK docker run method - using detached = false - Will run container in foreground
  2) Use Docker SDK docker run method - using detached = True - Will run the container in backrgoud; returns container class object
  3) Use Docker SDK docker create method; gives container class object and then invoke start method on the container object.

  2) and 3) method gives container object
'''

import docker
from itertools import izip
import json
import datetime


class docker_sdk_abstraction():


  def __init__(self):
    '''
     <Purpose>
      Initializes the Docker API client object.
      Initializes the Docker API container class object to None. 
      container_obj will be initialized while container_create / container_run methods.
    <Arguments>
      None
    '''
    self.docker_api_obj = docker.from_env() 
    self.container_obj = None

  # Following are the Getter methods for getting Docker Api Container Object attributes

  def get_container_id(self):
    '''
     <Purpose>
      For returning the container object id attribute. id attribute is container's id
    <Arguments>
      None
    <Return>
      Returns the container ID to which the object is pointing to  
    '''  
    return self.container_obj.id

  def get_container_id_short(self):
    '''
     <Purpose>
      Get method for container object short id(truncated to 10 character) attribute.
    <Arguments>
      None
    <Return>
      Returns the 10 charcter container ID to which the object is pointing to  
    '''  
    return self.container_obj.short_id

  
  def get_container_name(self):
    '''
     <Purpose>
      Get method for container object name attribute. 
      It is by default assigned by the docker container if not specified while docker run / docker create
    <Arguments>
      None
    <Return>
      Returns the 10 charcter container ID to which the object is pointing to  
    '''
    return self.container_obj.name

  def get_container_image_name(self):
    '''
     <Purpose>
      Get method for the container's object image attribute.
    <Arguments>
      None
    <Return>
      Returns the container image name for example <Image: 'python-prog:latest'>  
    '''
    return  str(self.container_obj.image)

  def get_container_status(self):

    return self.container_obj.status

  # Following are the class methods 

  def container_create(self, docker_image_tag_name):
    '''
     <Purpose>
      Create a docker container using containers.create method.
      Inigtializes the docker API container class object.

    <Arguments>
      1) Image name for which container is to created.
      2) A Dictonary which can be used for setting up the arguments for the containers.create() method.  
    '''
    self.container_obj = self.docker_api_obj.containers.create(docker_image_tag_name) 
 

  def container_start(self):
    '''
     <Purpose>
      Invoke Docker API container class object start method.
      Starts the docker container

    <Arguments>
      None  
    '''    
    self.container_obj.start()
  
  def container_run(self, docker_image_tag_name, detach_mode):
    
    if (detach_mode == False):
      # Docker container will run on foreground
      # Output = docker container logs
      # Will not return untill container execution completes

      container_run_log = self.docker_api_obj.containers.run(docker_image_tag_name, detach=detach_mode)
      return container_run_log
    
    else:
      # Docker container won't run in foreground
      # Output of the containers.run method = Container class object

      self.container_obj = self.docker_ai_obj.containers.run(docker_image_tag_name, detach=detach_mode)

  def container_log(self):
    '''
     <Purpose>
      This method is for getting the container log after container has stopped running.
      It creates a log file with the filename as container short id + output-file.log

    <Arguments>
      None
    <Return>
      None  
    '''

    #Calling container object logs method - stream is False and Follow is True
    container_end_log = self.container_obj.logs(stdout = True, stderr = True, stream = False, follow = True) 
    
    # Formatting the log output
    container_end_log.replace("\r", "\n")

    # Creating file name
    filename = self.get_container_id_short() +"-"+self.get_container_image_name()+"-output-file.log"

    # Creating and writting into the log file
    log_file_obj = open(filename, "w+")
    log_file_obj.write(container_end_log)
    log_file_obj.close()


  def container_log_stream(self):
    '''
    <Purpose>
      This method is for getting the container log throughout the container execution.
      It creates a log file with the filename as container short id + image name + output-file.log.
      This method will return back only after the container has completed its execution. i.e. status = exited.
    <Arguments>
      None
    <Return>
      None  
    '''



    # Reloading the container object attributes, especially needed for the status
    self.container_obj.reload()

    # Creating file name for the log file
    filename = self.get_container_id_short()+"-"+self.get_container_image_name()+"-output-file.log"

    log_file_obj = open(filename, "w+")



    # Gives generator stream object helper
    log_stream = self.container_obj.logs(stdout = True, stderr = True, stream = True, follow = True)
    
    for data in izip(log_stream):

      # Reloading the container object atrributes, more concerned for container status = exited
      self.container_obj.reload()
      
      # Formatting the stream data tuple
      data = "".join(data)
      data.replace("\r", "\n")

      # Dumping the data into file
      json.dump(data, log_file_obj)  

      if(self.get_container_status() == "exited"):
        stat_file_obj.close()
        break

  def container_stats_stream(self):
    '''
    <Purpose>
      This method is for getting the statistics stream during the container execution.
      It creates a stats file with the filename as container short id + stat-file.log.
      This method will return back only after the container has completed its execution. i.e. status = exited

      Next Task would be: Manually logging cpu and memory data and calculating average over them.
    <Arguments>
      None
    <Return>
      None  
    '''

    self.get_container_process()

    # Updating the container object attributes  
    self.container_obj.reload()

    # Creating file name. 
    filename = self.get_container_id_short() +"-"+self.get_container_image_name()+"-stats-file.log"

    stat_file_obj = open(filename, "w+")

    # Gives generator stream object helper
    stats_stream = self.container_obj.stats(decode=True)
    
    for data in izip(stats_stream):

      # Updating the container object attributes, especially the container status
      self.container_obj.reload()
      
      self.get_container_process()
      
      # Dumping the stats stream data, in the file 
      json.dump(data, stat_file_obj, indent = 4)  

      # If the container has exited, close the file object and break the for loop
      if(self.get_container_status() == "exited"):
        stat_file_obj.close()
        break


  def get_container_process(self):
    processes = self.container_obj.top()
    print processes

object1 = docker_sdk_abstraction()

object1.container_create("docker-cpu-hog-i")
object1.container_start()

print object1.get_container_image_name()

#object1.container_log_stream()


object1.container_stats_stream()
object1.container_log()


#print object1.get_container_image()



#while(object1.get_container_status == "running"):
#  pass



# object1.start_container()

# print object1.get_container_name()





