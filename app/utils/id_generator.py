import random
import string
import time

def generate_unique_id(prefix: str = "") -> str:
    """
    Generate a unique ID with optional prefix
    Format: {prefix}_{timestamp}_{random_6_chars}
    """
    timestamp = int(time.time())
    random_chars = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"{prefix}_{timestamp}_{random_chars}" if prefix else f"{timestamp}_{random_chars}" 