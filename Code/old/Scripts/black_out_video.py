import cv2
import numpy as np
import os

#os.chdir("../")
os.chdir("/mnt/sda1/shivam/Thesis/Grasp Experiment/Data/Videos/to osf")

blur_video_names = [
    "FP01.mkv",
    "FP02.mkv",
    "FP03.mkv",
    "FP05.mkv",
    "FP06.mkv",
    "FP07.mkv",
    "FP08.mkv",
    "FP09.mkv",
    "FP10.mkv",
    "FP11.mkv",
    "FP12.mkv",
    "FP13.mkv",
]

for file in blur_video_names:
    print(file)
    video_path = file
    output_path = file[:-4] + "--blacked.mkv"

    cap = cv2.VideoCapture(video_path)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    roi_start_x = 0
    roi_start_y = 0
    roi_end_x = 300
    roi_end_y = 300

    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        mask = np.zeros_like(frame)
        mask[roi_start_y:roi_end_y, roi_start_x:roi_end_x, :] = 255
        frame = np.where(mask == 255, 0, frame)

        out.write(frame)

        # cv2.imshow("Modified Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
