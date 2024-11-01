# Mall-Tycoon
### Credits:
Ananda Irwin  
10/31/2024

## Overview
Welcome to Mall-Tycoon! This purpose of this program is to act as a general overview of concepts for Object Orientated
Program (OOP), capable of being used as an educational tool for future classes. Originally, this program was 
conceptualized as a means to demonstrate polymorphism. It quickly grew far beyond that, however. Heed my experience as a
warning against dropping your guard around Python. The amount of time between an idea popping into my head and being 
able to actually execute that idea is sufficiently small that I basically didn't think about whether it was a good idea
to actually implement said idea. If you're programming in any language, think about what you're doing first, because 
it'll save you a lot of headaches and late nights in the future.

Functionally, this program provides a text-based menu for the user to interact with, editing a mall from the ground up
or adding onto a previously saved mall. The user is capable of creating plots, creating products, and editing said plots
and products.

The general menu is as follows:

- Create a New Plot
- Edit Existing Plot
  - Edit Name of Plot
  - Edit Description of Plot
  - Edit Items/Services
    - Add Product
    - Remove Product
    - Edit Product
      - Edit Price
      - Edit Stock(Item) / Availability(Service)
  - Remove Plot
- Recall Product
- Load Data
- Save Data
- Display Mall Data
  - Shorthand
  - All Plot Information
  - Specific Store Information
  - Mall Statistics

Due to the simplicity of this program, you cannot move up a submenu once you have selected an option. There are some
cases in which, if a requirement is not met (or you choose to cancel), you will restart at the highest level menu.
For example, having no products to edit while being in the Edit Product menu will restart you at the top menu, allowing
you to select "Create a New Plot," "Edit Existing Plot," etc.

It is also worth noting that the error correction in this program does not account for different data types. If you
input a non-integer string for something that requires an integer or float, the program *will* crash. However, it will
correct invalid inputs if they are of the correct type. For example, if the program asks you for an integer between 1
and 5, entering 6 will prompt the program to ask again until a valid input has been made.

## Examples of Polymorphism
Polymorphism is an OOP concept that literally translates to "many forms." In programming, this is the ability for
functions or operators with the same name to be called on different objects. In Python and other languages,
polymorphism exists by default. For example, the len() function in Python takes in any string, list, dictionary, etc.
and outputs an integer for how large/long the argument is. (The same can be said for the .size() function in C++)

In this program, inheritance polymorphism is used a lot. Children classes inherit methods from their parent classes
and are able to overwrite them if need be. This means that we can use a given method for a class and all of its
children.

The following are examples of polymorphism in this program:

- __dict__() method exists for every class, which is used when saving classes to a json file.
- display_catalog() method exists for the Plot class and its children, and it can be called on any of those objects.
- add_product() and remove_product() methods exist for the Retailer class and its children.
- print_stats() method exists for the Product class and its children.
- copy_product() function takes in any Product class and copies it. Whether a product is an item or a service, the
  function is able to execute, which is an example of polymorphism.

## .JSON Files
JSON stands for JavaScript Object Notation. (Thankfully, it is not Java.) This allows a user to store data in an
extremely easy to read format. If you've ever looked at the configuration files in a video game or program on your
machine, they are often written in as .json files.

In Python, storing classes into a .json file is the easiest and simplest way to store a class's data. In order to store
a class into a JSON file, it must be serializable. Serialization is the process of converting a native data type into a
JSON data type. Remember that JSON has its own notation, so you cannot just convert any old Python object into a JSON
object. Luckily, the json library (type "import json" at the top of the file to import) is able to do this for us in 
some cases. Most importantly for our applications, it is able to convert a Python dictionary to a JSON object. From
there, we can directly put a dictionary into a .json file by using "dump(save_destination, file_object)"

A .json file generally should only contain one object. So how do we save multiple Python objects to one file, then? The
simplest way is to add nested dictionaries. In the program, products are nested within their respective stores and
stores are nested within the mall. Once all of your data is inside your dictionary, you can dump it to the .json file.



For a list of equivalent Python and JSON objects, the image here is useful:
https://media.geeksforgeeks.org/wp-content/uploads/20201125193115/Capture-660x274.PNG
All credit to GeeksForGeeks for providing this handy chart.