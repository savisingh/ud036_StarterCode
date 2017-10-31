import webbrowser

class Movie():

	# the arguments to the __init__ function initialise the instance variables
	# self is the instance being created i.e. toy_story
    def __init__(self, movie_title, movie_storyline, movie_poster_image, movie_trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image = movie_poster_image
        self.trailer_youtube_url = movie_trailer_youtube
    def show_trailer(self):
    # this method opens the YouTube trailer of the movie, we must import the webbrowser module
        webbrowser.open(self.trailer_youtube_url)
