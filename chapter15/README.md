# Chapter 15 Infrastructure Automation  

This chapter covers the following topics:  
* **Controller Versus Device-Level Management:** This section compares and contrasts the two network device management options currently available: controller-based and device-level management.  
* **Infrastructure as Code:** This section introduces the concepts of infrastructure as code.  
* **Continuous Integration/Continuous Delivery Pipelines:** This section examines CI/CD pipelines, why they are used, the problems they address, and how they can be applied to infrastructure automation.  
* **Automation Tools:** This section covers popular automation tools that are used for configuration management and network automation.  
* **Cisco Network Services Orchestrator (NSO):** This section provides an introduction to Cisco NSO.  
* **Cisco Modeling Labs/Cisco Virtual Internet Routing Laboratory (CML/VIRL):** Cisco Modeling Labs (CML) is the new name for VIRL and we will use it interchangeably (CML/VIRL). This section explains what Cisco CML/VIRL is and how it can be used to build network simulations.  
* **Python Automated Test System (pyATS):** This section examines pyATS, including the components that make up the testing solution and how it can be used to automate network testing.  

There are usually two types of approaches to infrastructure as code:  
 
* **Declarative:** With the declarative approach, the desired state of the system is defined and then the system executes all the steps that need to happen in order to attain the desired state. 
* **Imperative:** The imperative approach defines a set of commands that have to be executed in a certain order for the system to achieve the desired state.  

A popular infrastructure as code solution is Terraform from HashiCorp. Infrastructure as code integrates very well in the continuous integration/continuous delivery pipelines discussed next. 
(Kindle Locations 10828-10832).  


## Continuous Integration/Continuous Delivery Pipelines  

CI/CD is a series of automated steps that code goes through from the IDE of the individual developer, through building, testing, and finally deployment to staging and production environments. Although usually used together, continuous integration and continuous delivery are two separate concepts that can be addressed separately.  

A key component of any CI pipeline is the **build server**. The role of the build server is to react to developers committing their code to the central repository and to start the initial tests on the new code features. Most version control systems support webhook mechanisms to automatically notify the build server when pull requests are opened and code is committed. Popular build servers include **Jenkins**, **Travis CI**, and **Drone CI**.  

<p align="left" width="100%">
    <img width="50%" src="https://github.com/rikosintie/DevNetAssoc/blob/main/chapter15/images/ch15-Dev-Environments.png"> 
</p>  

