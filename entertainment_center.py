#!/usr/bin/env python
import media
import movies

# It is the starting point of  project
# It import media module which contains movie class
# and initialize the movie with name Trailer_link etc.
# Then generates list of movies and pass them to open_movies_page
# function which will create page with movies and opens it in browser

ban = media.Movie(
    "Bharat Ane Nenu", "political",
    "https://bit.ly/2rZb44y",
    "KMWS5y2gZ6E")
aiw = media.Movie(
    "Avengers Infinity War",
    "Fiction",
    "https://cdn.movieweb.com/img.news/NE57z54J8o2t7a_1_1.jpg",
    "QwievZ1Tx-8")
ky = media.Movie(
    "Krishnarjuna Yuddham", "Love",
    "https://bit.ly/2GBBtur",
    "JwB_qfwFXZY")
rslm = media.Movie(
    "Rangastalam", "1980's",
    "https://bit.ly/2IAsUpJ",
    "sueMmTm-M4Y")
kn = media.Movie(
    "Kanam",
    "Horor",
    "https://bit.ly/2s0e5BF",
    "TSblrnXKfkE")

all_movies = [ban, aiw, ky, rslm, kn]

movies.open_movies_page(all_movies)
