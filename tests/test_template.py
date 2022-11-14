#!/usr/bin/env python3
from pathlib import Path

import pytest


def test_template():

    from git2ignore.git2ignore import Template

    template = Template("./tests/test_outputs/")

    # Remove template in test_outputs directory
    template.delete_gitignore(True)

    template_dir = Path("./git2ignore/templates/")

    # Check number of available templates in ./git2ignore/templates/
    all_templates = [
        f
        for f in template_dir.iterdir()
        if f.is_file() and "gitignore" in f.name
    ]

    assert template.print_available() == len(all_templates)

    # Add python template to test_outputs
    template.add_template("python")

    # Catch error with wrong template name
    with pytest.raises(KeyError):
        template.add_template("python_not_a_template")

    # Catch warning with existing .gitignore
    with pytest.warns(UserWarning):
        template.add_template("python")

    # Test adding arguments
    template.add_arguments(".DS_Store .vscode")

    assert (
        Path("./tests/test_outputs/.gitignore").read_text().splitlines()[-1]
        == ".vscode"
    )

    # Check duplication of arguments in .gitignore (also test with multiple whitespaces)
    with pytest.warns(UserWarning):
        template.add_arguments(".DS_Store     .vscode")

    # Test with comma separation
    with pytest.warns(UserWarning):
        template.add_arguments(".DS_Store, .vscode")

    template.delete_gitignore(".vscode")
    assert (
        Path("./tests/test_outputs/.gitignore").read_text().splitlines()[-1]
        == ".DS_Store"
    )
