import sys
import cv2
import statistics

import numpy as np
import matplotlib.pyplot as plt

from enum import Enum

from typing import Dict, List, TypedDict
from pathlib import Path

class FrameType(Enum):
    CUT = 0
    FADE = 1

class Frame(TypedDict):
    frame: int
    type: FrameType

# sect1 = []
# sect2 = []


def main():
    video_path = Path(__file__).parent / './assets/ski_cross.mp4'

    capture = cv2.VideoCapture(str(video_path))

    if not capture.isOpened():
        print('Error: cannot open video file')
        sys.exit(1)

    current_frame: np.ndarray = None
    last_frame: np.ndarray = None

    result: List[List[int]] = []
    frames: List[Frame] = []

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

        
        histogram_comparisons = []

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

                    comparison = cv2.compareHist(current_hist, last_hist, cv2.HISTCMP_BHATTACHARYYA)

                    histogram_comparisons.append(comparison)
            
            average = statistics.mean(histogram_comparisons)

            if average > 0.3:
                if not result:
                    frame = Frame(frame=frame_number, type=FrameType.CUT)
                    frames.append(frame)
                    result.append([frame_number])
                else:
                    if abs(frame_number - frames[-1]['frame']) > 10:
                        result.append([frame_number])
                        frame = Frame(frame=frame_number, type=FrameType.CUT)
                        frames.append(frame)
                    else:
                        result[-1].append(frame_number)
                        frames[-1]['type'] = FrameType.FADE
                        frame = Frame(frame=frame_number, type=FrameType.FADE)
                        frames.append(frame)
            
            histogram_comparisons.clear()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    capture.release()

    cv2.destroyAllWindows()

    for frame in result:
        if len(frame) > 1:
            print(f"Fondu: {min(frame)} - {max(frame)}")
        else:
            print(f"Coupure: {frame[0]}")

    # Code utilisé pour générer des histogrammes.
    # kwargs = dict(histtype='stepfilled', alpha=0.3, density=True, bins=50)

    # plt.hist(sect1[0], color='#e28743', **kwargs)
    # plt.hist(sect2[0], color='#154c79', **kwargs)

    # plt.show()

    # plt.hist(sect1[1], color='#e28743', **kwargs)
    # plt.hist(sect2[1], color='#154c79', **kwargs)

    # plt.show()

    # plt.hist(sect1[2], color='#e28743', **kwargs)
    # plt.hist(sect2[2], color='#154c79', **kwargs)

    # plt.show()

    # plt.hist(sect1[3], color='#e28743', **kwargs)
    # plt.hist(sect2[3], color='#154c79', **kwargs)

    # plt.show()

if __name__ == '__main__':
    main()
