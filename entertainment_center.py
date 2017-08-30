import media
import fresh_tomatoes

curious_george_2 = media.Movie("Curious George 2: Follow That Monkey!",
                    "George helps his elephant friend visit her family",
                    "https://images-na.ssl-images-amazon.com/images/I/51AQabHJk9L._SY355_.jpg",
                    "https://www.youtube.com/watch?v=nM2SHNJqtYU")

tombstone = media.Movie("Tombstone",
                        "Wyatt Earp takes on the cowboys in the Wild West",
                        "https://resizing.flixster.com/0C0RlHXzsCH6vcJXOuhUzD6ULzk=/206x305/v1.bTsxMTIwODU0MjtqOzE3NDk5OzEyMDA7MTk1MDsyNjAw",
                        "https://www.youtube.com/watch?v=QPTVLKKgGXw")
                        

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")
#avatar.show_trailer(

movies = [curious_george_2, tombstone, toy_story, avatar]
#print(media.Movie.tombstone)
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.__doc__)

