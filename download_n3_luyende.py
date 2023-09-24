import os
import copy
import subprocess

import dotenv

from download_base import DownloadBase
dotenv.load_dotenv()

# de thi JLTP N3 07/2018


class DownloadN3Luyende(DownloadBase):
    def __init__(self, output_folder):
        self.output_folder = output_folder
        self.kanji = {
            "kanji": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/luyendeN3/dethithat/07-2018/N3-Luyende-07-2018-1-Kanji.mp4.hls/1080p/index{index}.ts"
        }
        self.tuvung = {
            "mondai_3": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/luyendeN3/dethithat/07-2018/N3-Luyende-07-2018-2-Tuvung-01.mp4.hls/1080p/index{index}.ts",
            "mondai_4_5": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/luyendeN3/dethithat/07-2018/N3-Luyende-07-2018-2-Tuvung-02.mp4.hls/1080p/index{index}.ts"
        }
        self.nguphap = {
            "mondai_1": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/luyendeN3/dethithat/07-2018/N3-Luyende-07-2018-3-Nguphap-01.mp4.hls/1080p/index{index}.ts",
            "mondai_2_3": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/luyendeN3/dethithat/07-2018/N3-Luyende-07-2018-3-Nguphap-02.mp4.hls/1080p/index{index}.ts"
        }
        self.dochieu = {
            "mondai4_doanvanp1": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/luyendeN3/dethithat/07-2018/N3-Luyende-07-2018-4-Dochieu-01.mp4.hls/1080p/index{index}.ts",
            "mondai4_doanvanp2": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/luyendeN3/dethithat/07-2018/N3-Luyende-07-2018-4-Dochieu-02.mp4.hls/1080p/index{index}.ts",
            "mondai5_trungvanp1": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/luyendeN3/dethithat/07-2018/N3-Luyende-07-2018-4-Dochieu-03.mp4.hls/1080p/index{index}.ts",
            "mondai5_trungvanp2": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/luyendeN3/dethithat/07-2018/N3-Luyende-07-2018-4-Dochieu-04.mp4.hls/1080p/index{index}.ts",
            "mondai6_truongvan": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/luyendeN3/dethithat/07-2018/N3-Luyende-07-2018-4-Dochieu-05.mp4.hls/1080p/index{index}.ts",
            "mondai7_timkiemthongtin": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/luyendeN3/dethithat/07-2018/N3-Luyende-07-2018-4-Dochieu-06.mp4.hls/1080p/index{index}.ts"
        }
        self.nghehieu = {
            "mondai1_p1": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/luyendeN3/dethithat/07-2018/N3-Luyende-07-2018-5-Nghehieu-01.mp4.hls/1080p/index{index}.ts",
            "mondai1_p2": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/luyendeN3/dethithat/07-2018/N3-Luyende-07-2018-5-Nghehieu-02.mp4.hls/1080p/index{index}.ts",
            "mondai2_p1": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/luyendeN3/dethithat/07-2018/N3-Luyende-07-2018-5-Nghehieu-03-fix-20072022.mp4.hls/1080p/index{index}.ts",
            "mondai2_p2": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/luyendeN3/dethithat/07-2018/N3-Luyende-07-2018-5-Nghehieu-04-fix.mp4.hls/1080p/index{index}.ts",
            "mondai3": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/luyendeN3/dethithat/07-2018/N3-Luyende-07-2018-5-Nghehieu-05-fix.mp4.hls/1080p/index{index}.ts",
            "mondai4": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/luyendeN3/dethithat/07-2018/N3-Luyende-07-2018-5-Nghehieu-06.mp4.hls/1080p/index{index}.ts",
            "mondai5": "https://jpcdn.riki.edu.vn/Data/upload/files/Video/luyendeN3/dethithat/07-2018/N3-Luyende-07-2018-5-Nghehieu-07.mp4.hls/1080p/index{index}.ts"
        }
        # ignore index
        super().__init__()

    def start_download(self, config, folder_name):
        print(f"Starting download {folder_name}")
        output_folder = f"{self.output_folder}/{folder_name}"
        if not os.path.exists(output_folder):
            subprocess.run(["mkdir", output_folder])
        for video_name, video_url in config.items():
            print(f"Downloading {video_name}\nURL: {video_url}")
            self._download(video_url, output_folder, video_name)

    def download_all(self):
        self.start_download(self.kanji, "KANJI")
        self.start_download(self.tuvung, "TUVUNG")
        self.start_download(self.nguphap, "NGUPHAP")
        self.start_download(self.dochieu, "DOCHIEU")
        self.start_download(self.nghehieu, "NGHEHIEU")


if __name__ == "__main__":
    output_path = os.getenv("N3_LUYENDE_OUPUT_PATH")
    download_instance = DownloadN3Luyende(output_path)
    download_instance.download_all()
