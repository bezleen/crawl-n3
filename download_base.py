import os
import subprocess

import requests


class DownloadBase(object):
    def __init__(self):
        self.headers = {"Content-Type": "video/mp2t"}
        self.temp_dir = os.getcwd() + "/temp"
        self.file_list_path = f'{self.temp_dir}/file_list.txt'

    def _download(self, url_format: str, output_path: str, save_name: str) -> bool:
        index = 0
        frags_paths = []
        # Clean temporary files
        if os.path.exists(self.temp_dir):
            subprocess.run(["rm", "-rf", f"{self.temp_dir}"])
        subprocess.run(["mkdir", f"{self.temp_dir}"])
        while True:
            crawl_url = url_format.format(index=index)
            print(f"Downloading frag {index}")
            response = requests.get(crawl_url, headers=self.headers)
            if response.status_code != 200:
                if index == 0:
                    return False
                # concat results
                with open(f'{self.file_list_path}', 'w') as f:
                    for frag_path in frags_paths:
                        f.write(f"file '{frag_path}'\n")
                # Use ffmpeg to concatenate the videos
                print("Combining fragments...")
                subprocess.run(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', f'{self.file_list_path}', '-c', 'copy', f'{output_path}/{save_name}.mp4'])
                return True
            video_path = self.temp_dir + f"/index{index}.mp2t"
            frags_paths.append(video_path)
            with open(video_path, "wb") as f:
                f.write(response.content)
            # after crawl
            index += 1
