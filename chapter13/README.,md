# Chapter 13 Deploying Applications

## NIST (SP) 800-145 What is the cloud

* Broad Network Access - Services are available over the network and accessed via standard protocols on any type of client (Mobile phone, tablet, desktop, etc.)
* Rapid elasticity: Capacity can be automatically provisioned and decommissioned to scale the service to demand. 
* Measured service: Cloud systems measure resource utilization (compute, storage, and network) and charge for those services accordingly. Utilization is monitored, controlled, and reported on, allowing transparency for the service provider and customer. 
* On-demand self-service: The cloud consumer can provision compute, storage, and network as needed, without human interaction, through automation or self-service portals. 
* Resource pooling: The infrastructure is a common pool of resources that can serve multiple customers at the same time. The customer does not interact with the underlying hardware, and workloads can be moved within the cloud environment based on demand without the end user knowing or needing to be involved. 
Kindle Locations 9294-9300). 

## Service Models
* Software as a service (SaaS): A service provider hosts, manages, and controls an application and offers it to the customer to use. The customer does not interact at all with the underlying infrastructure, operating systems, storage, or network. There may be some customization capabilities, but they are usually limited to application-specific configuration. What you see is what you get. 
* Platform as a service (PaaS): A PaaS provider supplies a fully integrated service/software suite, and customers can deploy their applications on top of this suite with a predefined set of application programing interfaces, libraries, software development kits, and/or other tools and services. Customers can program the application in any way they choose and can customize it directly to their own workflow, as long as the customization is within the parameters of the service provider’s offering. Customers do not have to worry about integration of the underlying infrastructure components, and in the case of a managed PaaS service, have no management responsibilities for the underlying infrastructure. 
* Infrastructure as a service (IaaS): A provider enables the customer to provision compute, storage, and networking to run any combination of software and operating systems. While customers have no control of the underlying infrastructure hardware platform, they have full control over the software and services they deploy within the cloud service. The customer is also responsible for the maintenance of the software they deploy, including patching and upgrading. 


* Private Cloud
* Public Clouod
* Hybrid Cloud
* Community Cloud

## Edge or Fog Computing
With the increase in IoT applications, devices, and sensors, the various deployment models covered so far are just not up to the task of handling the sheer volume of data being created and needing to be processed. 

This sea of data cannot be consumed and processed by a centralized cloud application, given the cost of transporting the data and the latency involved in receiving information back to do anything with it. Your self-driving car would run into a ditch before a cloud service could detect and respond. 
(Kindle Location 9362). 

## Application Deployment Methods 
What is IT’s value to the business if you boil it down to the simplest aspect? IT is charged with supporting and maintaining applications that the business relies on. No one builds a network first and then looks for applications to stick on it. 
(Kindle Locations 9373-9375). 

### Bare-Metal Application Deployment </br>
The traditional application stack, or bare-metal, deployment is fairly well known. 

### Virtualized Applications  
Virtualization was created to address the problems of traditional bare-metal server deployments where the server capacity was poorly utilized. The idea with virtualization is to build one large server and run more than one application on it. Sounds simple, right?  


### Cloud-Native Applications 
Cloud-native, or microservice, applications represent the further intersection and evolution of virtualization and a cloud environment. As virtualization became popular, application developers started to ask themselves why they needed a heavy operating system to run their applications. All the patching, drivers, and configuration requirements don’t go away just because you load a virtual machine. 

### Containers
The benefits of containers are as follows: 
* Consistency for deployment automation 
* Simplified lightweight image files measured in megabytes (whereas VM files are measured in gigabytes) 
* Providing only what the app needs and nothing else 
* Ability to work the same in production as on a developer’s laptop 
* Open community-built best-of-breed containers for faster innovation 
* Ability to deploy applications in seconds 
(Kindle Locations 9426-9430). 


DevOps
* Culture: For DevOps to work, organizational culture must change. This is by far one of the most difficult aspects to embrace, but it is the single most important factor for success. DevOps requires a culture of sharing. 
* Automation: While DevOps is more than just a set of software tools, automation is the most easily identifiable benefit. Automation techniques greatly speed up the deployment process, enable defects to be caught and corrected earlier, and eliminate the need for human intervention in repetitive tasks. * Lean: Reducing wasted efforts and streamlining the process are the goals of Lean. It’s a management philosophy of continuous improvement and learning. 
* Measurement: Unless you measure your results, you can never improve. Success with DevOps requires the measurement of performance, process, and people metrics as often as is feasible. 
* Sharing: DevOps requires a culture of feedback and sharing. Breaking down silos and creating an inclusive shared fate environment is the ultimate goal. 
(Kindle Locations 9515-9522). 

The whole point is to reduce wasted time on rework. 
Kindle Location 9556). 

The following are the key characteristics of the first way: 
* Make work visible 
* Reduce batch sizes 
* Reduce intervals of work 
* Build in quality by preventing defects from being passed downstream 
* Constantly optimize for business goals 
(Kindle Locations 9558-9561). 

Second Way
One of the things you will see repeatedly in DevOps is analogies to manufacturing. Since so much of this management philosophy is derived from Lean and the Toyota Production System, concepts like defect prevention are front and center in the approach. 
(Kindle Locations 9562-9564). 

If something isn’t working, you have to make sure that it doesn’t happen again so you don’t end up on a hamster wheel of pain. 
(Kindle Locations 9565-9566). 

Third Way
The following are the key characteristics of the third way: 
* Conduct dynamic, disciplined experimentation and risk taking 
* Define time to fix issues and make the system better 
* When things go wrong, don’t point fingers 
* Create shared code repositories 
(Kindle Locations 9591-9593). 


DevOps Implementation 
Implementing DevOps technical practices within an organization typically involves three stages. These stages follow a natural progression that leads to a fully automated code-to-deployment operational model: 

*Continuous integration: This stage involves merging development work with the code base constantly so that automated testing can catch problems early. 
* Continuous delivery: This stage involves a software package delivery mechanism for releasing code to staging for review and inspection. 
* Continuous deployment: This stage relies on continuous integration and continuous delivery to automatically release code into production as soon as it is ready.
(Kindle Locations 9594-9601). 

https://xebialabs.com/periodic-table-of-devops-tools/ 
(Kindle Location 9606). 

For technologists, it’s easy to focus on the tools and technology, but honestly that’s the easy part of DevOps. Changing culture and implementing Lean methodologies are where many companies have struggled. Focus on streamlining your processes and implement technologies that help accelerate your efforts. 

Chris Jackson; Jason Gooley; Adrian Iliesiu; Ashutosh Malegaonkar. Cisco Certified DevNet Associate DEVASC 200-901 Official Cert Guide (Ken Beck's Library) (Kindle Locations 9644-9646). 


## Docker

Namespaces
Namespaces are essential for providing isolation for containers. Six namespaces are used for this purpose: 
* mnt (mountpoints): This namespace is used for mapping access to host operating system storage resources to the container process. 
* pid (processes): This namespace is used to create a new process ID for an application. 
* net (networks): This namespace is responsible for network access and mapping communication ports. 
* ipc (System V IPC): Inter-process communication controls how the application can access shared memory locations between applications within containers. 
* uts (hostname): This namespace controls host and domain names, allowing unique values per process.
* user (UIDs): This namespace is used to map unique user rights to processes. 
(Kindle Locations 9662-9669). 

**Cgroups**   
Cgroups, or control groups, are used to manage the resource consumption of each container process. You can set how much CPU and RAM are allocated as well as network and storage I/O. 
(Kindle Locations 9673-9675). 



**Union File System**   
The Union File System is a foundational building block for a container. It is a file system service that was developed for Linux to allow different file systems to be layered on top of each other to create a combination, or union, of the various files to create a single merged representation of the contents. 
Kindle Locations 9680-9682). 


**Working with Containers**   
When working with containers, the key commands are as follows:   
* create: Create a container from an image.  
* start: Start an existing container.  
* run: Create a new container and start it.   
* ls: List running containers.  
* inspect: Get detailed information regarding the container.   
* logs: Print run logs from the container’s execution.  
* stop: Gracefully stop running the container.  
* kill: Stop the main process in the container abruptly.   
* rm: Delete a stopped container. 
(Kindle Locations 9771-9775). 



To disconnect from the container, you can type exit, but that would stop the container. If you want to leave it running, you can:  
* hold down Ctrl and press P and then while still holding Ctrl press Q. 

This sequence drops you back to the host OS and leaves the container running. From the host OS, you can type `docker container ls` to see that your container is actively running: 
(Kindle Locations 9828-9830). 

**Map a local directory to the container**    
`docker container run --name test-nginx -p 80:80 -d -v ~/Documents/html:/usr/share/nginx/html nginx`

**Pruning all stopped containers**  
First list all containers  
 `docker container ls -a`                                                                               
```
CONTAINER ID   IMAGE                    COMMAND                  CREATED          STATUS                        PORTS                    NAMES
18f6517cdcd4   nginx                    "/docker-entrypoint.…"   11 minutes ago   Exited (0) 2 minutes ago                               test-nginx
987ddaac5870   ubuntu                   "bash"                   50 minutes ago   Exited (127) 35 minutes ago                            unruffled_lamport
8e99e34b2e4c   hello-world              "/hello"                 52 minutes ago   Exited (0) 52 minutes ago                              affectionate_morse
df226013c848   docker/getting-started   "/docker-entrypoint.…"   3 months ago     Exited (255) 3 months ago     0.0.0.0:80->80/tcp       condescending_agnesi
2bac829fd651   getting-started          "docker-entrypoint.s…"   3 months ago     Exited (255) 3 months ago     0.0.0.0:3000->3000/tcp   tender_carson
```
**Prune all stopped containers**    
```
docker container prune                                                                                WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y

docker container ls -a                                                                                
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
┌─[mhubbard@HP8600-4] - [~/GoogleDrive/01_Vector/25_City-of-Riverside/networkRefresh] - [3580]
```

### Docker Files

* FROM: Selects the base image used to start the build process or can be set to scratch to build a totally new image. 
* MAINTAINER: Lets you select a name and email address for the image creator. 
* RUN: Creates image layers and executes commands within a container. 
* CMD: Executes a single command within a container. Only one can exist in a Dockerfile. 
* WORKDIR: Sets the path where the command defined with CMD is to be executed. 
* ENTRYPOINT: Executes a default application every time a container is created with the image. 
* ADD: Copies the files from the local host or remotely via a URL into the container’s file system. 
* ENV: Sets environment variables within the container. 
* EXPOSE: Associates a specific port for networking binding. 
* USER: Sets the UID (or username) of the user that is to run the container. 
* VOLUME: Sets up a sharable directory that can be mapped to a local host directory.
* LABEL: Provides a label to identify the created Docker image. 
(Kindle Locations 9918-9926). 


**Create an Ubuntu container running nginx**  
```
FROM ubuntu:latest
MAINTAINER Cisco Champion (user@domain.com)
RUN apt-get update && apt-get upgrade -y
RUN apt-get install nginx -y
EXPOSE 80 443
VOLUME [ "/usr/share/nginx/html" ]
CMD [ "nginx", "-g", "daemon off;" ]

docker container build -t myimage:latest .

docker container run -p 80:80 -d myimage
```  

* docker image history myimage
* docker build -t myimage:latest .
* docker ps
* docker image ls
* docker container stop myimage
* docker container stop 5864bb27c1a3
* docker container stop friendly_rhodes
* docker container ls
* docker container ls -a
* docker container rm myimage
* docker container rm 0ab643b2276e
* docker image rm myimage
* docker container run -p 80:80 -d myimage
* docker container rm 5864bb27c1a3

**Log into bash on a running container**  
https://stackoverflow.com/questions/30172605/how-do-i-get-into-a-docker-containers-shell

```
docker ps -a                                                                                                                                                            
CONTAINER ID IMAGE 	COMMAND  				CREATED          STATUS 		PORTS                             NAMES
fe08c36f01ea nginx 	"nginx -g 'daemon of…"   44 seconds ago   Up 44 seconds 0.0.0.0:80->80/tcp, :::80->80/tcp test2

docker container exec -it fe08c36f01ea  bash
root@fe08c36f01ea:/# 

root@fe08c36f01ea:/# ls -l /usr/share/nginx/html
total 4
-rw-rw-r-- 1 1000 1000 12 Jul  6 23:14 test.html
root@fe08c36f01ea:/# cat /usr/share/nginx/html/test.html
Hello World
```

