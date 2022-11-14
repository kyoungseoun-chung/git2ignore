
# git2ignore

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

![CI status](https://github.com/kyoungseoun-chung/git2ignore/actions/workflows/git2ignore-action.yml/badge.svg)

Python interface to generate `.git-ignore` template.

Inspired by [git-ignore](https://github.com/qqpann/Git-ignore), but updated for the latest python version, and the package is managed by `poetry`.

## Dependency

There is no additional dependency to install for `git2ignore`. `git2ignore` only uses python standard library.

## Installation

We recommend you to install the package via `pip`

```zhs
python3 -m pip install git2ignore
```

## How-to-Use

- Supporting features

``` zsh
$ git2ignore -h
usage: git2ignore [-h] [-l] [-d [either blank or arguments]] [-t template]
                  [-a arguments] [-p path to save]

python interface to add gitignore template.

options:
  -h, --help            show this help message and exit
  -l, --list            Print list of supported templates.
  -d [either blank or arguments], --delete [either blank or arguments]
                        Delete .gitignore file or delete arguments in .gitignore
                        file.
  -t template, --template template
                        Add template to .gitignore.
  -a arguments, --add arguments
                        Add args as new lines to .gitignore. You can add multiple
                        arguments serpated by whitespace/s or comma.
  -p path to save, --path path to save
                        Custom path to save .gitignore. Default is current working
                        directory.
```

- List all available templates

  ```zsh
  git2ignore -l
  ```

- Add template
  - By default, `git2ignore` will store `.gitignore` file to current working directory: `./`

    ```zsh
    git2ignore -t python
    ```

  - However, you can also specify the path to store `.gitignore` file.

  > Note that, you have to attach `-p` flag and its directory path relative to the current working directory all the time (to add arguments mostly) unless you change your current location to the directory where you save the template.

    ```zsh
    git2ignore -t python -p ./git_repo/
    ```

- Add arguments to the template generated
  - If there is no template generated, this command will create a blank `.gitignore` file and add the arguments.

    ```zsh
    git2ignore -a .DS_Store ./tests/test_outputs/ # Using default path
    git2ignore -a .DS_Store ./tests/test_outputs/ -p ./git_repo/ # With custom path
    ```

- Delete `.gitignore` file

  ```zsh
  git2ignore -d
  ```

- Delete arguments in `.gitignore`

  ```zsh
  git2ignore -d .DS_Store  # Remove .DS_Store in .gitignore
  ```
