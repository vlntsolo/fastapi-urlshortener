import string
import random
from config import settings


def generate_slug() -> str:
    letters = string.ascii_letters + string.digits
    slug = ''.join(random.choice(letters) for i in range(6))
    return slug

def format_short_url(slug) -> str:
    return f"{settings.current_host}/{slug}"


def validate_secret(auth_header: str) -> bool:
    """One-endpoint middleware
    substitute to check private token
    """  
    if not settings.privateMode:
        # No validation required / going public
        return True
    try:
        token = auth_header.split(' ')[1]
    except:
        return False

    if token != settings.auth_secret.get_secret_value():
        return False
    
    return True