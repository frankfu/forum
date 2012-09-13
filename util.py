# -*- coding: utf-8 -*-
import web
import markdown

def humanize_bytes(bytes):
    bytes = float(bytes)
    if bytes >= 1073741824:
        gigabytes = bytes / 1073741824
        size = '%.2fGB' % gigabytes
    elif bytes >= 1048576:
        megabytes = bytes / 1048576
        size = '%.2fMB' % megabytes
    elif bytes >= 1024:
        kilobytes = bytes / 1024
        size = '%.2fKB' % kilobytes
    else:
        size = '%dB' % bytes
    return size

def make_html(c):
    return markdown.markdown(c)
