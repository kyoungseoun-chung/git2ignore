#!/usr/bin/env python3
import argparse

from .git2ignore import Template

__version__ = "0.1.3"

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
    "-d",
    "--delete",
    nargs="?",
    const=True,
    metavar="either blank or arguments",
    help="Delete .gitignore file or delete arguments in .gitignore file.",
)
GI_PARSE.add_argument(
    "-t", "--template", metavar="template", help="Add template to .gitignore."
)
GI_PARSE.add_argument(
    "-a",
    "--add",
    metavar="arguments",
    help="Add args as new lines to .gitignore. You can add multiple arguments serpated by whitespace/s or comma.",
    type=str,
)
GI_PARSE.add_argument(
    "-p",
    "--path",
    metavar="path to save",
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

    # Delete .gitignore or delete arguments in .gitignore
    # This is prior to all operation including copy template and add.
    if argv.delete or isinstance(argv.delete, str):
        template.delete_gitignore(argv.delete)

    # Add template if the argument is given
    # Always check template before adding arguments.
    if argv.template is not None:
        template.add_template(argv.template)

    # Add arguments to .gitignore if the argument is given
    if argv.add is not None:
        template.add_arguments(argv.add)


if __name__ == "__main__":

    main()
