import requests

import base64
from io import BytesIO

def convert_image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return img_base64

def load_data_from_url(url: str) -> dict:
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name: str):
    with open(file_name) as file:
        return f'<style>{file.read()}</style>'
    
# vchanges are don
nj="name"