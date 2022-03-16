import enum
import sys
from typing import Literal
import cv2

from pathlib import Path
from matplotlib import pyplot as plt

class FrameType(enum.Enum):
    CUT = 1
    FADE = 2

def main():
    video_path = Path(__file__).parent / './assets/ski_cross.mp4'

    capture = cv2.VideoCapture(str(video_path))

    if not capture.isOpened():
        print('Error: cannot open video file')
        sys.exit(1)

    current_frame = last_frame = None

    frames = []

    while True:
        last_frame = current_frame

        ret, frame = capture.read()

        current_frame = frame

        if not ret:
            break
        
        width = current_frame.shape[0]
        height = current_frame.shape[1]

        cv2.imshow('frame', current_frame)
        frame_number = capture.get(cv2.CAP_PROP_POS_FRAMES)

        comps = []
        if last_frame is not None:
            for x in range(0, width, width // 2):
                for y in range(0, height, height // 2):
                    x1 = x + width // 2
                    y1 = y + height // 2
                    current_scope = current_frame[x:x1, y:y1]
                    last_scope = last_frame[x:x1, y:y1]

                    current_hist = cv2.calcHist([current_scope], [0], None, [256], [0, 256])
                    current_hist = cv2.normalize(current_hist, current_hist).flatten()


                    last_hist = cv2.calcHist([last_scope], [0], None, [256], [0, 256])
                    last_hist = cv2.normalize(last_hist, last_hist).flatten()

                    comp = cv2.compareHist(current_hist, last_hist, cv2.HISTCMP_BHATTACHARYYA)

                    comps.append(comp)
            
            average = float(sum(comps)) / float(len(comps))

            if average > 0.3:
                if not frames:
                    frames.append({ 'frame': frame_number, 'type': FrameType.CUT })
                else:
                    if abs(frame_number - frames[-1]['frame']) > 10:
                        frames.append({ 'frame': frame_number, 'type': FrameType.CUT })
                    else:
                        frames[-1]['type'] = FrameType.FADE
                        frames.append({ 'frame': frame_number, 'type': FrameType.FADE })
            
            comps = []

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    capture.release()

    cv2.destroyAllWindows()

    for frame in frames:
        print(f'Frame : {frame["frame"]} - Type: {frame["type"]}')

if __name__ == '__main__':
    main()
