
# Facial Recognition Attendance System

This repository contains the code and documentation for a Facial Recognition Attendance System. The project utilizes OpenCV, NumPy, and the face_recognition library to recognize faces in a live webcam feed, compare them against known faces, mark attendance with timestamps, and store real-time information in a CSV file.
## Screenshots
![WhatsApp Image 2024-02-01 at 00 54 21](https://github.com/vibhudixit123/attendance_project/assets/104568465/4df8603b-c3d0-415f-88da-bf38484abd74)
![WhatsApp Image 2024-02-01 at 00 54 22](https://github.com/vibhudixit123/attendance_project/assets/104568465/9cb9b18c-e538-434c-bfc3-3e9b112096e2)



## Dependencies:
cv2 (OpenCV)

numpy

face_recognition
## Code Overview:
Image Loading and Encoding:

Images of known individuals are loaded from the opencv project/ directory.
Each image is encoded using the face_recognition library to generate a face encoding.

Attendance Marking and Real-time Storage:

The script captures frames from the webcam feed.
For each frame, face locations and encodings are extracted using the face_recognition library.
The face encodings are compared against the known face encodings.
If a match is found, the corresponding name is retrieved, and attendance is marked in the CSV file with the timestamp.
Real-time information about the recognized face, including the name and timestamp, is stored in the CSV file.

Webcam Feed Display:

The script displays the live webcam feed.
Detected faces are framed with rectangles, and the name is displayed above the face.
## License

[MIT](https://choosealicense.com/licenses/mit/)

