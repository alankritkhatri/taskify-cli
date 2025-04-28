from setuptools import setup, find_packages

setup(
    name='heytaskify',
    version = "1.0.7",
    description = "A command-line task management application for tracking and organizing your tasks",
    long_description = """
# Commands

1. Add Task
```
heytaskify addtask "Task Title" --description "task description" --status "pending" --duedate "22-3-2014"
```

To create multiple tasks at once (adding more arguments to each flag):
```
heytaskify addtask "Task Title" "Task 2 Title" --description "task description" "task 2  description" --status "pending"  "pending" --duedate "22-3-2014" "22-3-2014"
```

2. Show Tasks
```
heytaskify showtasks
```

3. Show Stats
```
heytaskify stats
```

4. Delete Task
```
heytaskify deletetask <task_number>
```

5. Update Status
```
heytaskify updatestatus <task_number> <new_status>
```
""",
    long_description_content_type = "text/markdown",
    packages=find_packages(),
    install_requires=[
        'click==8.1.8',
        'art',
        'colorama==0.4.6',
        'inspirational-quotes',
        'certifi==2025.1.31',
        'charset-normalizer==3.4.1',
        'docopt==0.6.2',
        'docutils==0.21.2',
        'id==1.5.0',
        'idna==3.10',
        'jaraco.classes==3.4.0',
        'jaraco.context==6.0.1',
        'jaraco.functools==4.1.0',
        'keyring==25.6.0',
        'markdown-it-py==3.0.0',
        'mdurl==0.1.2',
        'more-itertools==10.7.0',
        'nh3==0.2.21',
        'packaging==25.0',
        'pipreqs==0.4.13',
        'pyfiglet==1.0.2',
        'Pygments==2.19.1',
        'pywin32-ctypes==0.2.3',
        'readme_renderer==44.0',
        'requests==2.32.3',
        'requests-toolbelt==1.0.0',
        'rfc3986==2.0.0',
        'rich==14.0.0',
        'setuptools==79.0.1',
        'tabulate==0.9.0',
        'twine==6.1.0',
        'urllib3==2.4.0',
        'wheel==0.45.1',
        'yarg==0.1.10',
    ],
    entry_points={
        'console_scripts': [
            'heytaskify = taskify.main:main',
        ],
    },
)
