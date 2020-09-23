import cv2

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('crowd.png')
uncoloured_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_coordinates = trained_face_data.detectMultiScale(uncoloured_img)
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
print(face_coordinates)
cv2.imshow('Face?', img)

cv2.waitKey()
#
# webcam = cv2.VideoCapture(0)
# while True:
#     succ_frame_read, frame = webcam.read()
#     uncoloured_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     face_coordinates = trained_face_data.detectMultiScale(uncoloured_img)
#     for (x, y, w, h) in face_coordinates:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
#     cv2.imshow('Well done', frame)
#
#     key = cv2.waitKey(1)
#     if key == 81 or key == 113:
#         break
# # key = cv2.waitKey(1)
# webcam.release()

print('Code Completed')
