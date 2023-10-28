# VS Code Tips #

## Useful websites ##  

* [VS Code installation](https://mwhubbard.blogspot.com/2021/03/apple-macbook-air-m1-for-network_15.html#VSCode)  
This is from my blog. It covers install VSCode, picking a Theme, setting up the Pylance linter, etc. The blog is for macOS but everything after the basic install applies to Mac/Linux/Windows.  
* [VS Code Tutorial – Become More Productive](https://www.youtube.com/watch?v=heXQnM99oAI) - This tutorial is awesome. It's almost 6 hours long so you will have to do it in sections but it is worth doing.
* [Using Python environments in VS Code](https://code.visualstudio.com/docs/python/python-tutorial#_create-a-virtual-environment) -
I use Microsoft's Visual Studio Code as the Integrated Development Environment (IDE) for Python and PowerShell.  I had been creating virtual python environments in the terminal but the DevNet guide recommended doing it in VSCode. This article walks you through how to do it.  

* [See unsaved changes in vscode](https://stackoverflow.com/questions/65874120/see-unsaved-changes-in-vscode)  
Some good tips on editing unsaved files and using shortcuts in VSCode.  

* [Extensions for the Visual Studio family of products](https://marketplace.visualstudio.com/vscode)  
Microsoft's marketplace for VSCode extensions. There are a lot of useful extensions for VScode here. Most are free.  

* [User Interface](https://code.visualstudio.com/docs/getstarted/userinterface)  
The official documentation on the VSCode User Interface. It's worth some time reviewing this page.  

* [Resolving shell environment fails](https://code.visualstudio.com/docs/supporting/faq#_resolving-shell-environment-fails)  
I have had this happen a couple times with VScode on Mac and Linux.  

## Setting up the VSCode environment ##

VS Code has a rich set of editing tools. One feature I found really useful for the DevNet course is that you can open a folder and see all of the files in the VSCode explorer.  

For this course, I created a new folder called _DevNet and then opened the folder in VSCode. For later chapters, I created folders called Meraki and DNA using `python -m venv meraki` and `python -m venv DNA`.  

Then I could create the python scripts and any other documents in the repsective folders.

## Comparing a saved file to the one in the editor ##

On the VSCode "view" menu you can turn on the Explorer (shortcut ↑⌘e) or you can left click on the icon that looks like two documents on the top left of VSCode.  
<p align="center" width="100%">
    <img width="40%" src="https://github.com/rikosintie/DevNetAssoc/blob/main/chapter03/images/VS-View-Menu.png">  
</p>  

That will open a pane on the left. On the file menu, select "Open Folder" and select a folder on your file system. Here is what my _DevNet folder looks like:  
<p align="center" width="100%">
    <img width="40%" src="https://github.com/rikosintie/DevNetAssoc/blob/main/chapter03/images/VS-DevNet-Folder.png"> 
</p>  

Notice at the very top is the "Open Editors" pane. If yours is not on, you can right click over a folder and select "Open Editors".

Notice in the "Open Editors" pane that the file test.py has a white dot next to it. That means there are unsaved changes.  

<p align="center" width="100%">
    <img width="40%" src="https://github.com/rikosintie/DevNetAssoc/blob/main/chapter03/images/Unsaved-changes.png"> 
</p>  

To view the differences between the file on disk and the file in VScode, right click over test.py and select "Compare with Saved [⌘K D]".  

<p align="center" width="100%">
    <img width="40%" src="https://github.com/rikosintie/DevNetAssoc/blob/main/chapter03/images/VS-Compare.png"> 
</p>  

A second editor window will open up and the unsaved file will be on the right.
