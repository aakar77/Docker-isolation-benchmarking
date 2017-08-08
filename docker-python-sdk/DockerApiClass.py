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

'''

import docker
from itertools import izip
import json


class docker_sdk_abstraction():


  def __init__(self):
    '''
     <Purpose>
      Initializes the Docker API client object. 

    <Arguments>
      None
    '''
    self.docker_api_obj = docker.from_env() 
    self.container_obj = None

  def container_create(self, docker_image_tag_name):
    self.container_obj = self.docker_api_obj.containers.create(docker_image_tag_name) 
 

  def container_start(self):
    # docker container pbject start method, it 
    self.container_obj.start()

  """
  Either: 

  Container create and start combination 

        OR

  Container Run

  Output by run method of container : 
    container log

  Problem faced is::
    We are not getting any container object, will not return until container exists.
    Will have to rely on other methods for getting running stats of the container.

    WON'T USE CONTAINER OBJECT
  """
  
  def container_run(self, docker_image_tag_name, detach_mode):
    
    if (detach_mode == False):
      # Dokcer container will run on foreground
      # Output = docker container logs
      # Will not return untill container execution completes

      container_run_log = self.docker_api_obj.containers.run(docker_image_tag_name, detach=detach_mode)
      return container_run_log
    
    else:
      '''
      Docker container won't run in foreground
      
      containers.run() Output:
        Docker container object
      '''
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

container_log = object1.container_run("python-prog",False)
print (container_log)

# object1.start_container()

# print object1.get_container_name()





