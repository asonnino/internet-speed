import cv2
import os
import csv
from datetime import datetime
from dateutil import tz
from matplotlib import pyplot as plt

# --- start config ---

DATA_PATH = '/mnt/storage/speedtest-log/'

TIME_ROW = 3
DOWNLOAD_ROW = 6
UPLOAD_ROW = 7

DELIMITER = ','
TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'
FROM_TIMEZONE = tz.tzutc()
TO_TIMEZONE = tz.tzlocal()

TMP_IMAGE_FOLDER = 'images'
OUTPUT = 'speedtest.avi'
FPS = 1
FIG_DPI = 300

# --- end config ---


def plot(download, upload, file_name, image_folder, title='', dpi=100):
    fig = plt.figure(dpi=dpi)
    fig.suptitle(title)

    hours = range(24)
    plt.plot(hours, download, label='Download speed')
    plt.plot(hours, upload, label='Upload speed')
    plt.legend(loc='upper right', frameon=False)

    plt.ylabel('Network speed (Mbps)')
    plt.xlabel('Hours of the day')

    plt.xlim(0, 23)
    plt.ylim(0, 120)

    plt.savefig(os.path.join(image_folder, file_name + '.png'))
    plt.close(fig)


def make_images(data_folder, image_folder, dpi=FIG_DPI):
    files = [file for file in os.listdir(DATA_PATH) if file.endswith(".csv")]
    files.sort(key=lambda x: datetime.strptime('20' + x[0:-4], '%Y-%m-%d'))

    for index in range(len(files)):
        download = [0] * 24
        upload = [0] * 24

        with open(os.path.join(data_folder, files[index]), 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=DELIMITER)

            for row in csv_reader:
                time = row[TIME_ROW]
                download_speed = row[DOWNLOAD_ROW]
                upload_speed = row[UPLOAD_ROW]

                assert download_speed.replace('.', '', 1).isdigit()
                download_speed = float(download_speed) / 1000000  # Mbps
                assert upload_speed.replace('.', '', 1).isdigit()
                upload_speed = float(upload_speed) / 1000000  # Mbps
                try:
                    utc = datetime.strptime(time, TIME_FORMAT)
                    utc = utc.replace(tzinfo=FROM_TIMEZONE)
                    correct_timezone = utc.astimezone(TO_TIMEZONE)
                    hours = correct_timezone.hour
                except ValueError:
                    assert False

                download[hours] = download_speed
                upload[hours] = upload_speed

        plot(download, upload, str(index), image_folder, title=files[index], dpi=dpi)


def make_video(image_folder, video_name, fps=1):
    # Fetch images
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images.sort(key=lambda x: int(x[0:-4]))
    # Get image shape
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    # Make video
    video = cv2.VideoWriter(video_name, 0, fps, (width,height))

    # Write frames
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    # Export
    cv2.destroyAllWindows()
    video.release()

make_images(DATA_PATH, TMP_IMAGE_FOLDER, dpi=FIG_DPI)
make_video(TMP_IMAGE_FOLDER, OUTPUT, fps=FPS)
