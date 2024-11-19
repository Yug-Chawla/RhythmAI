from fer import FER
import cv2
import os
import matplotlib.pyplot as plt
dataset_path = r'D:\dataset\data\Test\happy'

# Initialize FER detector
detector = FER()
for image_name in os.listdir(dataset_path)[:5]:
    image_path = os.path.join(dataset_path, image_name)

    # Read the image
    image = cv2.imread(image_path)

    # Convert image to RGB (FER library uses RGB format)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Get the top emotion from the image
    emotion, score = detector.top_emotion(image_rgb)

    # Print the detected emotion and confidence score
    print(f"Image: {image_name} - Detected Emotion: {emotion}, Confidence: {score}")
    # Display the image with the detected emotion
    plt.imshow(image_rgb)
    plt.title(f"Detected Emotion: {emotion}")
    plt.axis('off')
    plt.show()
