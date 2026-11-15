# RobotArmPackages3

This is the third iteration of code for OxRAM's Robotic Arm project, started October 2026. This iteration uses native
Python concurrency libraries and not a framework like ROS2, in order to make the code space more accessible.

To use, execute `git clone https://github.com/OxRAMSociety/RobotArmPackages3.git', and use the newly created folder as a workspace.

## Setup

1. First, create the virtual environment: `python -m venv .venv`
2. Then, activate it:
  * For Windows, use `.venv\Scripts\activate`
  * For Linux, use `source .venv/bin/activate`
3. Then install the necessary packages.
* For Windows, use 
  ```sh
  python.exe -m pip install --upgrade pip
  pip install -r requirements.txt
  ```
* For Linux, use
  ```sh
  python -m pip install --upgrade pip
  pip install -r requirements.txt
  ```
4. Some sub-teams/tasks will have specific requirements for setup, follow the respective README.md to identify particular packages

## Helpful Resources
### Git
[This](https://github.com/javedali99/git-tutorial) git tutorial is good for getting an intuition about how git works. Although there is one important difference - instead of using forks (which are your "version" of the entire repository), we are using branches (a different "version" of the code, stored in the same repository). [This guide](https://github.com/git-guides) is a bit more information on them, as well as another decent explanation of how git works.
#### Quick guide for managing branches
1. Check you are currently in main ```git checkout main```
2. Create new branch and move to it ```git checkout -b <name>```
3. Commit regularly: ```git add <file_path>``` to add files to the commit, ```git commit -m <message>``` to commit
4. Push code to branch ```git push```

### Contribution Workflow
1. Propose a piece of work or ongoing issue using the Proposed Task Column in the [project](https://github.com/orgs/OxRAMSociety/projects/4). Explain the task, any previous work relevant to it, proposed actions, priority and the sub-team(s) related to it.
2. Discuss the proposed task. If suitable, move to Ready Column to be picked up at a later date. If currently impossible but needs to be done, move to Blocked. Otherwise, rejected
3. Assign tasks to yourself and the relevant sub-team leader, moving to In Progress. People can then start implementing it, recording current progress on the task every couple of meetings.
4. Move task to review if branch is ready to be combined, or Done if no code needs reviewing
Goals for this system are:
- Record all decisions so tasks can be easily picked up
- Ensure relevant information can be shared between the affected people
- Gives sub-teams power to organise their own workflow, whilst being aware of the current progress of the project
- Ensure it is easier for new or returning members to get into tasks quickly



