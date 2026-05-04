# AI Final Project: Capstone Project Assigner
## Project Description
This project serves to provide the ECCS Chair with a simple method to assign students to capstone projects based on student rankings and preferences. Student rankings and capstone projects are submitted via a set of CSV files into this application and the app then generates capstone assignments for students based on attempting to maximize student satisfaction via providing them their preferred projects.

The project is written in Python and works to assign projects through Mixed-Integer Linear Programming Optimization techniques.

## How Does the Application Work?
The app takes a given CSV file listing out all of the available capstone projects and a given CSV file listing out student names and rankings. 
Rankings are then converted to scores and the optimization method is used to maximize these scores for each project, thus maximizing student satisfaction.

Optimized assignments are then returned to the ECCS Chair and ready for proper assignment.
All assignment capacities are split evenly between students and any remaining students are put into groups in order as they prefer the projects as long as their preferred project has space, ensuring groups remain as even as possible while still prioritizing student preference.

## Downloading and Running the Application
To download and run in an executable:
- From this GitHub, go to the releases section
- Then...

To run from VSCode:
- Open this project in VSCode
- Go to the capstone_project_assigner.ipynb file
- Click the play button next to each section of code to allow them to run
- On the last section of code, click run and notice a new window will become visible in your taskbar
- Open the window to see the optimization program and click on a project to see students assigned to it

If you want to run the app's tests in VSCode:
- Go to capstone_project_assigner_test.ipynb under the tests folder
- Click the play button next to each section of code to allow them to run
- This should then display a list of test prompts telling you whether or not the prompts are passed

## Using the Application
In order to use the application, open the application, choose a given project CSV file, a student csv file, and...

## Example of Project CSV Input 
```csv
project_name
project1
project2
project3
project4
project5
project6
project7
project8
project9
project10
```

## Example of Student CSV Input
```csv
name,pick_1,pick_2,pick_3,pick_4
AA,7,8,6,9
AB,2,6,7,0
AC,6,0,1,10
AD,3,5,8,8
```

## AI Tools Used Cited 
- ChatGPT
  - Used for ideas on different types of quality tests to run on the optimization method
  - Used for figuring out data handling for the optimization method (what to do with zero ranks for example)
  - Used for checking program worked as intended (after manual + automatic testing)
- GitHub Copilot
  - Autofill feature used to speed up writing where it predicted intended code lines correctly
  - Note: Optimization method aided by autofill but ultimately the approach was taken from homework three
