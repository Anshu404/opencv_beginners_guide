import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break       

    cv2.imshow("Video Feed",frame)


# Problem kya hai?
# Kabhi-kabhi, khaas kar 64-bit computers par, cv2.waitKey() 
# sirf key ka code (jaise 113) nahi bhejta. Woh uske saath kuch extra information 
# bhi bhej deta hai, jisse number 113 se bada ho jaata hai. Lekin jo asli key ka 
# code hota hai, woh hamesha aakhri 8 bits mein hota hai.
    if cv2.waitKey(1) & 0Xff == ord('q'):
        print("Exiting video feed.")
        break

cap.release()
cv2.destroyAllWindows()