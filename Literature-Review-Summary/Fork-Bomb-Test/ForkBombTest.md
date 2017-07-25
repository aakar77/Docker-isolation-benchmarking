# Experiments with docker containers 

In this report, I am summarizing my understanding of Resource manger - Fence which is used in the Seattle-Testbed. I am also focusing more on the evaluation section of the research paper, in which already existing solutions like nice, ionice, cpu-freq performance are  compared against Fence. 

## Experiment with Fork Bomb Test

- Fence is resource control subsystem for Sandboxed environment. 
- It focuses on solving the resource availability problem, which arises when multiple resource intensive applications are running parallelly. 
- Fence is a solution for resource control by providing the protection against hog - applications along with limiting battery drain, overheating and improving resource allocation to various applications. 


## Useful resources which I found on the internet

- https://www.cloudsigma.com/manage-docker-resources-with-cgroups/


- https://goldmann.pl/blog/2014/09/11/resource-management-in-docker/

- https://docs.docker.com/engine/admin/resource_constraints/
- https://docs.docker.com/engine/admin/runmetrics/#enumerating-cgroups
- https://www.kernel.org/doc/gorman/html/understand/understand016.html
- https://superuser.com/questions/294771/what-is-kernel-memory-what-function-does-it-serve

-- The 'kernel' is the core bit of the operating system - the part that lets you talk to the hardware, the part that actually does the 'operating' as it were.

-Kernel memory, accordingly, is reserved for the parts of the operating system that have to stay in memory (which as you can see is comparatively not all that much) and is off-limits to any other software to prevent any accidents from, say, a badly-written app trying to access memory that's in use elsewhere. (Some bits of the OS can be paged, and you see that reflected there, but that's a bit misleading terminology.)

- https://stackoverflow.com/questions/26841846/how-to-allocate-50-cpu-resource-to-docker-container

- https://github.com/docker/labs/tree/master/security/cgroups
- https://www.cloudsigma.com/manage-docker-resources-with-cgroups/
- http://events.linuxfoundation.org/sites/events/files/slides/cgroups_0.pdf
- https://asciinema.org/a/19482


- https://github.com/wsargent/docker-cheat-sheet














