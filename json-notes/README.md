# My JSON notes<!-- omit from toc -->  

- [Introduction](#introduction)
- [Links to json tutorials](#links-to-json-tutorials)
- [Youtube Tutorials](#youtube-tutorials)
- [JSON to Python Conversion](#json-to-python-conversion)
- [Pandas](#pandas)

## Introduction

 JSON is the data structure used with API requests and responses. You must have
 a good understanding of json and python to successfully work as NetDevOps
 engineer.  

## Links to json tutorials  

- [JavaScript JSON](https://www.geeksforgeeks.org/javascript-json/) - What is JSON?
- [Learn {JSON} in 10 minutes](https://www.youtube.com/watch?v=iiADhChRriM) - A youtube video tutorial
- [How can I convert JSON to CSV](https://stackoverflow.com/questions/1871524/how-can-i-convert-json-to-csv)
- [ntc-templates](https://github.com/networktocode/ntc-templates/tree/master/ntc_templates/templates) - Convert "show run" commands to json
- [How can I access the nested data in this complex JSON, which includes another JSON document as one of the strings?](https://stackoverflow.com/questions/48193502/how-can-i-access-the-nested-data-in-this-complex-json-which-includes-another-js)
- [Using Pyton to loop through JSON-ENCODED DATA](https://www.tech-otaku.com/mac/using-python-to-loop-through-json-encoded-data/)
- [{JSON} Placeholder](https://jsonplaceholder.typicode.com) - A free fake API for testing and prototyping JSON objects.
- [JSONPlacehoder Guide](https://jsonplaceholder.typicode.com/guide/) - How to use the JSONPlaceholder server
- [JSON/YAML/XML Converter Site](https://textfsm.nornir.tech) - This site is awesome. You can take the output of a show command, for example "show interface status", and convert it to JSON, then paste the JSON into the next tab and get YAML and XML output!

**Nornir JSON/textFSM Converter**

<p align="center" width="100%">
    <img width="80%" src="https://github.com/rikosintie/DevNetAssoc/blob/main/json-notes/images/textfsm-nornir-tech-textfsm.png">  
</p>  

**Nornir JSON/YAML/XML Converter**
<p align="center" width="100%">
    <img width="80%" src="https://github.com/rikosintie/DevNetAssoc/blob/main/json-notes/images/textfsm-nornir-tech.png">  
</p>  

## Youtube Tutorials  

- [Learn JSON in 10 Minutes](https://www.youtube.com/watch?v=iiADhChRriM) - This is a good introduction to JSON (10 minutes)
- [Python Tutorial: Working with JSON Data using the json Module](https://www.youtube.com/watch?v=9N6a-VLBa2I&t=308s) - A deeper dive into JSON (20 minutes)

## JSON to Python Conversion  

When you use json.load() or json.loads() to read JSON data it converts the JSON data to python using the following types:

| JSON           | Python   |
|----------------|----------|
| object         | dict     |
| array          | list     |
| string         | str      |
| number (int)   | int      |
| number (real)  | float    |
| true           | True     |
| false          | False    |
| null           | None     |

## Pandas  

Pandas is a library for working with data structures. It allows you to read and write Excel files in Python.  
- [Pandas API Reference](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html)
- [Pandas User Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html)
- [Pandas.read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html)
