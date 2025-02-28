# # import cv2
# # import numpy as np
# # import os
# # from datetime import datetime
# # import time
# # import requests

# # def load_known_faces(image_directory):
# #     known_faces = []
# #     face_names = []
    
# #     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
# #     if not os.path.exists(image_directory):
# #         print("Error: Image directory not found.")
# #         return [], []

# #     for image_name in os.listdir(image_directory):
# #         if not image_name.lower().endswith(('.png', '.jpg', '.jpeg')):
# #             continue

# #         image_path = os.path.join(image_directory, image_name)
# #         print(f"Processing: {image_path}")
# #         img = cv2.imread(image_path)
# #         if img is None:
# #             print(f"Error: Could not load {image_path}")
# #             continue

# #         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #         faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# #         if len(faces) > 0:
# #             print(f"Found {len(faces)} faces in {image_name}")
# #             x, y, w, h = faces[0]
# #             face_roi = gray[y:y+h, x:x+w]
# #             face_roi = cv2.resize(face_roi, (128, 128))
# #             known_faces.append(face_roi)
# #             face_names.append(os.path.splitext(image_name)[0])
# #             print(f"Successfully processed face from {image_name}")
# #         else:
# #             print(f"No faces found in {image_name}")
# #     return known_faces, face_names

# # def compare_faces(known_face, current_face, threshold=0.5):
# #     current_face = cv2.resize(current_face, (known_face.shape[1], known_face.shape[0]))

# #     # Use Template Matching for face comparison
# #     result = cv2.matchTemplate(current_face, known_face, cv2.TM_CCOEFF_NORMED)
# #     max_similarity = np.max(result)

# #     return max_similarity >= threshold

# # def mark_attendance(name):
# #     if not os.path.exists("Attendance.csv"):
# #         with open("Attendance.csv", "w") as file:
# #             file.write("Name,Timestamp\n")
# #     with open("Attendance.csv", "r+") as file:
# #         lines = file.readlines()
# #         recorded_names = [line.split(",")[0] for line in lines]
# #         if name not in recorded_names:
# #             now = datetime.now()
# #             timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
# #             file.write(f"{name},{timestamp}\n")
# #             print(f"Attendance marked for {name}")


# # def process_video_stream(video_url, known_faces, face_names):
# #     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# #     while True:
# #         try:
# #             response = requests.get(video_url, timeout=5)  # Increased timeout to 10 seconds
# #             if response.status_code == 200:
# #                 arr = np.frombuffer(response.content, np.uint8)
# #                 frame = cv2.imdecode(arr, cv2.IMREAD_COLOR)

# #                 if frame is None:
# #                     print("Error: Could not decode frame.")
# #                     # time.sleep(1)
# #                     continue

# #                 gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# #                 faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# #                 for (x, y, w, h) in faces:
# #                     face_roi = gray[y:y + h, x:x + w]
# #                     face_roi = cv2.resize(face_roi, (128, 128))

# #                     best_match = "Unknown"
# #                     for known_face, name in zip(known_faces, face_names):
# #                         if compare_faces(known_face, face_roi):
# #                             best_match = name
# #                             break

# #                     if best_match != "Unknown":
# #                         mark_attendance(best_match)

# #                     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
# #                     cv2.putText(frame, best_match, (x, y - 10),
# #                                 cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

# #                 cv2.imshow('Face Recognition', frame)

# #                 if cv2.waitKey(1) & 0xFF == ord('q'):
# #                     print("Exiting video stream.")
# #                     break
# #             else:
# #                 print(f"Error fetching frame: {response.status_code}")
# #         except Exception as e:
# #             print(f"Error during video processing: {str(e)}")
# #             print("Retrying connection...")
# #             time.sleep(2)  # Wait for a few seconds before retrying

# #     cv2.destroyAllWindows()


# # def main():
# #     script_dir = os.path.dirname(os.path.abspath(__file__))
# #     image_directory = os.path.join(script_dir, "ImagesBasic")
# #     print(f"Looking for images in: {image_directory}")
# #     video_url = "http://192.168.108.170/cam-hi.jpg" 
# #     known_faces, face_names = load_known_faces(image_directory)

# #     if not known_faces:
# #         print("No faces loaded. Exiting...")
# #         return

# #     print("Starting video stream...")
# #     process_video_stream(video_url, known_faces, face_names)

# # if __name__ == "__main__":
# #     main()



# import cv2
# import numpy as np
# import os
# from datetime import datetime
# import time
# import requests

# def load_known_faces(image_directory):
#     known_faces = []
#     face_names = []
    
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
#     if not os.path.exists(image_directory):
#         print("Error: Image directory not found.")
#         return [], []

#     for image_name in os.listdir(image_directory):
#         if not image_name.lower().endswith(('.png', '.jpg', '.jpeg')):
#             continue

#         image_path = os.path.join(image_directory, image_name)
#         print(f"Processing: {image_path}")
#         img = cv2.imread(image_path)
#         if img is None:
#             print(f"Error: Could not load {image_path}")
#             continue

#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, 1.1, 4)

#         if len(faces) > 0:
#             print(f"Found {len(faces)} faces in {image_name}")
#             x, y, w, h = faces[0]
#             face_roi = gray[y:y+h, x:x+w]
#             face_roi = cv2.resize(face_roi, (128, 128))
#             known_faces.append(face_roi)
#             face_names.append(os.path.splitext(image_name)[0])
#             print(f"Successfully processed face from {image_name}")
#         else:
#             print(f"No faces found in {image_name}")
#     return known_faces, face_names

# def compare_faces(known_face, current_face, threshold=0.5):
#     current_face = cv2.resize(current_face, (known_face.shape[1], known_face.shape[0]))

#     # Use Template Matching for face comparison
#     result = cv2.matchTemplate(current_face, known_face, cv2.TM_CCOEFF_NORMED)
#     max_similarity = np.max(result)

#     return max_similarity >= threshold

# def mark_attendance(name, attendance_record):
#     if name in attendance_record:
#         return  # Skip marking duplicate attendance

#     if not os.path.exists("Attendance.csv"):
#         with open("Attendance.csv", "w") as file:
#             file.write("Name,Timestamp\n")

#     with open("Attendance.csv", "a") as file:
#         now = datetime.now()
#         timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
#         file.write(f"{name},{timestamp}\n")
#         attendance_record.add(name)
#         print(f"Attendance marked for {name}")

# def process_video_stream(video_url, known_faces, face_names):
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#     attendance_record = set()  # Stores already marked names

#     while True:
#         try:
#             response = requests.get(video_url, timeout=5)
#             if response.status_code == 200:
#                 arr = np.frombuffer(response.content, np.uint8)
#                 frame = cv2.imdecode(arr, cv2.IMREAD_COLOR)

#                 if frame is None:
#                     print("Error: Could not decode frame.")
#                     continue

#                 gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#                 faces = face_cascade.detectMultiScale(gray, 1.1, 4)

#                 for (x, y, w, h) in faces:
#                     face_roi = gray[y:y + h, x:x + w]
#                     face_roi = cv2.resize(face_roi, (128, 128))

#                     best_match = "Unknown"
#                     for known_face, name in zip(known_faces, face_names):
#                         if compare_faces(known_face, face_roi):
#                             best_match = name
#                             break

#                     if best_match != "Unknown":
#                         mark_attendance(best_match, attendance_record)

#                     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#                     cv2.putText(frame, best_match, (x, y - 10),
#                                 cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

#                 cv2.imshow('Face Recognition', frame)

#                 if cv2.waitKey(1) & 0xFF == ord('q'):
#                     print("Exiting video stream.")
#                     break
#             else:
#                 print(f"Error fetching frame: {response.status_code}")
#         except Exception as e:
#             print(f"Error during video processing: {str(e)}")
#             print("Retrying connection...")
#             time.sleep(2)

#     cv2.destroyAllWindows()

# def main():
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     image_directory = os.path.join(script_dir, "ImagesBasic")
#     print(f"Looking for images in: {image_directory}")
#     video_url = "http://192.168.108.170/cam-hi.jpg"
#     known_faces, face_names = load_known_faces(image_directory)

#     if not known_faces:
#         print("No faces loaded. Exiting...")
#         return

#     print("Starting video stream...")
#     process_video_stream(video_url, known_faces, face_names)

# if __name__ == "__main__":
#     main()


import cv2
import numpy as np
import os
from datetime import datetime
import time
import requests

def load_known_faces(image_directory):
    known_faces = []
    face_names = []
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    if not os.path.exists(image_directory):
        print("Error: Image directory not found.")
        return [], []

    for image_name in os.listdir(image_directory):
        if not image_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue

        image_path = os.path.join(image_directory, image_name)
        print(f"Processing: {image_path}")
        img = cv2.imread(image_path)
        if img is None:
            print(f"Error: Could not load {image_path}")
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        if len(faces) > 0:
            print(f"Found {len(faces)} faces in {image_name}")
            x, y, w, h = faces[0]
            face_roi = gray[y:y+h, x:x+w]
            face_roi = cv2.resize(face_roi, (128, 128))
            known_faces.append(face_roi)
            face_names.append(os.path.splitext(image_name)[0])
            print(f"Successfully processed face from {image_name}")
        else:
            print(f"No faces found in {image_name}")
    return known_faces, face_names

def compare_faces(known_face, current_face, threshold=0.5):
    current_face = cv2.resize(current_face, (known_face.shape[1], known_face.shape[0]))
    result = cv2.matchTemplate(current_face, known_face, cv2.TM_CCOEFF_NORMED)
    max_similarity = np.max(result)
    return max_similarity >= threshold

def mark_attendance(name, attendance_record):
    if name in attendance_record:
        return  

    if not os.path.exists("Attendance.csv"):
        with open("Attendance.csv", "w") as file:
            file.write("Name,Timestamp\n")

    with open("Attendance.csv", "a") as file:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{name},{timestamp}\n")
        attendance_record.add(name)
        print(f"Attendance marked for {name}")

def process_video_stream(video_url, known_faces, face_names):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    attendance_record = set()

    while True:
        try:
            response = requests.get(video_url, timeout=5)
            if response.status_code == 200:
                arr = np.frombuffer(response.content, np.uint8)
                frame = cv2.imdecode(arr, cv2.IMREAD_COLOR)

                if frame is None:
                    print("Error: Could not decode frame.")
                    continue

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.1, 4)

                for (x, y, w, h) in faces:
                    face_roi = gray[y:y + h, x:x + w]
                    face_roi = cv2.resize(face_roi, (128, 128))

                    best_match = "Unknown"
                    for known_face, name in zip(known_faces, face_names):
                        if compare_faces(known_face, face_roi):
                            best_match = name
                            break

                    if best_match != "Unknown":
                        mark_attendance(best_match, attendance_record)

                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(frame, best_match, (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

                cv2.imshow('Face Recognition', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print("Exiting video stream.")
                    break
            else:
                print(f"Error fetching frame: {response.status_code}")
        except Exception as e:
            print(f"Error during video processing: {str(e)}")
            print("Retrying connection...")
            time.sleep(2)

    cv2.destroyAllWindows()

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_directory = os.path.join(script_dir, "ImagesBasic")
    print(f"Looking for images in: {image_directory}")
    video_url = "http://192.168.108.170/cam-hi.jpg"
    known_faces, face_names = load_known_faces(image_directory)

    if not known_faces:
        print("No faces loaded. Exiting...")
        return

    print("Starting video stream...")
    process_video_stream(video_url, known_faces, face_names)

if __name__ == "__main__":
    main()
