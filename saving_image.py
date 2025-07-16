import cv2

image = cv2.imread("ullu-app-web-series-actress-khushi-mukherjee-hot-photos-202204-1650530127.png")
if image is not None:
    success = cv2.imwrite("output_image.png", image)
    if success:
        print("Image saved successfully.")
    else:
        print("Error: Could not save the image.")
else:
    print("Error: Could not read the image.")

    