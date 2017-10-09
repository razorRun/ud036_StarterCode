class Movie():
 
    def __init__(self,title,year,trailerUrl,boxUrl,screenWriter):
        """This class can be used to create instence of movies, consttructor can be called using Movies(title,year,trailerUrl,boxUrl,screenWriter)"""
        self.title=title
        self.year=year
        self.trailer_youtube_url=trailerUrl
        self.poster_image_url=boxUrl
        self.screenWriter=screenWriter
    