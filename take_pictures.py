import time
import cv2
from playsound import playsound 

# Define the number of pictures to take
num_pictures = 3

# Initialize the camera
cap = cv2.VideoCapture(0)

for i in range(num_pictures):
    # Display countdown
    for count in range(4, 0, -1):
        print(count)
        time.sleep(1)
        if count == 1:
            # Play countdown sound
            playsound('Sound.wav')

    # Take a picture
    ret, frame = cap.read()
    print(ret,frame)
    cv2.imwrite(f'picture_{i+1}.jpg', frame)

# Release the camera
cap.release()
cv2.destroyAllWindows()
