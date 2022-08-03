# Chapter 13 Deploying Applications

### Table of Contents
[NIST](#NIST)  
[Service Models](#ServiceModels)  
[Cloud deployment models](#Cloud-deployment-models)  
[Edge or Fog Computing](#Edge-or-Fog-Computing)  
[Application Deployment Methods](#Application-Deployment-Methods)  
[DevOps](#DevOps)  
[Docker](#Docker)



<a name="NIST"/>  

## NIST (SP) 800-145 What is the cloud

* Broad Network Access - Services are available over the network and accessed via standard protocols on any type of client (Mobile phone, tablet, desktop, etc.)
* Rapid elasticity: Capacity can be automatically provisioned and decommissioned to scale the service to demand. 
* Measured service: Cloud systems measure resource utilization (compute, storage, and network) and charge for those services accordingly. Utilization is monitored, controlled, and reported on, allowing transparency for the service provider and customer. 
* On-demand self-service: The cloud consumer can provision compute, storage, and network as needed, without human interaction, through automation or self-service portals. 
* Resource pooling: The infrastructure is a common pool of resources that can serve multiple customers at the same time. The customer does not interact with the underlying hardware, and workloads can be moved within the cloud environment based on demand without the end user knowing or needing to be involved. 
Kindle Locations 9294-9300). 

<p align="center" width="100%">
    <img width="50%" src="https://github.com/rikosintie/DevNetAssoc/blob/main/chapter13/images/ch13-Cloud-definition.png"> 
</p> 

<a name="ServiceModels"/>  

## Service Models
* Software as a service (SaaS): A service provider hosts, manages, and controls an application and offers it to the customer to use. The customer does not interact at all with the underlying infrastructure, operating systems, storage, or network. There may be some customization capabilities, but they are usually limited to application-specific configuration. What you see is what you get. 
* Platform as a service (PaaS): A PaaS provider supplies a fully integrated service/software suite, and customers can deploy their applications on top of this suite with a predefined set of application programing interfaces, libraries, software development kits, and/or other tools and services. Customers can program the application in any way they choose and can customize it directly to their own workflow, as long as the customization is within the parameters of the service provider’s offering. Customers do not have to worry about integration of the underlying infrastructure components, and in the case of a managed PaaS service, have no management responsibilities for the underlying infrastructure. 
* Infrastructure as a service (IaaS): A provider enables the customer to provision compute, storage, and networking to run any combination of software and operating systems. While customers have no control of the underlying infrastructure hardware platform, they have full control over the software and services they deploy within the cloud service. The customer is also responsible for the maintenance of the software they deploy, including patching and upgrading. 

<p align="center" width="100%">
    <img width="50%" src="https://github.com/rikosintie/DevNetAssoc/blob/main/chapter13/images/ch13-Cloud-Serice-Models.png"> 
</p> 

<a name="#Cloud-deployment-models"/>

### Cloud deployment models

* Private Cloud
* Public Clouod
* Hybrid Cloud
* Community Cloud

<a name="#Edge-or-Fog-Computing"/>

## Edge or Fog Computing
With the increase in IoT applications, devices, and sensors, the various deployment models covered so far are just not up to the task of handling the sheer volume of data being created and needing to be processed. 

This sea of data cannot be consumed and processed by a centralized cloud application, given the cost of transporting the data and the latency involved in receiving information back to do anything with it. Your self-driving car would run into a ditch before a cloud service could detect and respond. 
(Kindle Location 9362). 

<p align="center" width="100%">
    <img width="50%" src="https://github.com/rikosintie/DevNetAssoc/blob/main/chapter13/images/ch13-Edge-Computing.png"> 
</p> 

<a name="#Application-Deployment-Methods"/>  

## Application Deployment Methods 
What is IT’s value to the business if you boil it down to the simplest aspect? IT is charged with supporting and maintaining applications that the business relies on. No one builds a network first and then looks for applications to stick on it. 
(Kindle Locations 9373-9375). 

### Bare-Metal Application Deployment </br>
The traditional application stack, or bare-metal, deployment is fairly well known. 

### Virtualized Applications  
Virtualization was created to address the problems of traditional bare-metal server deployments where the server capacity was poorly utilized. The idea with virtualization is to build one large server and run more than one application on it. Sounds simple, right?  


### Cloud-Native Applications 
Cloud-native, or microservice, applications represent the further intersection and evolution of virtualization and a cloud environment. As virtualization became popular, application developers started to ask themselves why they needed a heavy operating system to run their applications. All the patching, drivers, and configuration requirements don’t go away just because you load a virtual machine. 

<p align="center" width="100%">
    <img width="50%" src="https://github.com/rikosintie/DevNetAssoc/blob/main/chapter13/images/ch13-Cloud-Native.png"> 
</p> 


### Containers
The benefits of containers are as follows: 
* Consistency for deployment automation 
* Simplified lightweight image files measured in megabytes (whereas VM files are measured in gigabytes) 
* Providing only what the app needs and nothing else 
* Ability to work the same in production as on a developer’s laptop 
* Open community-built best-of-breed containers for faster innovation 
* Ability to deploy applications in seconds 
(Kindle Locations 9426-9430). 

<a name="#DevOps"/>  

## DevOps
* Culture: For DevOps to work, organizational culture must change. This is by far one of the most difficult aspects to embrace, but it is the single most important factor for success. DevOps requires a culture of sharing. 
* Automation: While DevOps is more than just a set of software tools, automation is the most easily identifiable benefit. Automation techniques greatly speed up the deployment process, enable defects to be caught and corrected earlier, and eliminate the need for human intervention in repetitive tasks. * Lean: Reducing wasted efforts and streamlining the process are the goals of Lean. It’s a management philosophy of continuous improvement and learning. 
* Measurement: Unless you measure your results, you can never improve. Success with DevOps requires the measurement of performance, process, and people metrics as often as is feasible. 
* Sharing: DevOps requires a culture of feedback and sharing. Breaking down silos and creating an inclusive shared fate environment is the ultimate goal. 
(Kindle Locations 9515-9522). 

The whole point is to reduce wasted time on rework. 
Kindle Location 9556). 

**The First way**    
The following are the key characteristics of the first way: 
* Make work visible 
* Reduce batch sizes 
* Reduce intervals of work 
* Build in quality by preventing defects from being passed downstream 
* Constantly optimize for business goals 
(Kindle Locations 9558-9561). 

**Second Way: Feedback Loop**    
One of the things you will see repeatedly in DevOps is analogies to manufacturing. Since so much of this management philosophy is derived from Lean and the Toyota Production System, concepts like defect prevention are front and center in the approach. 
(Kindle Locations 9562-9564). 

If something isn’t working, you have to make sure that it doesn’t happen again so you don’t end up on a hamster wheel of pain. 
(Kindle Locations 9565-9566). 

**Third Way: Continuous Experimentation and Larning**  
How do you foster innovation? Create a culture of trust where your people are allowed to try new things and fail. That doesn’t mean that you are just rolling the dice on crackpot ideas; rather, it means having a dynamic and disciplined approach to experimentation and risk taking. It’s very rare that success happens on the first try.  
(Kindle Locations 9580-9582). 

The following are the key characteristics of the third way: 
* Conduct dynamic, disciplined experimentation and risk taking  
* Define time to fix issues and make the system better  
* When things go wrong, don’t point fingers  
* Create shared code repositories  
(Kindle Locations 9591-9593). 


### DevOps Implementation 
Implementing DevOps technical practices within an organization typically involves three stages. These stages follow a natural progression that leads to a fully automated code-to-deployment operational model:  

* Continuous integration: This stage involves merging development work with the code base constantly so that automated testing can catch problems early. 
* Continuous delivery: This stage involves a software package delivery mechanism for releasing code to staging for review and inspection. 
* Continuous deployment: This stage relies on continuous integration and continuous delivery to automatically release code into production as soon as it is ready.  
(Kindle Locations 9594-9601). 

https://xebialabs.com/periodic-table-of-devops-tools/  
(Kindle Location 9606). 

_For technologists, it’s easy to focus on the tools and technology, but honestly that’s the easy part of DevOps. Changing culture and implementing Lean methodologies are where many companies have struggled. Focus on streamlining your processes and implement technologies that help accelerate your efforts._   
(Kindle Locations 9644-9646). 

### DevOps Pipeline


<p align="center" width="100%">
    <img width="80%" src="https://github.com/rikosintie/DevNetAssoc/blob/main/chapter13/images/ch13-DevOps-Pipeline.png"> 
</p> 

Here is how the pipeline works:  
* Step 1. The developer pulls the latest code from the version control system with Git. This ensures that the developer has the most recent changes and is not working with an old version.  
* Step 2. The developer makes changes to the code, adding new features or fixing bugs. The developer also writes test cases that will be used to automatically test the new code to software functional requirements. The developer eventually stages the changes in Git for submission.  
* Step 3. The developer uses Git to push the code and tests to the version control system (for example, GitHub), synchronizing the local version with the remote code repository stored in the version control system.  
* Step 4. The continuous integration server, such as Jenkins, has a login that monitors GitHub for new code submissions. When Jenkins sees a new commit, it is able to pull the latest version and starts an automated build process using the test cases.  
* Step 5. Jenkins kicks off the automated build of a testing environment for the new software build. It is possible to use Python scripts, Ansible, or other infrastructure automation tools to build the testing environment as close to production as possible. 
* Step 6. Jenkins executes various automated testing, including unit testing, integration testing, smoke testing (stress testing), and security testing. When all the tests are finished, the results are sent back to Jenkins for compilation.  
* Step 7. Jenkins sends the test results to the developer for review. They can be sent via email, but a more modern way of alerting the developer is through a collaboration tool such as Webex Teams. Jenkins has plug-ins for all major team management tools and allows for easy integration. If the build fails, the developer can use links to the information on what failed and why, make changes to the code, and restart the process.  
* Step 8. If the build process is successful and all of the tests pass, Jenkins can deploy the new code to an artifact repository (just a fancy name for the place finished software is stored). The software is not able to be deployed in production.  
* Step 9. Jenkins signals the infrastructure that an updated version of software is ready. For example, there may be a new container ready to be deployed into a Kubernetes platform. The updated container replaces the existing containers with the new code fully tested and ready to go. Now the application is updated with minimal (or no) disruption. 

***The nuts and bolts of building a DevOps pipeline are beyond of the scope of the 200-901 DevNet Associate DEVASC exam.***
(Kindle Locations 9630-9643).  

<a name="#Docker"/>

## Docker 
[15 Docker commands you should know](https://towardsdatascience.com/15-docker-commands-you-should-know-970ea5203421)  
[zsh-docker-aliases](https://github.com/akarzim/zsh-docker-aliases)  
If you use zsh as your shell, these aliases will save you a lot of time.
 
To work with Docker commands, you first need to know whether you’re dealing with an image or a container.
* A Docker image either exists or it doesn’t.
* A Docker container either exists or it doesn’t.
* A Docker container that exists is either running or it isn’t.

Once you know what you’re working with you can find the right command for the job.

Namespaces  
Namespaces are essential for providing isolation for containers. Six namespaces are used for this purpose:  
* mnt (mountpoints): This namespace is used for mapping access to host operating system storage resources to the container process. 
* pid (processes): This namespace is used to create a new process ID for an application. 
* net (networks): This namespace is responsible for network access and mapping communication ports. 
* ipc (System V IPC): Inter-process communication controls how the application can access shared memory locations between applications within containers. 
* uts (hostname): This namespace controls host and domain names, allowing unique values per process.
* user (UIDs): This namespace is used to map unique user rights to processes. 
(Kindle Locations 9662-9669). 

<p align="center" width="100%">
    <img width="50%" src="https://github.com/rikosintie/DevNetAssoc/blob/main/chapter13/images/ch13-NamseSpace.png"> 
</p> 

**Cgroups**  
Cgroups, or control groups, are used to manage the resource consumption of each container process. You can set how much CPU and RAM are allocated as well as network and storage I/O. 
(Kindle Locations 9673-9675).  

<p align="center" width="100%">
    <img width="50%" src="https://github.com/rikosintie/DevNetAssoc/blob/main/chapter13/images/ch13-CGroups.png"> 
</p> 

**Union File System**  
The Union File System is a foundational building block for a container. It is a file system service that was developed for Linux to allow different file systems to be layered on top of each other to create a combination, or union, of the various files to create a single merged representation of the contents. 
Kindle Locations 9680-9682).  

### Docker Architecture
The Docker architecture consists of three primary parts: the client, the Docker host, and the docker registry.

The Docker client is a command-line utility (run with the docker command) that talks to the REST API of the Docker daemon so that the administrator can issue commands for the operations and management of Docker containers. The client can communicate to a local or remote Docker instance. 
(Kindle Locations 9704-9705).  
</br>

<p align="center" width="100%">
    <img width="50%" src="https://github.com/rikosintie/DevNetAssoc/blob/main/chapter13/images/ch13-DockerArchitecture.png"> 
</p> 
</br>


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
┌─[mhubbard@HP8600-4] -
```

### Docker Files  
[Docker for Beginners](https://docker-curriculum.com) - This is a great tutorial on Docker.
[How to build Docker Files](https://www.youtube.com/watch?v=WmcdMiyqfZs)  
[ADD vs COPY](https://www.geeksforgeeks.org/difference-between-the-copy-and-add-commands-in-a-dockerfile/)  
[what is the difference between the COPY and ADD command](https://stackoverflow.com/questions/24958140/what-is-the-difference-between-the-copy-and-add-commands-in-a-dockerfile)  
[Dockerfiles](https://towardsdatascience.com/learn-enough-docker-to-be-useful-b0b44222eef5)  
[Docker Basics: How to Use Dockerfiles](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/)  


When to use ADD or COPY: According to the Dockerfile best practices guide, we should always prefer COPY over ADD unless we specifically need one of the two additional features of ADD.

Dockerfile = Comments + Commands + Arguments  
Dockerfile is used with `docker build` to create a docker image.  

Example  
RUN mkdir -p /home/app  
COPY ./app /home/app  (copy files from <Dokerfile directory>/app on the host to the container)
CMD ["node", "server.js"]  
ADD /[source]/[destination] EX ADD /root_folder/testfolder

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
```

Working with Images  
* build: Builds an image from a Dockerfile. 
* push: Pushes a local image to a remote registry for storage and sharing. 
* ls: List images stored locally. 
* history: Shows the creation and build process for an image. 
* inspect: Provides detailed information on all aspects of an image, including layer detail. 
* rm: Deletes an image from local storage. 
(Kindle Locations 9951-9955). 

Build the image
`docker image build -t myimage:latest .`

-t - tag the image myimage:latest  
. - Docker file is located in the same directory

**Login into Docker Hub and push the image**  
`docker login` — Log in to a Docker registry. Enter your username and password when prompted.  

`docker image push my_repo/my_image:my_tag`  

Run the container  
`docker container run -p 80:80 -d myimage`  
 

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

### Docker Hub
Docker Hub has a slick web interface that makes it easy to set up a repository and secure it. It also integrates with GitHub and Bitbucket to enable automated container creation from source code stored in your version control system. It’s a great way to start building a CI/CD pipeline as it is free to get started. 
Kindle Locations 10033-10035).  

Create a free account at [hub.docker.com](hub.docker.com).  
* My username is rikosintie.  
* Create a new repo. I called mine devnet  
* On the hub I see rikosintie/devnet

**Tag the image and then upload it to the hub**
`docker image tag 09f9874161b3 rikosintie/devnet:myimage`

**Push the image to the hub**  
`docker push rikosintie/devnet:myimage`  
  
</br>
<p align="center" width="100%">
    <img width="80%" src="https://github.com/rikosintie/DevNetAssoc/blob/main/chapter13/images/ch13-DockerHub.png"> 
</p>  
</br>


**To use the image**  
`docker image pull  rikosintie/devnet:myimage`  
