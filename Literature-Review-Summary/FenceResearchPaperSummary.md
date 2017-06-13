# [Fence: Protecting Device Availability With Uniform Resource](https://ssl.engineering.nyu.edu/papers/li-usenix-fence-2015.pdf)  Research Paper Summary

In this report, I am summarizing my understanding of Resource manger - Fence which is used in the Seattle-Testbed. I am also focusing more on the evaluation section of the research paper, in which already existing solutions like nice, ionice, cpu-freq performance are  compared against Fence. 

## What is Fence?

- Fence is resource control subsystem for Sandboxed environment. 
- It focuses on solving the resource availability problem, which arises when multiple resource intensive applications are running parallelly. 
- Fence is a solution for resource control by providing the protection against hog - applications along with limiting battery drain, overheating and improving resource allocation to various applications. 

## What are hog-applications?

- An application can be considered as a hog-application, if it is having characteristics of acquiring/ attempt to acquire multiple resources quickly at a time resulting into exacerbating the resource allocation process and limiting resource availability to other applications.

## How are resources classified as?

Resources are classified on the basis of two dimensions, as whether they are fungible or non - fungible, renewable or nonrenewable.
 
- **_Fungible resources_** are those resources which are interchangeable and they can be quantified. Their usage by an application can be limited by quota. When the application requests for a fungible resource, if the application usage for that resource has not exceeded the quota, the resource can be granted else application’s process requesting the resource can be suspended or blocked depending upon whether the asked resource is renewable or nonrenewable resource.

-  For **_non-fungible resources,_** when an application requests a resource instance, its further usage will be automatically blocked for other applications. They are reserved for an application, even when the application is not running.

- **_Renewable resources_** automatically replenished over a period of time, say CPU - cycles.

- **_Non-renewable resources_**  are like memory, file descriptors or persistent storage which is acquired by the application. So granting non-renewable resources is allocating a resource to an application permanently or allocating a resource for a longer duration, although an application can voluntarily decide to release the resource. 

Once the resources are allocated, Fence makes use of a table maintaining which resources are allocated to monitor their update requests and its releases. Also, it can block the resource if the application is asking for more quantity of a resource which is greater than the allocated quota dedicated for its usage.

## How Fence is implemented? 
Fence code is written in Python and it is majorly divided into two parts Uniform Resource Control code (140 lines of code) and Operating system specific code which is of about (650 lines of code).

- **_Uniform Resource Control_** code is majorly similar for all platforms. Off course, for few platforms some code needed to be added with URC code for proper support and functioning of URC on that platform. 
- Provides various methods for different types of resources like whether UDP port can be consumed or not, calls for charging bandwidth consumption.
- The remaining code of Fence is **_Operating System Specific Code_** ( apporx, 650 lines of code) is target platform specific code, which contains necessary support for polling, signalling, enforcing restrictions for resources.

## How Fence provides resource isolation to control resources?
Fence resource isolation capability totally depends upon the type of resource. It makes use of two mechanisms for controlling resources viz. (1) Call interposition (2) polling and signalling.
 
Call interposition requires Fence to be called each and every time when the application consumes a resource. There are four strategies regarding when the resource control of Fence should be applied.
- Pre-call strategy: Resource control is imposed before the application tries to consume resource or before it makes a call for consuming resource. Best suited for non-renewable resources.
- Post-call strategy: Application is charged after it consumes resource or makes call for resource consumption. This has drawbacks of application acquiring many resources before resource control is imposed on it. Application may monopolize particular resource. Can be used with fungible resources which are renewable.
- Pre and Post call strategy:  Pre call utility will block the resource until resource usage from previous calls have been replenished or not. If not, application/process will be blocked until the resources are replenished again. The application is charged after it makes necessary calls for resource requests. This is most widely used strategy used with Fence and it works with both the systems.

 
## How Fence provides resource isolation for CPU and memory?
- Usage statistics on memory and CPU are polled from operating system, as fence does not implement its own scheduling for these resources. OS scheduler process scheduling.
- Fence needs to poll and understand about how process has been scheduled. It has to signal the scheduler for stopping and executing the applications.
- There are overhead associated with polling. Fence can overload the CPU for polling.
- How often Fence polls CPU? i.e. the rate of checking and control. If the rate of checking is very low, drawback is the process can overspend resources between checks and so Fence would not be able to control the resource properly. If the rate of checking is high, it can interfere with normal execution of the CPU and can incur high overhead to CPU.
 
## How Seattle makes use of Fence?
- Every devices running Seattle makes use of Fence for allocating a fixed percentage of resources such as CPU, memory, disk. Resources can be allocated to one or more VMs.
- Calls to network and disk devices are re-routed through Fence. While for CPU and memory, it has to use polling and signalling mechanism.
- Fence provides a capability to choose a resource limit for fungible resource
- There is hard maximum limit imposed for memory and CPU usages on Seattle. This means when the process tries to exceed the limit will be killed.

## How resource isolation provided by Fence evaluated?  (Main Section of my concern)
- For evaluating the resource isolation of Fence, the performance of Fence is compared with the standard solutions which are already implemented on various platforms such as:
- **_nice_** - sets scheduling priority for a process
- **_ionice_** - sets io priority 
- **-_ulimit_** - impose hard limits on overall computation of a resource like file size, CPU time, stack size.
- **_cpufreq-set_** - helps in changing the cpu frequency and through which one can also slow down the processing speed of cpu
- The experiment setup is running a simulated hog application along with VLC player which is trying to decode a HD video.
- As discussed above, the simulated hog process tries to acquire the specific type of resource as quickly as possible. For example, CPU-hog will try to go into infinite loop, memory hog will try to acquire maximum memory as it can. Also, an ‘everything hog’ is created which tries to acquire all the resources such as network bandwidth, memory, storage IO, CPU. 

### Testing performance degradation: 
- Here the everything-hog is parallely run along with VLC player decoding a 1080 H.264 video. 
VLC player is set to have the maximum possible priority. 
- For the performance metric, proportion of frames decoded by the player during above experiment setup is taken into consideration. 
- Performance of Fence is superior in comparison to nice, ionice, ulimit and cpufreq-set and combine application of all. Also, the performance of everything hog was also not impacted by resource limiting policy of Fence. 

### Control of Power and Heat:
- Here the main focus is to control the rate of power consumption and heat produced by running the everything hog application. As discussed in the paper 
- This experiment is performed by running the everything hog application for 10 minutes followed by examining the ACPI battery and temperature.
- An important fact to note is, cpufreq-set is most effective among ionice, nice, ulimit but by reducing the frequency, it failed to provide resource isolation for other resources. Which means, attempting to control one resource, can negatively impact other resources too.
- Fence performance is effective in controlling battery consumption, better than cpufreq-set.

### Effectiveness on Diverse platforms:
The main aim is here to test whether uniform-resource control is effective to run on diverse platforms or not.
Five benchmark tests are performed on Seattle platform against everything hog with no restrictions and under Fence’s control: 
- HTTP server serving a large file, 
- Amazon S3
- HTTP server benchmark with small files/ directory entries 
- UDP P2P messaging program 
- Richard’s benchmark 
 
## What i need to perform for Docker?
- As Fence is implemented as resource manager for Seattle, cgroups (control groups) provides resource isolation for docker containers. I need to implement similar experiments which are mentioned in the section 5 of the paper and as mentioned above which are performed for evaluating Fence. 
 
## How I am going to perform for docker? What plan I have thought of?
- I am planning to create a docker container by including the hog application code (Python) in the container. 
- I will be reusing the code written for memory hog application and running hog application under the python container along with running a video decoding application i.e. VLC player. 
- I am yet to devise the proper plan. Will be updating the plan after a meeting with my professors


























