import cv2

image = cv2.imread("ullu-app-web-series-actress-khushi-mukherjee-hot-photos-202204-1650530127.png")
if image is not None:
    print("Image loaded successfully.")
    flipped_image_horizontally = cv2.flip(image, 1)  # Flip horizontally
    flipped_image_vertically = cv2.flip(image, 0)    # Flip vertically
    flipped_image_both = cv2.flip(image, -1)        # Flip both horizontally and vertically
    cv2.imshow("Original Image", image)
    print("Image flipped horizontally, vertically, and both.")
    # Display the flipped images
    cv2.imshow("Flipped Horizontally", flipped_image_horizontally)
    cv2.imshow("Flipped Vertically", flipped_image_vertically)
    cv2.imshow("Flipped Both", flipped_image_both)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not read the image.")