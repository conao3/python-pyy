import typer

app = typer.Typer()


@app.callback()
def callback():
    'pyy: Python meets YAML'
