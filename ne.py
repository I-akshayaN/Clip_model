import requests
from PIL import Image
from io import BytesIO

# Define the URL of the image
image_url = "https://images.pexels.com/photos/3408743/pexels-photo-3408743.jpeg"

# Ensure this URL is correct

# Print the URL to verify its correctness
print(f"Fetching image from: {image_url}")

try:
    # Check if the URL starts with 'http://' or 'https://'
    if not image_url.startswith(('http://', 'https://')):
        raise ValueError("URL must start with 'http://' or 'https://'")

    # Fetch the image
    response = requests.get(image_url)
    response.raise_for_status()  # Raise an error for bad status codes

    # Check content type
    content_type = response.headers.get('Content-Type')
    if content_type and content_type.startswith('image'):
        # Open the image
        image = Image.open(BytesIO(response.content))
        print("Image loaded successfully.")
    else:
        print(f"Content is not an image. Content-Type: {content_type}")

except requests.exceptions.MissingSchema:
    print("The URL is missing the schema (e.g., 'http://' or 'https://').")
except requests.exceptions.RequestException as e:
    print(f"Error fetching the image: {e}")
except Exception as e:
    print(f"Error opening image: {e}")
