## Chapter 3 Introduction to Python

Chapter 3 is a great introduction to python. You will need to use additional resources to master this chapter but it gets you started.

**Useful websites**   
[Learning Python 3](https://mwhubbard.blogspot.com/2018/07/learning-python-3.html)  
This is my blog on Python resources. I update it on regular basis so bookmark it and check back weekly.  

[A curated list of Ultimate Python resources!](https://twitter.com/ayushi7rawat/status/1315651868891049984)  
This is a twiter thread. It contains a curated list of 
* books
* IDEs
* playgrounds
* podcasts hosting platforms for python projects
* youtube channels
* websites
* courses
* Technical Blogging Platforms where you can read python blogs

[Using Python environments in VS Code ](https://code.visualstudio.com/docs/python/environments)  
I use Microsoft's Visual Studio Code as the Integrated Development Environment (IDE) for Python and PowerShell. I had been creating virtual python environments int the terminal but the DevNet guide recommended doing it in VSCode.   

This article walks you through how to do it. The only thing I will add is that on the section ## Create a virtual environment it says:  
```
# macOS/Linux
# You may need to run sudo apt-get install python3-venv first
python3 -m venv .venv
``` 

DO THIS IN THE TERMINAL IN VSCode, not in your regular terminal.

## Setting up the VSCode environment

VS Code has a rich set of editing tools. One feature I found really useful for the DevNet course is that you can open a folder and see all of the files in the VSCode explorer. 

For this course, I created a new folder called _DevNet and then opened the folder in VSCode. For later chapters, I created folders called Meraki and DNA using `python -m venv meraki` and `python -m venv DNA`. 

Then I could create the python scripts and any other documents in the repsective folders.


## Comparing a saved file to the one in the editor

On the VSCode "view" menu you can turn on the Explorer (shortcut ↑⌘e) or you can left click on the icon that looks like two documents on the top left of VSCode.   
<p align="center" width="100%">
    <img width="40%" src="https://github.com/rikosintie/DevNetAssoc/blob/main/chapter3/images/VS-View-Menu.png"> 
</p>  

That will open a pane on the left. On the file menu, select "Open Folder" and select a folder on your file system. Here is what my _DevNet folder looks like:  
<p align="center" width="100%">
    <img width="40%" src="https://github.com/rikosintie/DevNetAssoc/blob/main/chapter3/images/VS-DevNet-Folder.png"> 
</p> 

Notice at the very top is the "Open Editors" pane. If yours is not on, you can right click over a folder and select "Open Editors".

Notice in the "Open Editors" pane that the file test.py has a white dot next to it. That means there are unsaved changes.  

<p align="center" width="100%">
    <img width="40%" src="https://github.com/rikosintie/DevNetAssoc/blob/main/chapter3/images/Unsaved-changes.png"> 
</p>  

To view the differences between the file on disk and the file in VScode, right click over test.py and select "Compare with Saved [⌘K D]".  

<p align="center" width="100%">
    <img width="40%" src="https://github.com/rikosintie/DevNetAssoc/blob/main/chapter3/images/VS-Compare.png"> 
</p>  
