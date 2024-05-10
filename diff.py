import face_recognition

# Load the images
image1 = face_recognition.load_image_file("path/to/image.jpg")
image2 = face_recognition.load_image_file("path/to/second/image.jpg")

# Find face encodings for each image
encoding1 = face_recognition.face_encodings(image1)[0]
encoding2 = face_recognition.face_encodings(image2)[0]

# Compare the face encodings
results = face_recognition.compare_faces([encoding1], encoding2)

# Check if the faces match
if results[0]:
    print("The faces are likely of the same person.")
else:
    print("The faces are likely of different people.")
