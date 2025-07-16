import cv2

image = cv2.imread("ullu-app-web-series-actress-khushi-mukherjee-hot-photos-202204-1650530127.png")
if image is not None:
    print("Image loaded successfully.")
    #i want to draw the line between two points 
    start_point = (50, 50)  # Starting point of the line
    end_point = (200, 200)   # Ending point of the line
    color = (255, 0, 0)      # Color of the line in
    thickness = 2           # Thickness of the line
    cv2.line(image, start_point, end_point, color, thickness)
    cv2.imshow("Image with Line", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()     