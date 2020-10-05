# NDRT Programming Challenges

This repository is designed to help people get more comfortable with
programming in Python by doing practice problems.

## Instructions

### Initial Set-Up

To set up this repository on your laptop, type this command:

```bash
git clone https://github.com/pfaley/NDRT_Programming_Challenges.git
```

### Challenge Set-Up

When beginning a new challenge, you should first make sure that the
repository is updated.

```bash
git checkout master
git pull --rebase
```

After running these commands, you can create a branch to work on
the given problem. For example, here is the command you would
run to begin work on Problem 1.

```bash
git checkout -b problem01
```

Within the current folder, in this case `problem01`, write your
solution in a file called `solution.py`. Once you're done,
perform these commands to save your work to the remote repository.

Note: make sure you are in the `problem01` folder in your shell.

```bash
git add solution.py
git commit -m "Finished problem01"
git push -u origin problem01
```

For future problems, just replace `problem01` with whatever the
name of the current problem is.
