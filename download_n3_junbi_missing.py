import os
import copy
import subprocess

import dotenv

from download_base import DownloadBase
dotenv.load_dotenv()

# de thi JLTP N3 07/2018


class DownloadN3JunbiMissing(DownloadBase):
    def __init__(self, output_folder):
        self.output_folder = output_folder
        self.missing_url = {
            "Lesson3-Part1": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/N3Junbi/N3kanjiKaizen/N3-Kanji-Kaizen-3-1-fix.mp4.hls/1080p/index{index}.ts",
            "Lesson3-Part2": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/N3Junbi/N3kanjiKaizen/N3-Kanji-Kaizen-3-2-fix-2.mp4.hls/1080p/index{index}.ts",
            "Lesson3-Part3": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/N3Junbi/N3kanjiKaizen/N3-Kanji-Kaizen-3-3-fix-2.mp4.hls/1080p/index{index}.ts",
            "Lesson4-Part1": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/N3Junbi/N3kanjiKaizen/N3-Kanji-Kaizen-4-1-fix-2.mp4.hls/1080p/index{index}.ts",
            "Lesson4-Part2": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/N3Junbi/N3kanjiKaizen/N3-Kanji-Kaizen-4-2-fix-1.mp4.hls/1080p/index{index}.ts"
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
    output_path = os.getenv("N3_JUNBI_OUPUT_PATH")
    download_instance = DownloadN3JunbiMissing(output_path)
    download_instance.download_all()
