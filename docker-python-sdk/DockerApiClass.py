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
  1) Use Docker SDK docker run method  - using detached = false - Will run container in foreground
  2) Use Docker SDK docker run method - using detached = True - Will run the container in backrgoud; returns container class object
  3) Use Docker SDK docker create method; gives container class object and then invoke start method on the container object.

  2) and 3) method gives container object
'''

import docker
from itertools import izip
import json


class docker_sdk_abstraction():


  def __init__(self):
    '''
     <Purpose>
      Initializes the Docker API client object.
      Initializes the Docker API container class object to None. 

    <Arguments>
      None
    '''
    self.docker_api_obj = docker.from_env() 
    self.container_obj = None

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
      # Dokcer container will run on foreground
      # Output = docker container logs
      # Will not return untill container execution completes

      container_run_log = self.docker_api_obj.containers.run(docker_image_tag_name, detach=detach_mode)
      return container_run_log
    
    else:
      # Docker container won't run in foreground
      # Output of the containers.run method = Containe class object
      
      self.container_obj = self.docker_api_obj.containers.run(docker_image_tag_name, detach=detach_mode)

  def container_stats_stream(self):
    pass    


  def container_log_stream(self):
    pass


  def container_log(self):
    pass


  def get_container_process(self):
    pass



  # Following are the Getter methods for getting Docker Api Container Object attributes

  def get_container_id(self):

    return self.container_obj.id
  
  def get_container_name(self):

    return self.container_obj.name

  def get_container_image(self):

    return self.container_obj.image

  def get_container_status(self):

    return self.container_status



object1 = docker_sdk_abstraction()

container_log = object1.container_run("python-prog", False)
print (container_log)

# object1.start_container()

# print object1.get_container_name()





