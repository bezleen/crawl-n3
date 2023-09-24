import os
import copy
import subprocess

import dotenv

from download_base import DownloadBase
dotenv.load_dotenv()


class DownloadN3Taisaku(DownloadBase):
    def __init__(self, output_folder):
        self.output_folder = output_folder
        self.skeleton_video_url = 'https://jpcdn.riki.edu.vn/Data/upload/files/Video/N3taisaku/nguphapMonss/N3TSK-nguphap-{lesson}-{part}{fix}.mp4.hls/1080p'
        self.tail_url = '/index{index}.ts'
        # 20 lessons
        self.lessons = list(range(1, 21))
        # each lesson has 2 to 4 parts
        self.parts = list(range(1, 5))
        # fix_num should try from -3 -2 -1 to ""
        self.fixes = ["-fix-3", "-fix-2", "-fix-1", "-fix", ""]
        # ignore index
        super().__init__()

    def init_lesson_folder(self):
        for lesson in self.lessons:
            output_folder = f"{self.output_folder}/Lesson{lesson}"
            if os.path.exists(output_folder):
                continue
            subprocess.run(["mkdir", output_folder])

    def start_download(self):
        self.init_lesson_folder()
        for lesson in self.lessons:
            output_folder = f"{self.output_folder}/Lesson{lesson}"
            for part in self.parts:
                for fix in self.fixes:
                    video_url = copy.deepcopy(self.skeleton_video_url)
                    video_url = video_url.format(lesson=lesson, part=part, fix=fix)
                    video_url += self.tail_url
                    print(video_url)
                    video_name = f"Lesson{lesson}-Part{part}"
                    result = self._download(video_url, output_folder, video_name)
                    # try any fix num and break when there is at least one success
                    if result:
                        print(f"Successfully downloaded {video_name}")
                        break
        return


if __name__ == "__main__":
    output_path = os.getenv("N3_TAISAKU_OUPUT_PATH")
    download_instance = DownloadN3Taisaku(output_path)
    download_instance.start_download()
