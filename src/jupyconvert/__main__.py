"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """JupyConvert."""


if __name__ == "__main__":
    main(prog_name="jupyconvert")  # pragma: no cover
