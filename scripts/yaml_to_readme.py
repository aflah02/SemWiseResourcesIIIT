import yaml

YAML_FILE_PATH:str = 'resources.yaml'
INIT_README:str = 'scripts/init_readme.md'
FINAL_README:str = 'README.md'

def build_index(yaml_dump:str) -> str:
    # open the init_readme.md file
    with open(INIT_README, 'r') as f:
        readme = f.read()
    
    # start creating the table
    readme += "\n| Semester | Courses |"
    readme += "\n| --- | --- |\n"

    # add the semesters
    for semester in yaml_dump.keys():
        sem_link = semester.replace(' ', '-').lower()
        readme += f"| [{semester}]({sem_link}) | "
        cnt = 0
        # add the courses
        for course in yaml_dump[semester].keys():
            cnt += 1
            course_link = course.lower()
            # replace & with empty string
            course_link = sem_link + "#" + course_link.replace('&', '')
            readme += f"[{course}]({course_link}) "
            if (cnt == 10):
                readme += '<br><br>'
                cnt = 0

        # add the new line
        readme += "|\n"
    
    return readme

def build_content(yaml_dump:str) -> str:
    readme = "\n"

    for semester_heading in yaml_dump.keys():
        readme += f"## {semester_heading}\n"
        for course in yaml_dump[semester_heading]:
            readme += f"### {course}\n"
            resources, notes = yaml_dump[semester_heading][course]
            for note in notes:
                readme += f"> {note}\n"
            for resource in resources:
                readme += f"- {resource}\n"
            readme += "\n"
        readme += "\n"

    readme += """
---
> ## Course Books : [here](https://drive.google.com/drive/folders/1Xhwlwbhj1HP6R9BysSoXcqScWFsnIj7B?usp=sharing)
"""

    return readme

def yaml_to_readme(yaml_file_path, readme_file_path):
    with open(yaml_file_path, 'r') as f:
        yaml_dump = yaml.load(f, Loader=yaml.FullLoader)

    readme = build_index(yaml_dump)
    readme += build_content(yaml_dump)

    with open(readme_file_path, 'w') as f:
        f.write(readme)

if __name__ == "__main__":
    yaml_to_readme('resources.yaml', 'README.md')