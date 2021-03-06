# !/usr/bin/env python3
# author: changkun<hi@changkun.us>

chapters = ['00-preface.md', '01-intro.md',  '02-usability.md', '03-runtime.md', '04-containers.md', '05-pointers.md', '06-regex.md', '07-thread.md', '08-filesystem.md', '09-others.md', '10-cpp20.md', 'appendix.md']

ignores = ['TOC', '返回目录', '许可', 'license']

with open('modern-cpp-tutorial.md', 'w') as outfile:
    outfile.write("""---
title: "高速上手 C++11/14/17"
author: 欧长坤 <hi@changkun.us>
copyright: cc-by-nc-nd 4.0
---
""")
    for chapter in chapters:
        with open(chapter) as ch:
            outfile.write('\n')
            for line in ch:
                if any(keyword in line for keyword in ignores):
                    continue
                else:
                    outfile.write(line)