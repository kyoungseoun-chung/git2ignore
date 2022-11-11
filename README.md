
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

- Delete `.gitignore`

    ```zsh
    git2ignore -d
    ```
