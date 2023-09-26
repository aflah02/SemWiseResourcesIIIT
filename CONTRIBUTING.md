# Contributions Guide for the Resources Repository

Thank you for contributing to our resources repository! Your contributions help make this repository a valuable resource for others. To ensure consistency and ease of navigation, please follow the guidelines below when adding courses and resources.

## Adding Courses

1. Navigate to the relevant section where you want to add the course.

   ```markdown
   ### Semester/Year
   ```

2. Under the appropriate semester/year heading, add the course using the following format:

   ```markdown
   ### Course Abbreviation (e.g., ATP)

   > Notes (if any) otherwise omit this

   - [Course Resource 1](URL to Course Resource 1)
   - [Course Resource 2](URL to Course Resource 2)
   
   ```

3. If you're the first contributor to add a course for a specific semester/year, please also add the course abbreviation and a link to it at the top of the repository for quicker navigation. For example if you are adding a course for the first semester then modify the table below accordingly:

   ```markdown
   | [IP](#ip) | [DC](#dc) | [LA](#la) | [HCI](#hci) | [COM](#com) |
   |----|----|----|-----|------|
   ```

   Ensure that the course abbreviation and the corresponding anchor link (e.g., `#ip`) match the format used in your course entry.
   To modify the table you need to add the course name you want to display in the navigation menu in `[]` and the lowercase version of the same in the `()`
   At the same time also add `------|` in the row below 

## Example

Here's an example of how to add a course for the Spring 2023 semester:

```markdown
### Semester 2

### New Course

> Taken Professor XYZ in Monsoon 2023

- [Resource 1](google.com)
- [Resource 2](google.com)
```

Thank you for your contribution! Your efforts help make this repository a valuable resource for everyone.
