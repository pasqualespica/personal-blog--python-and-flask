import os
import random
import re   #   regular expression
import string
import unicodedata

from flask import current_app
from PIL import Image # used fro image

from blog import app

UPLOAD_FOLDER = app.config["UPLOAD_FOLDER"]

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

def save_picture(form_data):
    print("p7b---1")
    file_name = form_data.filename
    print("p7b---2", file_name)
    picture_name = generate_random_strings() + "-" + file_name
    print("p7b---3")
    picture_path = os.path.join(current_app.root_path, UPLOAD_FOLDER, picture_name)
    print("p7b---4")
    # modulo di PIL
    image = Image.open(form_data)
    image.save(picture_path)

    return picture_name
