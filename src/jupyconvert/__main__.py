"""Command-line interface."""
import click

from .functions import files_to_convert


@click.command()
@click.version_option()
@click.option("--to", required=True, type=click.Choice(["nb", "py"]))
def main(to: str) -> None:
    """JupyConvert."""
    file_list = files_to_convert("py")
    print(f"This is the jupyconvert application, converting to {to}")
    print(f"{file_list=}")


if __name__ == "__main__":
    main(prog_name="jupyconvert")  # pragma: no cover
