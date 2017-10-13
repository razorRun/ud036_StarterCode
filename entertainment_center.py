import media
import fresh_tomatoes
# will create content to display in the site 
movies = []
movies.append(media.Movie("Jack Reacher", "2016", 
"https://www.youtube.com/watch?v=aRwrdbcAh2s",
"http://images.primewire.ag/thumbs/2784228_Jack_Reacher_Never_Go_Back_2016.jpg",  # NOQA
"Edward Zwick"))
movies.append(media.Movie("Friend Request", "2016", 
"https://www.youtube.com/watch?v=nDNgs0dgjj4", 
"https://upload.wikimedia.org/wikipedia/en/a/ab/Friend_Request_Poster.jpg",  # NOQA
"Simon Verhoeven"))
movies.append(media.Movie("Masterminds", "2016", 
"https://www.youtube.com/watch?v=lFQP73G5yRg", 
"http://images.primewire.ag/thumbs/2784243_Masterminds_2016.jpg",  # NOQA
"Jared Hess"))
movies.append(media.Movie("The BFG", "2016", 
"https://www.youtube.com/watch?v=GZ0Bey4YUGI", 
"http://images.primewire.ag/thumbs/2779353_The_BFG_2016.jpg",  # NOQA
"	Steven Spielberg"))
movies.append(media.Movie("Finding Dory", "2016", 
"https://www.youtube.com/watch?v=oP0WR2Ql9yI", 
"http://images.primewire.ag/thumbs/2778720_Finding_Dory_2016.jpg",  # NOQA
"Andrew Stanton"))
movies.append(media.Movie("Snowden", "2016", 
"https://www.youtube.com/watch?v=QlSAiI3xMh4", 
"http://images.primewire.ag/thumbs/2784192_Snowden_2016.jpg",  # NOQA
"Oliver Stone"))

# will create the website 
fresh_tomatoes.open_movies_page(movies)
