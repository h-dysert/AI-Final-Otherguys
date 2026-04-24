# AI Final Project: Capstone Project Assigner
## Project Description
This project serves to provide the ECCS Chair with a simple method to assign students to capstone projects based on student rankings and preferences. Student rankings are submitted via a CSV file into this application and the app then generates capstone assignments for students based on attempting to maximize student satisfaction via providing them their preferred projects.

The project is written in Python with a Jupyter notebook and works to assign projects through Mixed-Integer Linear Programming Optimization techniques.

## How Does the Application Work?
The app takes a given CSV file listing out all of the available capstone projects and a given CSV file listing out student names and rankings. 
Rankings are then converted to scores and the optimization method is used to maximize these scores for each project, thus maximizing student satisfaction.

Optimized assignments are then returned to the ECCS Chair and ready for proper assignment.
All assignment capacities are split evenly between students and any remaining students are put into groups in order as they are listed on the CSV,
ensuring groups remain as even as possible.
