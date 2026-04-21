# Final Project: Capstone Ranking Web Application
# Created by: Hope Dysert
# Date: 04-15-2026
# AI Agents Used: VSCode Agent Which Autofilled Some of the Constraint Matrices

# Import all necessary libraries and modules to perform MILP optimization.
import numpy as np # Numerical Operations
from scipy.optimize import Bounds # Bounds for Optimization
from scipy.optimize import LinearConstraint # Linear Constraints for Optimization
from scipy.optimize import milp # MILP Optimization Method

# Placeholder Student Names
students = [
    "John Smith", "Bob Brown", "Alice Malice", "Bryce Pryce",
    "David Smavid", "Michael Wichael", "Chris P. Bacon", "Anna Bannana",
    "Evil Knievel", "Wompus Pompus", "Wagoogus Boogus", "Alex Johnson"
]

# Placeholder Projects
projects = ["Project A", "Project B", "Project C"]

# Track Number of Projects and Students
num_students = len(students)
num_projects = len(projects)

# Each Students Placeholder Ranking Shown in Rows, Columns are Projects
rankings = np.array([
    [1,2,3],
    [2,1,3],
    [1,3,2],
    [3,1,2],
    [2,3,1],
    [1,2,3],
    [3,1,2],
    [2,1,3],
    [1,3,2],
    [2,3,1],
    [3,2,1],
    [1,2,3]
])

# Higher preference rankings get higher values (1 being highest value).
value = (num_projects + 1) - rankings

# Maximum amounts of students in each capstone group.
capacities = np.array([4, 4, 4])

# Objective Function: Negate values for maximizing student preferences per each project.
c = -value.flatten()

# List to store constraints. 
constraints = []

# Equality Constraint Matrix
A_eq_students = np.zeros((num_students, num_students * num_projects))

# Each row is a student and each student is constrained to be a part of one project.
for i in range(num_students):
    for j in range(num_projects):
        A_eq_students[i, i * num_projects + j] = 1

# Each student assigned to one project.
b_eq_students = np.ones(num_students)

# Add equality constraints to constraint list.
constraints.append(LinearConstraint(A_eq_students, b_eq_students, b_eq_students))

# Inequality Constraint Matrix
A_ub_projects = np.zeros((num_projects, num_students * num_projects))

# Each column is a project and counts how many students are attached to it.
for j in range(num_projects):
    for i in range(num_students):
        A_ub_projects[j, i * num_projects + j] = 1

# Add inequality constraints to constraint list.
constraints.append(LinearConstraint(A_ub_projects, -np.inf, capacities))

# Each variable is binary: 0 not in group, 1 is + integrality is binary
bounds = Bounds(0, 1)
integrality = np.ones(num_students * num_projects)

# Run the MILP optimization method. Reshape the solution into a matrix.
result = milp(c=c, constraints=constraints, integrality=integrality, bounds=bounds)
x = result.x.reshape((num_students, num_projects)).astype(int)

# Print out each student and the project they were assigned to.
print("Assignment Results:")
for i in range(num_students):
    for j in range(num_projects):
        if x[i, j] == 1: 
            print(f"{students[i]} → {projects[j]}")