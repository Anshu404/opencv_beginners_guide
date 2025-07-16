import cv2

image = cv2.imread("ullu-app-web-series-actress-khushi-mukherjee-hot-photos-202204-1650530127.png")

if image is not None:
    h,w,c = image.shape
    print(f"Image dimensions: Height = {h}, Width = {w}, Channels = {c}")
else:
    print("Error: Could not read the image.")
