<!DOCTYPE html>
<html>
  <body>
   <div id="header" align="center">
    <img src="https://imgs.search.brave.com/FMPy6jQxP1mj7gQFsEqpuEZf4dqLmjakssjeXfr6c8A/rs:fit:1200:1200:1/g:ce/aHR0cHM6Ly9jZG4u/ZnJlZWJpZXN1cHBs/eS5jb20vaW1hZ2Vz/L2xhcmdlLzJ4L2Fp/cmJuYi1sb2dvLnBu/Zw" alt="airbnb image" height=300px>
    <h1 style="text-align: center;"> AirBnb Clone </h1>
    </div>
  

* [Project Description](#project-description)
* [Command interpreter](#command-interpreter)
  * [Starting the interpreter](#starting-the-interpreter)
  * [Using the interpreter](#using-the-interpreter)
  * [Examples](#interpreter-examples)

# Project Description
This project is a joint project as part of the ALX software engineering program.
Here, a simple clone of the AirBnb website is made and modifications at the backend is made with
the use of the [Command interpreter](#command-interpreter).
The AirBnb clone consists of
 * A command interpreter
 * A local storage that stores all instances created
 * Restful API to fetch and send data to and fro
 * A simple front-end implementation that works both static and dynamic

# Command interpreter
The command interpreter works for testing and debugging purposes.
With the command interpreter, instances can be created, modified, deleted , API, object file serialization and deserialization is done.

# Starting the interpreter
To start the interpreter, the console.py file is launched.

# Using the interpreter
To make use of the interpreter, the following commands presented in the table is used
<table>
  <thead>
    <tr class="bold">
      <td> <strong>Command</strong> </td>
      <td> <strong> Function </strong> </td>
      <td><strong>Implementation </strong> </td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td> help </td>
      <td> Displays all commands that function with the interpreter </td>
      <td> help </td>
    </tr>
    <tr>
      <td> quit </td>
      <td> Quits the interpreter </td>
      <td> quit </td>
    </tr>
    <tr>
      <td> update </td>
      <td> Updates a an instance </td>
      <td> update (object to update) </td>
    </tr>
    <tr>
      <td> create </td>
      <td> Create an instance on it's class </td>
      <td> create (object) </td>
    </tr>
    <tr>
      <td> destroy </td>
      <td> Deletes/destroys an instance </td>
      <td> destroy (instance name)</td>
    </tr>
    <tr>
      <td> &nbsp </td>
      <td> &nbsp </td>
      <td> &nbsp </td>
    </tr>
    <br>
    <br>
    <caption id="cap" align="center"> <i>commands for command interpreter</i> </caption>
    </table>
  </body>
  </html>
