import cv2

# x, y: The coordinates of the mouse pointer when the event occurred.
def find_coordinates(event, x, y, flags, params):
    
    # We only want to take action on a specific event: the left mouse button being pressed down.
    if event == cv2.EVENT_LBUTTONDOWN:
        
        print(f"Clicked at coordinates -> X: {x}, Y: {y}")

        
        # Define the font we will use to write the text.
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        # Prepare the text string that we want to draw.
        text_to_draw = f'({x}, {y})'
        
        # The main function to draw text on an image.
        cv2.putText(
            image,              # The image to draw on.
            text_to_draw,       # The text string to be written.
            (x, y),             # The (x, y) coordinate where the text will start (bottom-left corner).
            font,               # The font style to use.
            1,                  # The font scale (size).
            (0, 0, 255),        # The color of the text in BGR format. (0, 0, 255) is RED.
            2                   # The thickness of the text lines.
        )
        
        cv2.imshow("Image", image)

# --- Main part of the program ---

# Load an image from the file.
image = cv2.imread("ullu-app-web-series-actress-khushi-mukherjee-hot-photos-202204-1650530127.png")

# It's a good practice to check if the image was loaded successfully.
if image is not None:

    # Create a display window with the name "Image".
    cv2.imshow("Image", image)

    cv2.setMouseCallback("Image", find_coordinates)

    cv2.waitKey(0)


    # It closes all the windows that were opened by OpenCV.
    cv2.destroyAllWindows()

else:
    # If the image could not be loaded, print an error message.
    print("Error: Could not load the image. Please check the file path.")