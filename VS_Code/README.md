# VS Code Tips <!-- omit from toc -->  

Table of Contents

- [Introduction](#introduction)
- [Useful websites](#useful-websites)
- [Setting up the VSCode environment](#setting-up-the-vscode-environment)
- [Comparing a saved file to the one in the editor](#comparing-a-saved-file-to-the-one-in-the-editor)
- [VS Code Extensions](#vs-code-extensions)

## Introduction  

I had been using Sublime Text for a long time and was reluctant to switch to VS Code but I finally decided to try it and I am fully onboard now! I still use Sublime Text for text files but even there, VS Code is winning out slowly but surely.  

What did it for me was the VS Code Tutorial that I have listed in the "Useful Websites" section below. VS Code has become my favorite tool.

## Useful websites  

- [VS Code installation](https://mwhubbard.blogspot.com/2021/03/apple-macbook-air-m1-for-network_15.html#VSCode)  
This is from my blog. It covers install VSCode, picking a Theme, setting up the Pylance linter, etc. The blog is for macOS but everything after the basic install applies to Mac/Linux/Windows.  
- [VS Code Tutorial – Become More Productive](https://www.youtube.com/watch?v=heXQnM99oAI) - This tutorial is awesome. It's almost 6 hours long so you will have to do it in sections but it is worth doing.
- [Using Python environments in VS Code](https://code.visualstudio.com/docs/python/python-tutorial#_create-a-virtual-environment) -
I use Microsoft's Visual Studio Code as the Integrated Development Environment (IDE) for Python and PowerShell.  I had been creating virtual python environments in the terminal but the DevNet guide recommended doing it in VSCode. This article walks you through how to do it.  

- [See unsaved changes in vscode](https://stackoverflow.com/questions/65874120/see-unsaved-changes-in-vscode)  
Some good tips on editing unsaved files and using shortcuts in VSCode.  

- [Extensions for the Visual Studio family of products](https://marketplace.visualstudio.com/vscode)  
Microsoft's marketplace for VSCode extensions. There are a lot of useful extensions for VScode here. Most are free.  

- [User Interface](https://code.visualstudio.com/docs/getstarted/userinterface)  
The official documentation on the VSCode User Interface. It's worth some time reviewing this page.  

- [Resolving shell environment fails](https://code.visualstudio.com/docs/supporting/faq#_resolving-shell-environment-fails)  
I have had this happen a couple times with VScode on Mac and Linux.  

## Setting up the VSCode environment  

VS Code has a rich set of editing tools. One feature I found really useful for the DevNet course is that you can open a folder and see all of the files in the VSCode explorer.  

For this course, I created a new folder called _DevNet and then opened the folder in VSCode. For later chapters, I created folders called Meraki and DNA using `python -m venv meraki` and `python -m venv DNA`.  

Then I could create the python scripts and any other documents in the repsective folders.

## Comparing a saved file to the one in the editor  

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

## VS Code Extensions  
Microsoft maintains its own marketplace for [extensions](https://marketplace.visualstudio.com/VSCode). There are tens of thousands of extensions so obviously I can't review them here.  

The extensions that I use:

- [autoDocstring: VSCode Python Docstring Generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring&ssr=false#review-details) - When you are in a function and type """ or ''' (use the extension settings to configure which) it will autopopulate the recommended fields.  Also in settings you can select the type of fields. There is a Python PEP257 but I use the Google option. This [article](https://stackabuse.com/common-docstring-formats-in-python/) discusses common docstring formats for Python.  

- [Better Jinja](https://marketplace.visualstudio.com/items?itemName=samuelcolvin.jinjahtml&ssr=false#review-details) - You will find yourself using Jinja2 a lot with Ansible and just templating in general. This extension provides "Syntax highlighting for jinja(2) including HTML, Markdown, YAML and other templates."
- [Blockman - Highlight Nested Code Blocks](https://marketplace.visualstudio.com/items?itemName=leodevbro.blockman) - VS Code Extension For Nested Block Highlighting. I like it so much that I donated to the author.
- [Cisco Config Highlight](https://marketplace.visualstudio.com/items?itemName=Y-Ysss.cisco-config-highlight) - isco device configuration Syntax Highlighting for Visual Studio Code. The only drawback to this extension is that you have to use the file extension .cisco.
- [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens&ssr=false#overview) - ErrorLens turbocharges language diagnostic features by making diagnostics stand out more prominently, highlighting the entire line wherever a diagnostic is generated by the language and also prints the message inline. I really like this extension but it can make the screen a little crowed.
- [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph) - View a Git Graph of your repository, and easily perform Git actions from the graph. Configurable to look the way you want!
- [indent-rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow) - This extension colorizes the indentation in front of your text, alternating four different colors on each step. Some may find it helpful in writing code for Python, Nim, Yaml, and probably even filetypes that are not indentation dependent. I modified the setting to make the lines wider and darker.
- [Jinja Snippets](https://marketplace.visualstudio.com/items?itemName=noxiz.jinja-snippets) - A large collection of snippets for Jinja2. For information on Jinja2 read this [turorial](https://jinja.palletsprojects.com/en/3.0.x/templates/).
- [Juniper Junos Extension](https://marketplace.visualstudio.com/items?itemName=codeout.vscode-junos) - A syntax highlighter for Junos. You must use .conf for the extension to work.
- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) - All you need for Markdown (keyboard shortcuts, table of contents, auto preview and more). Markdown is a very popular language for creating documentation. It is used by GitHub and you will have to be skilled at markdown to efficiently make README.md files on GitHub.  

    One feature that Markdown all in one doesn't have is a table generator. I use [Tables Generator](https://www.tablesgenerator.com/markdown_tables#) to create tables.  
- [Markdown Preview Github Styling](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-preview-github-styles) - Changes VS Code's built-in markdown preview to match GitHub's styling. Of Course, Github uses its own markdown flavor.
- [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) - markdownlint is an extension for the Visual Studio Code editor that includes a library of rules to encourage standards and consistency for Markdown files.
- [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme) - This extension adds icons for files and folder. At first I laughed and said "Why?". But I have to admit they look nice.
- [One Dark Pro](https://marketplace.visualstudio.com/items?itemName=zhuangtongfa.Material-theme) - Atom's iconic One Dark theme, and one of the most installed themes for VS Code! There are so many themes for VS Code that it's hard to pick one. I have used Monokai, Github, etc. Currently One Dark Pro is my preferred.
- [Peacock](https://marketplace.visualstudio.com/items?itemName=johnpapa.vscode-peacock) - This is another one that I laughed at until I started using workspaces. Now I couldn't live wihthout it.
- [PowerShell](https://marketplace.visualstudio.com/items?itemName=ms-vscode.PowerShell) - Network Engineers don't live in a vacuum! PowerShell is cross-platform and quite an elegant lanugage. I do a lot of DHCP mods for customers and find that PowerShell saves time and mistakes. Here is my github repo for DHCP scripts: [PowerShell-DHCP](https://github.com/rikosintie/PowerShell-DHCP/)
- [Python Indent](https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent) - Every time you press the Enter key in a Python context, this extension will parse your Python file up to the location of your cursor, and determine exactly how much the next line (or two in the case of hanging indents) should be indented and how much nearby lines should be un-indented.
- [Rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv) - I love this extension! So much better than Excel.
  - Highlight columns in comma (.csv), tab (.tsv), semicolon and pipe - separated files in different colors
  - Transform and filter tables using built-in SQL-like query language.
  - Fixed sticky header line (optional).
  - Provide info about column on hover.
  - Automatic consistency check for csv files (CSVLint).
  - Align columns with spaces and Shrink (trim spaces from fields).
  - Multi-cursor column edit.
  - Works in browser (vscode.dev).
- [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) - I built a Raspberry Pi Zero W serial console. I used Python for a lot of the functionality. With this extension I was able to use VS Code even though the files were on the Pi. The Remote - SSH extension lets you use any remote machine with a SSH server as your development environment. This can greatly simplify development and troubleshooting in a wide variety of situations.
  - You can:
  - Develop on the same operating system you deploy to or use larger, faster, or more specialized hardware than your local machine.
  - Quickly swap between different, remote development environments and safely make updates without worrying about impacting your local machine.
  - Access an existing development environment from multiple machines or locations.
  - Debug an application running somewhere else such as a customer site or in the cloud.
- [Remote - SSH: Editing Configuration Files](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh-edit) - The Remote - SSH extension lets you use any remote machine with a SSH server as your development environment. This extension complements the Remote - SSH extension with syntax colorization, keyword intellisense, and simple snippets when editing SSH configuration files.
- [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) - Ruff can be used to replace Flake8 (plus dozens of plugins), Black, isort, pyupgrade, and more, all while executing tens or hundreds of times faster than any individual tool.
- [TextFSM Template Syntax](https://marketplace.visualstudio.com/items?itemName=andytruett.TextFSM-Syntax) - Visual Studio Code syntax highlighting for textFSM templates

    Syntax Coloring for:

  - Comments
  - Value Definitions (w/ options, regex)
  - Reserved States
  - States
  - State Rules
  - Rule Actions
  - New State Transitions
  - Error Actions
  - EOF marker
- [XML Tools](https://marketplace.visualstudio.com/items?itemName=qub.qub-xml-vscode) - This extension provides XML language support for VS Code, beyond simple text coloring.

    Features

  - Format XML documents (Alt+Shift+F)
  - Error messages for not well-formed XML documents
  - Hover text for declaration name and attribute names
  - Auto-completion for declaration name and attribute names and values
  - Hover text for DOCTYPE name
  - Auto-completion for end tag name
  - Automatically close elements on start tag's closing right angle bracket ('>')
  - Automatically close CDATA on second left square bracket ('[')
  - Automatically close comments on second dash ('-')
- [YAML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) - YAML Language Support by Red Hat. Provides comprehensive YAML Language support to Visual Studio Code, via the yaml-language-server, with built-in Kubernetes syntax support.
