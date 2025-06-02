import click
from models.user import User
from utils.db import Session

@click.group()
def auth_cli():
    """User authentication commands"""
    pass

@auth_cli.command()
@click.option('--username', prompt=True)
def register(username):
    """Register a new user"""
    session = Session()
    if session.query(User).filter_by(username=username).first():
        click.echo("Username already exists!")
        return
        
    user = User(username=username)
    session.add(user)
    session.commit()
    click.echo(f"User {username} registered successfully!")