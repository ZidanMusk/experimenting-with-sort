"""
@author: Mahmoud I.Zidan
"""

import numpy as np
import os.path
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from skimage import io
import time
import argparse

from sort import Sort
from detector import GroundTruthDetections

def main():
    args = parse_args()
    display = args.display
    use_dlibTracker  = args.use_dlibTracker
    saver = args.saver

    total_time = 0.0
    total_frames = 0

    # for disp
    if display:
        colours = np.random.rand(32, 3)  # used only for display
        plt.ion()
        fig = plt.figure()


    if not os.path.exists('output'):
        os.makedirs('output')
    out_file = 'output/townCentreOut.top'

    #init detector
    detector = GroundTruthDetections()

    #init tracker
    tracker =  Sort(use_dlib= use_dlibTracker) #create instance of the SORT tracker

    if use_dlibTracker:
        print "Dlib Correlation tracker activated!"
    else:
        print "Kalman tracker activated!"

    with open(out_file, 'w') as f_out:

        frames = detector.get_total_frames()
        for frame in range(0, frames):  #frame numbers begin at 0!
            # get detections
            detections = detector.get_detected_items(frame)

            total_frames +=1
            fn = 'test/Pictures%d.jpg' % (frame + 1)  # video frames are extracted to 'test/Pictures%d.jpg' with ffmpeg
            img = io.imread(fn)
            if (display):
                ax1 = fig.add_subplot(111, aspect='equal')
                ax1.imshow(img)
                if(use_dlibTracker):
                    plt.title('Dlib Correlation Tracker')
                else:
                    plt.title('Kalman Tracker')

            start_time = time.time()
            #update tracker
            trackers = tracker.update(detections,img)

            cycle_time = time.time() - start_time
            total_time += cycle_time

            print('frame: %d...took: %3fs'%(frame,cycle_time))

            for d in trackers:
                f_out.write('%d,%d,%d,%d,x,x,x,x,%.3f,%.3f,%.3f,%.3f\n' % (d[4], frame, 1, 1, d[0], d[1], d[2], d[3]))
                if (display):
                    d = d.astype(np.int32)
                    ax1.add_patch(patches.Rectangle((d[0], d[1]), d[2] - d[0], d[3] - d[1], fill=False, lw=3,
                                                    ec=colours[d[4] % 32, :]))
                    ax1.set_adjustable('box-forced')
                    #label
                    ax1.annotate('id = %d' % (d[4]), xy=(d[0], d[1]), xytext=(d[0], d[1]))
                    if detections != []:#detector is active in this frame
                        ax1.annotate(" DETECTOR", xy=(5, 45), xytext=(5, 45))

            if (display):
                plt.axis('off')
                fig.canvas.flush_events()
                plt.draw()
                fig.tight_layout()
                #save the frame with tracking boxes
                if(saver):
                    fig.savefig("./frameOut/f%d.jpg"%(frame+1),dpi = 200)
                ax1.cla()


    print("Total Tracking took: %.3f for %d frames or %.1f FPS"%(total_time,total_frames,total_frames/total_time))

def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='Experimenting Trackers with SORT')
    parser.add_argument('--NoDisplay', dest='display', help='Disables online display of tracker output (slow)',action='store_false')
    parser.add_argument('--dlib', dest='use_dlibTracker', help='Use dlib correlation tracker instead of kalman tracker',action='store_true')
    parser.add_argument('--save', dest='saver', help='Saves frames with tracking output, not used if --NoDisplay',action='store_true')

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    main()