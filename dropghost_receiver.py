#Coded by Mulvun
#!/usr/bin/env python3
import glob
import hashlib
import os
import subprocess
import time
from signal import signal, SIGINT

from Imports import AutoPhish, Pretty

try:
    from dev_settings import *
except:
    from settings import *


class Dropper(AutoPhish.DropBear, Pretty.Logo):
    def __init__(self):
        super().__init__(email_from, email_to, password_from, password_to, host_server)
        self.file_list = glob.glob("./attachments/*")
        self.animation = Pretty.Animation()
        for f in self.file_list:
            os.remove(f)
        signal(SIGINT, self.catch)

    def catch(self, signal_received, frame):
        self.animation.done('SIGINT or CTRL-C detected. Exited gracefully')
        exit()

    @Pretty.Logo.wrap
    def run(self):
        already_run_malware_hashes = []
        try:
            try:
                os.mkdir('./attachments')
            except:
                pass
            while 1:
                Pretty.clear_console()
                self.animation.start("Master Script Starting")
                self.animation.done()
                self.animation.start("Downloading Emails")
                self.receive_mail()
                self.animation.done()
                self.animation.start("Emails Downloaded")
                self.animation.done()
                executables = glob.glob("./attachments/*.exe")
                malwareHashes = []
                self.animation.start("Finding Duplicate Malware")
                self.animation.done()
                for malware in executables:
                    malwareHashes.append(self.md5(malware))

                index_of_old_malware = [
                    i
                    for i, item in enumerate(already_run_malware_hashes)
                    if item in set(malwareHashes)
                ]
                if len(index_of_old_malware) == 0:
                    for malware in executables:
                        self.animation.start(f"Spawning {malware} {self.md5(malware)}")
                        self.animation.done()
                        subprocess.call(malware, shell=True)
                        already_run_malware_hashes.append(self.md5(malware))

                else:
                    if len(index_of_old_malware) == len(executables):
                        self.animation.start("No New Malware :(")
                        self.animation.done()
                        pass
                    else:
                        # new shit!
                        new_malware = []
                        self.animation.start(str(index_of_old_malware))
                        self.animation.done()
                        index_of_new_malware = range(len(executables))
                        self.animation.start(str(index_of_new_malware))
                        self.animation.done()
                        for items in index_of_old_malware:
                            del index_of_new_malware[items]
                        for idx in range(len(index_of_new_malware)):
                            new_malware.append(executables[idx])
                        for malware in new_malware:
                            subprocess.call(new_malware, shell=True)
                            already_run_malware_hashes.append(self.md5(malware))

                self.animation.start("Deleting Emails")
                self.animation.done()
                self.delete_emails()
                self.animation.start("Waiting 15 seconds")
                time.sleep(15)
                self.animation.done()
        except Exception as e:
            self.animation.error(str(e))

    @staticmethod
    def diff(li1, li2):
        return list(set(li1) - set(li2))

    @staticmethod
    def md5(fname):
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(2 ** 20), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()


if __name__ == '__main__':
    d = Dropper()
    d.run()