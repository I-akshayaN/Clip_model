import torch
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import requests
from io import BytesIO

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Load image from a URL or local file
image_url = "https://images.pexels.com/photos/3408743/pexels-photo-3408743.jpeg"

response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

# Define the question and possible answers
questions = [
    "What is in the image?",
    "Is there a person in the image?",
    "What color is the object in the image?"
]
# Process the image and text queries
inputs = processor(text=questions, images=image, return_tensors="pt", padding=True)

# Forward pass
with torch.no_grad():
    outputs = model(**inputs)

# Get the logits for the questions
logits_per_image = outputs.logits_per_image  # This is the similarity score
probs = logits_per_image.softmax(dim=1)  # Convert logits to probabilities

# Print the probabilities for each question
for i, question in enumerate(questions):
    print(f"Question: {question}")
    print(f"Probability: {probs[0][i].item():.4f}")

