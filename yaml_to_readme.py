import yaml

def build_readme(yaml_dump):
    readme = "# IIIT Resources\n"
    readme += """
Contributors:

<a href="https://github.com/aflah02/SemWiseResourcesIIIT/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=aflah02/SemWiseResourcesIIIT" />
</a>

If you want to add resources but confused about markdown or how to start, please refer to this [guide](https://github.com/aflah02/SemWiseResourcesIIIT/blob/main/CONTRIBUTING.md)

[Essential Starters Guide](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

"""

    readme += "## Jump to specific semester\n"
    vals = ['Sem 1', 'Sem 2', 'Sem 3', 'Sem 4', 'Sem 5-8']
    cnt = 0
    for key in yaml_dump.keys():
        readme += f"- [{vals[cnt]}](#{key.replace(' ', '-').lower()})\n"
        readme += "<center>\n"
        readme += '\n'
        courses_str = "| "
        for course in yaml_dump[key].keys():
            course_link = course.lower()
            # replace & with empty string
            course_link = "#" + course_link.replace('&', '')
            courses_str += f"[{course}]({course_link}) | "
        readme += courses_str + "\n"
        readme += "|"
        for _ in yaml_dump[key].keys():
            readme += "----|"
        readme += "\n"
        readme += "</center>\n"
        readme += "\n"

        cnt += 1

    readme += "\n"

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
        yaml_dump = yaml.safe_load(f)

    readme = build_readme(yaml_dump)

    with open(readme_file_path, 'w') as f:
        f.write(readme)

if __name__ == "__main__":
    yaml_to_readme('resources.yaml', 'README_CI_CD.md')