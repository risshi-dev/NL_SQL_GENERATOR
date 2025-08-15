# import external libraries
import typer
import getpass
import time
from dotenv import load_dotenv, dotenv_values

#import modules
from context.relationalContext import MySqlContext
from rich.progress import track
from RAG.pipleline import Embed
from model.gemini import Gemini

app = typer.Typer()
config = dotenv_values('.env')
load_dotenv()


@app.command()
def execute():
    typer.secho("Please provide your database credentials.", fg=typer.colors.CYAN)
    
    host        = config.get('HOST') or typer.prompt("Host")
    username    = config.get('USERNAME') or typer.prompt("Username")
    password    = config.get('PASSWORD') or getpass.getpass("Password: ")
    database    = config.get('DATABASE') or typer.prompt("Database")

    try:
        builder = MySqlContext(host, username, password, database)
        builder.get_schema_information()
    except Exception as e:
        typer.echo("Error connecting database...")
        raise typer.Exit()

    try:
        pipeline = Embed(builder._schema_output, database)
        pass
    except Exception as e:
        typer.echo("Error embedding data")
        raise typer.Exit()
    
    try:
        gemini = Gemini(pipeline=pipeline)
        pass
    except Exception:
        pass
    
    for value in track(range(100), description=typer.secho("\nConnecting to the database...", fg=typer.colors.RED)):
        time.sleep(0.001)

    typer.echo("You can now start typing your questions. Type 'exit' to quit.")
    
    while True:
        query = typer.prompt(">")
        
        if query.lower() == "exit":
            typer.secho("Select Exit from CLI", fg=typer.colors.BRIGHT_YELLOW)
            raise typer.Exit()
        
        typer.echo(f"Processing query: ...")
        queryOutput = gemini.generate_query(query)
        typer.echo(queryOutput)
        runQuery = typer.prompt("Y to run query or N to pass")

        if runQuery.lower() == 'y' :
            typer.echo(builder.query(queryOutput))

if __name__ == "__main__":
    app()