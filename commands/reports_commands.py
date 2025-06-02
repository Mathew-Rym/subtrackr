import click
from datetime import datetime, timedelta
from models import Subscription
from utils.db import session
from utils.helpers import format_date

@click.group()
def report():
    """Generate subscription reports"""
    pass

@report.command()
def monthly_total():
    """Calculate total monthly expenses"""
    subs = session.query(Subscription).all()
    
    monthly_cost = sum(
        sub.cost for sub in subs 
        if sub.billing_cycle == 'monthly'
    )
    
    yearly_to_monthly = sum(
        sub.cost / 12 for sub in subs 
        if sub.billing_cycle == 'yearly'
    )
    
    weekly_to_monthly = sum(
        sub.cost * 4 for sub in subs 
        if sub.billing_cycle == 'weekly'
    )
    
    total = monthly_cost + yearly_to_monthly + weekly_to_monthly
    click.echo(f"Total monthly expenses: ${total:.2f}")

@report.command()
def upcoming():
    """Show subscriptions due in the next 7 days"""
    today = datetime.now().date()
    next_week = today + timedelta(days=7)
    
    upcoming_subs = session.query(Subscription).filter(
        Subscription.next_payment_date >= today,
        Subscription.next_payment_date <= next_week
    ).all()
    
    if not upcoming_subs:
        click.echo("No upcoming payments in the next 7 days")
        return
    
    click.echo("Upcoming subscriptions:")
    for sub in upcoming_subs:
        days_until = (sub.next_payment_date - today).days
        click.echo(
            f"- {sub.name}: ${sub.cost} "
            f"(due in {days_until} days on {format_date(sub.next_payment_date)})"
        )

@report.command()
@click.option('--threshold', default=10.0, help='Minimum cost to filter by')
def expensive(threshold):
    """List subscriptions above a certain cost"""
    expensive_subs = session.query(Subscription).filter(
        Subscription.cost >= threshold
    ).order_by(Subscription.cost.desc()).all()
    
    if not expensive_subs:
        click.echo(f"No subscriptions cost ${threshold} or more")
        return
    
    click.echo(f"Subscriptions costing ${threshold}+ per billing cycle:")
    for sub in expensive_subs:
        click.echo(f"- {sub.name}: ${sub.cost} ({sub.billing_cycle})")

@report.command()
def summary():
    """Show a complete subscription summary"""
    all_subs = session.query(Subscription).all()
    
    # Count by billing cycle
    cycles = {}
    for sub in all_subs:
        cycles[sub.billing_cycle] = cycles.get(sub.billing_cycle, 0) + 1
    
    click.echo("\nSubscription Summary:")
    click.echo(f"Total subscriptions: {len(all_subs)}")
    for cycle, count in cycles.items():
        click.echo(f"- {count} {cycle} subscriptions")
    
    # Most expensive
    if all_subs:
        most_expensive = max(all_subs, key=lambda x: x.cost)
        click.echo(f"\nMost expensive: {most_expensive.name} (${most_expensive.cost})")
    
    # Next payment
    upcoming = session.query(Subscription).order_by(
        Subscription.next_payment_date
    ).first()
    if upcoming:
        days_until = (upcoming.next_payment_date - datetime.now().date()).days
        click.echo(
            f"Next payment: {upcoming.name} "
            f"in {days_until} days ({format_date(upcoming.next_payment_date)})"
        )