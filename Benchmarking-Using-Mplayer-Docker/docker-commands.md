### General commands for creating docker images and docker containers

I am appending c as post-fix for the docker container and i as a post-fix for docker image
- For example, *docker-mplayer-i* is a docker image as *i* is appended as postfix
- Similarly, *docker-mplayer-c* is a docker container as *c* is appended as postfix

First, we have to construct the Dockerfile. After writing the Dockerfile, we have to build docker image using docker build command.
All the resources and files whose path is specified in the Dockerfile must be available or else compilation will fail 

```
sudo docker build -t docker-mplayer-i .
``` 

- In the above docker command -t is used for tagging docker image with a name, which is more convenient as compared to docker image id 

Second, after building the image, we need to create a container with docker run command

```
sudo docker run --name docker-mplayer-c1 docker-mplayer-i
```
- Here -name command is used for naming the container with a name which is more convenient in comparison to docker container id

Memory for a container can be limited using the option -m
```
sudo docker run --name docker-mplayer-c1 -m 100M docker-mplayer-i
```
Container can also be restricted to run on only one core using
```
sudo docker run --name docker-mplayer-c1 --cpuset-cpus 1 docker-mplayer-i
``` 
A running container can be stopped using the command
```
sudo docker stop docker-mplayer-c1
```
- A container which is already running cannot be deleted. 

For deleting a container, which is not currently being running:
```
sudo docker rm docker-mplayer-c1
```
For deleting docker images which are stored in the local registry
```
sudo docker rmi docker-mplayer-i
```
Real time container metrics can be obtained using the command
```
sudo docker stats
```

### Commands used for creating docker-mplayer image and container 

```
sudo docker build -t docker-mplayer-i .

sudo docker run --name docker-mplayer-c1 --cpuset-cpus 1 -m 400M docker-mplayer-i
```

- I am limiting memory requirement of mplayer docker container to 400 MB and running it on cpu core 1

### Commands used for creating docker memory-cpu-hog image and container

```
sudo docker build -t docker-cpu-memory-hog-i .

sudo docker run --name docker-memory-cpu-hog-c1 --cpuset-cpus 1 -m 400M docker-cpu-memory-hog-i
```
- I am limiting memory requirement of cpu-memory-hog docker container to 400 MB and running it on cpu core 1

That means, I am limiting both the mplayer and cpu memory hog to core 1 (i.e. same cpu core)


