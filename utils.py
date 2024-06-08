# utils.py
import datetime
import pytz

def get_current_time(timezone=None):
    """
    Returns the current time in the specified timezone.
    
    Args:
    timezone: A string representing the timezone (e.g., "UTC", "Europe/Paris").
              If not provided, defaults to UTC.
    
    Returns:
    A string representing the current time in the specified timezone in the format "YYYY-MM-DD HH:MM:SS".
    """
    if timezone:
        try:
            tz = pytz.timezone(timezone)
        except pytz.exceptions.UnknownTimeZoneError:
            raise ValueError(f"Invalid timezone: {timezone}")
        now = datetime.datetime.now(tz=tz)
    else:
        now = datetime.datetime.utcnow()
    return now.strftime("%Y-%m-%d %H:%M:%S")