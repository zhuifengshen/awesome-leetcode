#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os

if __name__ == '__main__':
    readme_template = 'README_TEMPLATE.md'
    readme_file = 'README.md'
    python_solution_dirpath = './docs/Leetcode_Solutions/Python'
    file_path_template = '- [{filename}](./docs/Leetcode_Solutions/Python/{file})\n'
    file_name_list = ''

    for dirpath, dirnames, filenames in os.walk(python_solution_dirpath):
        filenames.sort()
        for filename in filenames:
            file_name_list += file_path_template.format(filename=os.path.splitext(filename)[0], file=filename)
        break

    with open(readme_template, 'r') as fr, open(readme_file, 'w') as fw:
        content = fr.read()
        content = content.replace('{leetcode_solution_list}', file_name_list)
        # print(content)
        fw.write(content)

    print('Congratulation, readme file generate successfully!')
