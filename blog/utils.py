import random
import re   #   regular expression
import string
import unicodedata

ALPHANUMERIC_CHARS = string.ascii_lowercase + string.digits
STRING_LENGTH = 6

def generate_random_strings(chars=ALPHANUMERIC_CHARS, length=STRING_LENGTH):
    """ 
    genera un stringa casuale di 6 carattere alfanumerica
    """
    return "".join(random.choice(chars) for _ in range(length))

def slugify(value):
    """
    versione modificata di slugify di Django
    value : title
    """
    value = str(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii','ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return re.sub(r'[-\s]+', '-', value)

def title_slugfier(post_title):
    slug = slugify(post_title) + "-" + generate_random_strings()
    return slug


