import os
import copy
import subprocess

import dotenv

from download_base import DownloadBase
dotenv.load_dotenv()

# de thi JLTP N3 07/2018


class DownloadN3TaisakuMissing(DownloadBase):
    def __init__(self, output_folder):
        self.output_folder = output_folder
        self.missing_url = {
            "Lesson15-Part3": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/N3taisaku/nguphapMonss/NGUPHAP-BAI14-PHAN3-DONE-fix.mp4.hls/1080p/index{index}.ts",
            "Lesson16-Part3": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/N3taisaku/nguphapMonss/NGUPHAP-BAI15-PHAN3-fix-khongxemduoc.mp4.hls/1080p/index{index}.ts",
            "Lesson11-Part1": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/N3taisaku/nguphapMonss/NGUPHAP-BAI11-PHAN1-DONE.mp4.hls/1080p/index{index}.ts",
            "Lesson8-Part2": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/N3taisaku/nguphapMonss/NGUPHAP-BAI8-PHAN2-DONE.mp4.hls/1080p/index{index}.ts",
            "Lesson7-Part1": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/N3taisaku/nguphapMonss/N3-taisaku-nguphap-bai7-1.mp4.hls/720p/index{index}.ts",
            "Lesson7-Part2": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/N3taisaku/nguphapMonss/NGUPHAP-BAI7-PHAN2-DONE.mp4.hls/1080p/index{index}.ts",
            "Lesson6-Part2": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/N3taisaku/nguphapMonss/N3-taisaku-Bai6-2.mp4.hls/1080p/index{index}.ts",
            "Lesson5-Part1": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/N3taisaku/nguphapMonss/N3-Nguphap-TSK-5-1.mp4.hls/1080p/index{index}.ts",
            "Lesson4-Part2": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/N3taisaku/nguphapMonss/N3TSK-nguphap-4-2-1.ts.hls/1080p/index{index}.ts",
            "Lesson4-Part3": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/N3taisaku/nguphapMonss/N3TSK-nguphap-4-2-2.ts.hls/1080p/index{index}.ts",
            "Lesson3-Part1": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/N3taisaku/nguphapMonss/NGUPHAP-BAI3-PHAN1-DONE.mp4.hls/1080p/index{index}.ts",
            "Lesson2-Part3": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/N3taisaku/nguphapMonss/N3-taisaku-mon-nguphap-bai2-P3.mp4.hls/1080p/index{index}.ts"
        }

        # ignore index
        super().__init__()

    def start_download(self, video_name, video_url, folder_name):
        print(f"Starting download {folder_name}")
        output_folder = f"{self.output_folder}/{folder_name}"
        if not os.path.exists(output_folder):
            subprocess.run(["mkdir", output_folder])
        print(f"Downloading {video_name}\nURL: {video_url}")
        self._download(video_url, output_folder, video_name)

    def download_all(self):
        for video_name, video_url in self.missing_url.items():
            folder_name = video_name.split("-")[0]
            self.start_download(video_name, video_url, folder_name)


if __name__ == "__main__":
    output_path = os.getenv("N3_TAISAKU_OUPUT_PATH")
    download_instance = DownloadN3TaisakuMissing(output_path)
    download_instance.download_all()
