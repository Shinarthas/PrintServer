# coding: utf-8
from __future__ import division, print_function, absolute_import, unicode_literals

import subprocess
import sys
gsprint = r"C:\Program Files\Ghostgum\gsview\gsprint.exe"

# -quertオプションでプリンタ一覧を呼び出す
cmd = '"{}" -query "{}"'.format(gsprint, "file.pdf")

proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = proc.communicate()
exit_code = proc.wait()