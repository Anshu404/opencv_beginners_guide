import cv2

image = cv2.imread("ullu-app-web-series-actress-khushi-mukherjee-hot-photos-202204-1650530127.png")

if image is None:
    print("Error: Could not read the image .")
else:
    print("Image loaded successfully.")
    # You can add more processing here if needed
    # For example, displaying the image
    cv2.imshow("Loaded Image", image)
    waitkey = cv2.waitKey(0)     # 0 - dabayega toh wo delete kar dega 
    cv2.destroyAllWindows()      # saare windows ko band kar dena 



    #now we will learn how to save the image 
