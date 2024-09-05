# Problem Structure Creator

This script creates a folder structure for competitive programming problems, including a C++ file with a template, and empty input and output files.

## Usage

```
python template_generator.py <path> <problem_name>
```

### Arguments:
- `path`: The base path where the problem folder will be created.
- `problem_name`: The name of the problem (will be used as folder name).

### Optional flag:
- `--add-code`: (Currently unused) Intended to automatically add default content to the .cpp file.

## Example

```
python template_generator.py /home/user/cp_problems new_problem
```

This will create a folder named `new_problem` in `/home/user/cp_problems` with the following structure:

```
new_problem/
├── new_problem.cpp
├── input.txt
└── output.txt
```

## Requirements

- Python 3.x
