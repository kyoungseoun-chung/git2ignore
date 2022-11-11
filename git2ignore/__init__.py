#!/usr/bin/env python3
import argparse
from typing import Any

from .git2ignore import Template

__version__ = "0.1.0"

GI_PARSE = argparse.ArgumentParser(
    prog="git2ignore",
    description="python interface to add gitignore template.",
)

GI_PARSE.add_argument(
    "-l",
    "--list",
    help="Print list of supported templates.",
    action="store_true",
)
GI_PARSE.add_argument(
    "-d", "--delete", help="Delete .gitignore file.", action="store_true"
)
GI_PARSE.add_argument(
    "-t", "--template", metavar="template", help="Add template to .gitignore."
)
GI_PARSE.add_argument(
    "-a",
    "--add",
    metavar="add",
    help="Add args as new lines to .gitignore. You can add multiple arguments serpated by whitespace/s or comma.",
    type=str,
)
GI_PARSE.add_argument(
    "-p",
    "--path",
    metavar="path",
    help="Custom path to save .gitignore. Default is current working directory.",
    type=str,
)


def main() -> None:
    """Main routine. Return dictionary for debugging purpose."""

    print(f"git2ignore version: {__version__}")
    argv = GI_PARSE.parse_args()
    # Set save location for .gitignore
    if argv.path is None:
        gitignore_dir = "./"
    else:
        gitignore_dir = argv.path

    template = Template(gitignore_dir)

    # Display list of available templates
    if argv.list:
        template.print_available()
        printed = True
    else:
        printed = False

    # Delete .gitignore
    if argv.delete:
        template.delete_gitignore()

    # Add template if the argument is given
    if argv.template is not None:
        save_template = argv.template
        template.add_template(save_template)

    # Add arguments to .gitignore if the argument is given
    if argv.add is not None:
        add_arguments = argv.add
        template.add_arguments(add_arguments)
