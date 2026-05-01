# ROBOTS.md

## Purpose
This project takes student rankings of capstone projects to assign students to a project based on their ranking preferences. Each project also has student capacity constraints and each student has the constraint of only being assigned one project. The project does this
through utilizing a MILP optimization method.

## Project Structure
- `Final/capstone_project_assigner.ipynb.py` runs the optimization method and handles the user interface
- `Final/tests/capstone_project_assigner_test.ipynb.py` has automated tests for the provided MILP optimization method 

## Key Project Concepts
- Constraint: Students must be assigned to exactly one project
- Constraint: Projects have group capacity constraints
- Preferences are weighted based on a rankings system where a higher rank is a higher value (1 is the highest rank, 4 is the lowest)
- Optimization Goal: Maximize the total preference score of each group

## Data Expectations
- Project Data must include the name of each project
- Student Data must include the name and rankings of each student
- Rankings in Student Data files are ordered (pick_1 to pick_4)
- 0 or missing values in rankings indicate no selection and will be ignored
- Validate that there are no duplicate rankings per student (warn if there are duplicate rankings)

## Constraints for AI Agents
- Preserve feasibility of the model by:
  - Making sure each student is assigned only once
  - Making sure the given group capacity limits are respected
- Maintain the reproducibility of results
- Clearly document any modifications to optimization logic
- Clearly document any modifications to testing logic

## Allowed
- Index public pages for search engines
- Use content snippets for summaries with attribution

## Disallowed
- Scraping user data or personal information
- Accessing `/private/` or `/admin/` routes
- Training AI models on proprietary content without explicit permission

## Rate Limits
- Maximum 1 request per minute
- Respect server load and back off on errors

## Attribution
If you use content from this site, please credit:
https://github.com/PurpleLampShade/AI-Final-Otherguys