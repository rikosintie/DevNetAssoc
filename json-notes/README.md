# My JSON notes<!-- omit from toc -->

- [Introduction](#introduction)
- [Links to json tutorials](#links-to-json-tutorials)
- [Tools](#tools)
- [Youtube Tutorials](#youtube-tutorials)
- [JSON to Python Conversion](#json-to-python-conversion)
- [Online JSON Conversion sites](#online-json-conversion-sites)
- [Pandas](#pandas)

## Introduction

 JSON is the data structure used with API requests and responses. You must have
 a good understanding of json and python to successfully work as NetDevOps
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
- [simplify json parsing with jsonata](https://www.packetcoders.io/simplify-json-parsing-with-jsonata/) - JSONata is a lightweight query and transformation language for JSON; it provides:
  - Parsing: Easily pull the data from your payloads with minimal syntax.
  - Built-in functions: Manipulate your data, for example, sum and join data without moving from JSONata into another language (such as Python).
  - Path Transversal: Navigate nested objects using chained, wildcard, parent, and child selectors.
  - Transformation: Generate new JSON payloads easily.
  - Python Library: Use JSONata within Python using the jsonata library.
  - Online Testing: Validate expressions in the JSONata Exerciser.

## Tools

**Nornir JSON/textFSM Converter**

<p align="center" width="100%">
    <img width="80%" src="https://github.com/rikosintie/DevNetAssoc/blob/main/json-notes/images/textfsm-nornir-tech-textfsm.png">
</p>

**Nornir JSON/YAML/XML Converter**
<p align="center" width="100%">
    <img width="80%" src="https://github.com/rikosintie/DevNetAssoc/blob/main/json-notes/images/textfsm-nornir-tech.png">
</p>

**F(x)**

Fx is a dual-purpose command-line tool tailored for JSON, providing both a terminal-based JSON viewer and a JSON processing utility.

While the JSON viewer is crafted in Go and functions without external dependencies, the JSON processing tool is developed in JS, compatible with Node.js and Deno.

[F(x) Getting Started](<https://fx.wtf/getting-started>)

**jq**

jq is a lightweight and flexible command-line JSON processor.

[jq documentation](https://jqlang.github.io/jq/)


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

## Online JSON Conversion sites

[Convert CSV to JSON](https://www.convertcsv.com/csv-to-json.htm) - **Choose from the following 5 JSON conversions offered by this tool:**
- CSV to JSON - array of JSON structures matching your CSV, nested JSON via column headers, and JSONLines (MongoDB) mode
- CSV to Keyed JSON - Generate JSON with the specified key field as the key value to a structure of the remaining fields, also known as an hash table or associative array. If the key field value is unique, then you have "keyvalue" : { object }, otherwise "keyvalue" : [ {object1}, {object2},... ]
- CSV to JSON Array - An array of CSV values where the CSV values are in an array, or a structure with column names and data as an array
- CSV to JSON Column Array - An array of CSV values where each column of values are in an array
- Generate JSON via Template - Using our template engine, easily customize your JSON output NEW
- Automatic detection of numeric values, logical values, and nulls
- TSV to JSON

[Nornir's conversion tool](https://textfsm.nornir.tech) - A swiss army knife of conversion tools. JSON/XML/XPATH/YAML conversion

## Pandas

Pandas is a library for working with data structures. It allows you to read and write Excel files in Python.

- [Pandas API Reference](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html)
- [Pandas User Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html)
- [Pandas.read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html)

<figure>
      <img src=https://github.com/rikosintie/DevNetAssoc/blob/main/json-notes/images/textfsm-nornir-tech.png align="center" alt="Image Test" width=60% height=60%>
      <figcaption><b>Your caption here</b>
</figure>
