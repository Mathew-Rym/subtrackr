import click
from datetime import datetime
from models.subscription import Subscription
from utils.db import Session

@click.group()
def sub_cli():
    """Subscription management commands"""
    pass

@sub_cli.command()
@click.option('--name', prompt=True)
@click.option('--cost', prompt=True, type=float)
@click.option('--cycle', prompt=True, type=click.Choice(['monthly', 'yearly', 'weekly']))
@click.option('--next-payment', prompt=True, type=click.DateTime(formats=['%Y-%m-%d']))
def add(name, cost, cycle, next_payment):
    """Add a new subscription"""
    session = Session()
    sub = Subscription(
        name=name,
        cost=cost,
        billing_cycle=cycle,
        next_payment_date=next_payment.date()
    )
    session.add(sub)
    session.commit()
    click.echo(f"Added subscription: {name}")