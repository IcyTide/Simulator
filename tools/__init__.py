import json
import os
import re

import pandas as pd

BASE_DIR = "../jx3_hd_src"


def read_tab(file):
    file_path = os.path.join(BASE_DIR, file)
    df = pd.read_csv(file_path, sep="\t", low_memory=False, encoding="utf-8", on_bad_lines="skip")
    df = df.where(pd.notna(df), None)
    return df


def read_script(*paths):
    if not paths or not paths[-1]:
        return None
    include_pattern = re.compile(r'Include\("([^"]+)"\)')
    file_path = os.path.join(BASE_DIR, "scripts", *paths)
    with open(file_path, encoding="utf-8") as f:
        content = include_pattern.sub('', f.read())
    return content
