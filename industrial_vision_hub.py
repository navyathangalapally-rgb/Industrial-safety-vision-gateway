import cv2
import time
import edge_vision_hub.web_gateway as gateway
import edge_vision_hub.safety_escalation as escalation

gateway.start_server()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

cap = cv2.VideoCapture(0)
closed_timer_start = None

while True:
    ret, frame = cap.read()
    if not ret: break
    frame = cv2.flip(frame, 1)
    gray = cv2.equalizeHist(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))
    operator_drowsy = False

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 6, minSize=(20, 20))
        
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(frame[y:y+h, x:x+w], (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        if len(eyes) == 0: operator_drowsy = True

    if operator_drowsy and len(faces) > 0:
        if closed_timer_start is None: closed_timer_start = time.time()
        elapsed = time.time() - closed_timer_start
        
        msg, color = escalation.process_safety_tier(elapsed, "Navya", time.time())
        cv2.putText(frame, msg, (20, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
    else:
        closed_timer_start = None
        gateway.current_active_tier = "TIER_0"
        cv2.putText(frame, "Operator: Navya | STATUS: ALERT", (25, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    cv2.imshow("Industrial Safety Edge Gateway", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()