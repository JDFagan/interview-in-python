# interview-in-python
A repo for practicing interview problems in Python 3.

## Environment

### Creating Environment
Assumes using Conda to manage one's Python environment.  Use following command to create Miniconda virtual environment to support this repo:

```bash
conda env update --name $(basename $(pwd)) --file environment.yml --prune
```

### Using your Environment
If you're using IDE like PyCharm, you'll want to set Prefences for Project Interpreter to the Conda env you just setup (e.g., ~/miniconda3/envs/interview-in-python/bin/python).

### Updating your Environment
If you update Conda packages or add new ones, you should sync/persist the change to the repo via the following command which will modify the root level file, environment.yml which you should then commit/push back to the repo:

```bash
$ cd Repositories/JDFagan/interview-in-python

$ conda env list
# conda environments:
#
base                  *  /Users/jdfagan/miniconda3
apollo                   /Users/jdfagan/miniconda3/envs/apollo
circleup                 /Users/jdfagan/miniconda3/envs/circleup
interview-in-python      /Users/jdfagan/miniconda3/envs/interview-in-python
kinsa                    /Users/jdfagan/miniconda3/envs/kinsa
lyric                    /Users/jdfagan/miniconda3/envs/lyric
yoda                     /Users/jdfagan/miniconda3/envs/yoda


$ . activate $(basename $(pwd))

(interview-in-python)
$ conda env export > environment.yml

(interview-in-python)
$ vi environment.yml  # Remove last line regarding prefix path which is local specific that conda unfortunately creates
```

## Source code

Lives in src subdirectories.  Use packages to generally categorize different major areas of Python interview practicing - whether they are from different websites or real interview questions experienced.

## Test code

Try to make use of TDD (test driven development) and write my unit tests first before writing underlying code to solve the various problems.  All test code assumes running with Pytest framework.

## Contributing

Contributions to interview-in-python are welcome.  If you have new interview questions or problems or if you have feedback on existing solutions, please feel free to send a PR.
