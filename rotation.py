import cv2

image = cv2.imread("ullu-app-web-series-actress-khushi-mukherjee-hot-photos-202204-1650530127.png")
if image is not None:
    print("Image loaded successfully.")
    #cv2.getRotationMatrix2D( center , angle , scale )
    M = cv2.getRotationMatrix2D((image.shape[1] // 2, image.shape[0] // 2), 45, 1)
    #cv2.wrapAffine(image, M, (width, height))
    #M is the rotation matrix , which contains the transformation to be applied 
    rotated_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    cv2.imshow("Original Image", image)
    print("Image rotated by 45 degrees.")
    # Display the rotated image
    cv2.imshow("Rotated Image", rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not read the image.")