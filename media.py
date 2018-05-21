#!/usr/bin/env python
import webbrowser


class Movie():
    def __init__(self, movie_title, movie_story, poster_image, trailer_youtbe):
        self.m_title = movie_title
        self.story = movie_story
        self.banner = poster_image
        self.trailer_link = trailer_youtbe

    def show_trailer(self):
        webbrowser.open(self.trailer_link)
