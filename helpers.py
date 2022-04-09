import string
import random
from config import settings


def generate_slug():
    letters = string.ascii_letters + string.digits
    slug = ''.join(random.choice(letters) for i in range(6))
    return slug

def format_short_url(slug):
    return f"{settings.current_host}/{slug}"