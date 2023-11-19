# install using 'pip install opencv-python'
import cv2
import dlib

# Downloaded from "http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2" using wget or curl
# unzip in command line using "bzip2 -d shape_predictor_68_face_landmarks.dat.bz2"
predictor = dlib.shape_predictor("python/shape_predictor_68_face_landmarks.dat") # change the ("") to the path for .dat file
detector = dlib.get_frontal_face_detector()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = detector(gray)
    
    for face in faces:
        landmarks = predictor(gray, face)
        
        for i in range(68):
            x,y = landmarks.part(i).x, landmarks.part(i).y
            cv2.circle(frame, (x,y), 2, (0, 255, 0), -1)
            
    cv2.imshow('Facial Landmark Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
     
cap.release()
cv2.destroyAllWindows()