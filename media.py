#!/usr/bin/env python
'''
This module contains the information
regarding the movie and some functions
'''

import webbrowser


class Movie():
    '''
    It Stores all properties related to the movie
    '''
    def __init__(self,
                 movie_title,
                 movie_story,
                 poster_image,
                 trailer_youtbe):
        '''
        Initilize the with its data/properties

        :params movie_title: string
        :params movie_story: string
        :params poster_image: string image url
        :params trailer_youtbe: string  youtube url
        '''
        self.m_title = movie_title
        self.story = movie_story
        self.banner = poster_image
        self.trailer_link = trailer_youtbe

    def show_trailer(self):
        '''
        It open the trailer in webbrowser
        when you call the function on object (ex:movie.show_trailer())
        '''
        webbrowser.open(self.trailer_link)
