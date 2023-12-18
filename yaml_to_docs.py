import yaml

# Constants
YAML_FILE_PATH:str = 'resources.yaml'
DOCS_DIRECTORY:str = 'docs/'


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

    build_docs(yaml_dump)

if __name__ == '__main__':
    yaml_to_docs()