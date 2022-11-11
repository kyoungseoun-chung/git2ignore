#!/usr/bin/env python3
from pathlib import Path
from unittest import mock

from git2ignore import GI_PARSE
from git2ignore import main


def test_cli():
    """Test CLI functions."""

    # Delete
    with mock.patch(
        "argparse.ArgumentParser.parse_args",
        return_value=GI_PARSE.parse_args(
            ["-d", "-p", "./tests/test_outputs/"]
        ),
    ):
        main()

    # List
    with mock.patch(
        "argparse.ArgumentParser.parse_args",
        return_value=GI_PARSE.parse_args(["-l"]),
    ):
        main()

    # Add template
    with mock.patch(
        "argparse.ArgumentParser.parse_args",
        return_value=GI_PARSE.parse_args(
            ["-t", "python", "-p", "./tests/test_outputs/"]
        ),
    ):
        main()

    # Add arguments with template
    with mock.patch(
        "argparse.ArgumentParser.parse_args",
        return_value=GI_PARSE.parse_args(
            [
                "-t",
                "python",
                "-a",
                ".vscode, .DS_Store tests/",
                "-p",
                "./tests/test_outputs/",
            ]
        ),
    ):
        main()

    assert (
        Path("./tests/test_outputs/.gitignore").read_text().splitlines()[-3]
        == ".vscode"
    )
    assert (
        Path("./tests/test_outputs/.gitignore").read_text().splitlines()[-2]
        == ".DS_Store"
    )
    assert (
        Path("./tests/test_outputs/.gitignore").read_text().splitlines()[-1]
        == "tests/"
    )

    with mock.patch(
        "argparse.ArgumentParser.parse_args",
        return_value=GI_PARSE.parse_args(
            ["-d", "-p", "./tests/test_outputs/"]
        ),
    ):
        main()

    # Add argument without template
    with mock.patch(
        "argparse.ArgumentParser.parse_args",
        return_value=GI_PARSE.parse_args(
            ["-a", "I-love-python", "-p", "./tests/test_outputs/"]
        ),
    ):
        main()

    assert (
        Path("./tests/test_outputs/.gitignore").read_text().splitlines()[-1]
        == "I-love-python"
    )

    with mock.patch(
        "argparse.ArgumentParser.parse_args",
        return_value=GI_PARSE.parse_args(
            ["-d", "-p", "./tests/test_outputs/"]
        ),
    ):
        main()

    # Add fresh template
    with mock.patch(
        "argparse.ArgumentParser.parse_args",
        return_value=GI_PARSE.parse_args(
            ["-t", "python", "-p", "./tests/test_outputs/"]
        ),
    ):
        main()
