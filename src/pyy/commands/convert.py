import typer


from .. import cli


@cli.app.command()
def convert():
    'Convert pyy to python'
    typer.echo('Convert pyy to python')
