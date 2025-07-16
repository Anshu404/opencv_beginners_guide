import cv2

image = cv2.imread("ullu-app-web-series-actress-khushi-mukherjee-hot-photos-202204-1650530127.png")
if image is not None:
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", grayscale_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not read the image.")