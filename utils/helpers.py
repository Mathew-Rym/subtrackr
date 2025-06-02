from datetime import datetime

def format_date(date_obj):
    """Format date object as YYYY-MM-DD string"""
    return date_obj.strftime('%Y-%m-%d')

def calculate_next_payment(last_date, cycle):
    """Calculate next payment date based on billing cycle"""
    if cycle == 'weekly':
        return last_date + timedelta(weeks=1)
    elif cycle == 'monthly':
        return last_date + timedelta(days=30)
    elif cycle == 'yearly':
        return last_date + timedelta(days=365)
    return last_date