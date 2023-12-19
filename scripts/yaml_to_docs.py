import yaml

# Constants
YAML_FILE_PATH:str = 'resources.yaml'
DOCS_DIRECTORY:str = 'docs/'
INIT_README:str = 'scripts/init_readme.md'
FINAL_README:str = 'docs/index.md'

def build_index(yaml_dump:str) -> None:
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
    
    # write to README.md
    with open(FINAL_README, 'w') as f:
        f.write(readme)


def build_docs(yaml_dump:str) -> None:
    for semester in yaml_dump.keys():
        # Create file name
        file_name = semester.replace(' ', '-').lower()
        file_name = DOCS_DIRECTORY + file_name + '.md'

        # Create content
        content = ""

        # Add header
        for course in yaml_dump[semester].keys():
            content += f"### {course}\n"
            resources, notes = yaml_dump[semester][course]
            
            # Add resources and notes
            for note in notes:
                content += f"> {note}\n\n"
            for resource in resources:
                content += f"- {resource}\n"
            content += "\n"

        # Write to file
        with open(file_name, 'w') as f:
            f.write(content)



def yaml_to_docs() -> None:
    with open(YAML_FILE_PATH, 'r') as f:
        yaml_dump = yaml.load(f, Loader=yaml.FullLoader)

    build_index(yaml_dump)
    build_docs(yaml_dump)

if __name__ == '__main__':
    yaml_to_docs()