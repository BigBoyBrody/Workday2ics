import click
from tkinter import Tk, filedialog


@click.command()
@click.argument('filepath', required=False, type=click.Path(exists=True))
def main(filepath):

    if not filepath:
        Tk().withdraw()  # hide the empty tkinter root window
        filepath = filedialog.askopenfilename(
            title="Select Workday export",
            filetypes=[("Excel files", "*.xlsx")]
        )

    if not filepath: click.echo("No file selected."); return
    click.echo(f"Using file: {filepath}")


if __name__ == '__main__':
    main()