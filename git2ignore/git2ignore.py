#!/usr/bin/env python3
import re
import warnings
from dataclasses import dataclass
from pathlib import Path


TEMPLATE_DIR = Path(__file__).parents[0] / Path("templates")


@dataclass
class Template:
    """Manipulate gitignore templates.

    Args:
        save_path (str): Path to save .gitignore
    """

    save_path: str = "./"

    def __post_init__(self):

        self.template_dict = {
            f.stem.lower(): f.stem
            for f in TEMPLATE_DIR.iterdir()
            if f.is_file() and "gitignore" in f.name
        }

        self.base_dir = Path(self.save_path)
        self.gitignore = self.base_dir / Path(".gitignore")

    def print_available(self) -> int:
        """Print list of available templates."""

        print(f"git2ignore: {len(self.template_dict)} available templates are")
        for k in self.template_dict.keys():
            print(f" - {k}")

        return len(self.template_dict)

    def add_template(self, target: str) -> None:
        """Copy template to .gitignore"""

        if target in self.template_dict:

            template_path = TEMPLATE_DIR / Path(
                f"{self.template_dict[target]}.gitignore"
            )
            if self.gitignore.exists():
                warnings.warn(
                    UserWarning(
                        f"git2ignore: .gitignore already exists in {template_path.cwd()}! No further action required."
                    )
                )
            else:
                self.gitignore.write_text(template_path.read_text())
                print(
                    f"git2ignore: {self.template_dict[target]}.gitignore added in {self.save_path}!"
                )
        else:
            raise KeyError(f"git2ignore: {target} is not a valid template!")

    def add_arguments(self, args: str) -> None:
        """Add arguments to .gitignore"""

        if not self.gitignore.exists():
            warnings.warn(
                UserWarning(
                    f"git2ignore: .gitignore does not exist. {args} will be added to a blank .gitignore file."
                )
            )
            self.gitignore.touch()

        ignore_text = self.gitignore.read_text()

        # Sepration of arguments using comma is possible
        args = args.replace(",", " ")

        # Split args by whitespace/s
        args_splitted = re.split(r"[\s,]+", args)

        for arg in args_splitted:
            if re.search(arg, ignore_text):
                warnings.warn(
                    UserWarning(
                        f"git2ignore: argument ({args}) is already in .gitignore!"
                    )
                )
            else:
                with self.gitignore.open("a") as f:
                    print(f"git2ignore: adding {args} to .gitignore...")
                    f.write(f"\n{arg}")
        print("git2ignore: done!")

    def delete_gitignore(self) -> None:
        """Delete gitignore file created."""

        gitignore_path = Path(self.gitignore)
        if gitignore_path.exists():
            gitignore_path.unlink()
        else:
            warnings.warn(
                UserWarning(
                    "git2ignore: .gitignore does not exist! No action required."
                )
            )
