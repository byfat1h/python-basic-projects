#pip install youtube_dl

from __future__ import unicode_literals
import youtube_dl

ydl_options = {}

with youtube_dl.YoutubeDL(ydl_options) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=jLybDqMZsqM'])