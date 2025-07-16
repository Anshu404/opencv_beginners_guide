import cv2

image = cv2.imread("ullu-app-web-series-actress-khushi-mukherjee-hot-photos-202204-1650530127.png")
if image is not None:
    resized_image = cv2.resize(image , (100, 600))  # Resize to 100x600 pixels
    cv2.imshow("Original Image", image)
    cv2.imshow("Resized Image", resized_image)
    
    #cropped the image
    cropped_image= image[100:400, 200:500]  # Crop the image (y1:y2, x1:x2)
    cv2.imshow("Cropped Image", cropped_image)
    cv2.imwrite("cropped_image.png", cropped_image)  # Save the cropped image
    cv2.imwrite("resized_image.png", resized_image)  # Save the resized image
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not read the image.")