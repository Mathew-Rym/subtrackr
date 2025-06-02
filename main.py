import click
from commands import auth, subs, report
from utils.db import init_db

@click.group()
def cli():
    """SubTrackr - Subscription Expense Tracker"""
    init_db()

cli.add_command(auth)
cli.add_command(subs)
cli.add_command(report)

if __name__ == '__main__':
    cli()