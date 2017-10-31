import project_media # import project_media.py with class Movie() defined
import fresh_tomatoes

# created multiple instances below

toy_story = project_media.Movie("Toy Story", "Toys that come to life",
                                "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                                "https://www.youtube.com/watch?v=vwyZH85NQC4")

fellowship_of_the_rings = project_media.Movie("Lord of the Rings: The Fellowship of the Ring",
                                              "Frodo must take the ring to Mordor",
                                              "https://i.ytimg.com/vi/4LhkXX9r6kY/maxresdefault.jpg",
                                              "https://www.youtube.com/watch?v=V75dMMIW2B4")

the_notebook = project_media.Movie("The Notebook", "Love story between different classes",
                                   "https://hips.hearstapps.com/sev.h-cdn.co/assets/15/31/1438124471-the-notebook-2004-copy.jpg", 
                                   "https://www.youtube.com/watch?v=4M7LIcH8C9U")

super_bad = project_media.Movie("Super Bad", "Comedy about highschool kids",
                                "https://static1.squarespace.com/static/56f2f43b20c64775298d66aa/t/57bcab76414fb51a85d1e226/1471982465255/",
                                "https://www.youtube.com/watch?v=zFjaJbihWwc")

fight_club = project_media.Movie("Fight Club", "Rule One: Don't talk about fight club",
                                 "https://resizing.flixster.com/XugIZHeXNKH7FmC4qsqD319_Ke4=/206x305/v1.bTsxMTM3MjQ0ODtqOzE3NTQ2OzEyMDA7MTE5MTsxNTg4",
                                 "https://www.youtube.com/watch?v=SUXWAEX2jlg")

moana = project_media.Movie("Moana", "Get the heart of Tafiti",
                            "https://images-na.ssl-images-amazon.com/images/I/61geeb4TJ4L._SX342_.jpg",
                            "https://www.youtube.com/watch?v=LKFuXETZUsI")

harry_potter_one = project_media.Movie("Harry Potter and the Philosopher's Stone", "Harry is a wizard",
                                       "https://upload.wikimedia.org/wikipedia/en/c/c0/Harry_Potter_and_the_Philosopher%27s_Stone_posters.JPG", 
                                       "https://www.youtube.com/watch?v=VyHV0BRtdxo")

white_chicks = project_media.Movie("White Chicks", "Cops undercover in the Hamptons",
                                   "https://occ-0-114-116.1.nflxso.net/art/fced8/"
                                   "5335793f019f2a4125f8dde156d1bc3708efced8.jpg",
                                   "https://www.youtube.com/watch?v=aeVkbNka9HM")

parent_trap = project_media.Movie("The Parent Trap", "Twins try to reunit their parents",
                                  "http://www.filmaps.com/nposters/xn-246701548-300412063108.jpg.pagespeed.ic.z9pcVfAUOB.jpg", 
                                  "https://www.youtube.com/watch?v=32WeiH4TrIY")

love_actually = project_media.Movie("Love Actually", "Intertwining stories at Christmas",
                                    "https://www.uphe.com/sites/default/files/2015/04/Love-Actually-Gallery-2.jpg", 
                                    "https://www.youtube.com/watch?v=fOS-HMiVejo")

home_alone = project_media.Movie("Home Alone", "Kevin McAllistar left home alone at Christmas",
                                 "http://hotcountry1035.com/wp-content/uploads/2016/12/HomeAloneThumb.jpg",
                                 "https://www.youtube.com/watch?v=CK2Btk6Ybm0")

sing = project_media.Movie("Sing", "Singing competition",
                           "http://cdn1-www.comingsoon.net/assets/uploads/2016/02/singheader.jpg",
                           "https://www.youtube.com/watch?v=Y7uGHY-t80I")

kill_bill = project_media.Movie("Kill Bill", "Tarantino hit film about revenge",
                                "https://i.ytimg.com/vi/ot6C1ZKyiME/maxresdefault.jpg",
                                "https://www.youtube.com/watch?v=7kSuas6mRpk")

school_of_rock =  project_media.Movie("School of Rock", "Storyline",
                                     "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                                     "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = project_media.Movie("Ratatouille", "Storyline",
                                  "http://images4.fanpop.com/image/photos/22600000/rataouille-movie-cover-ratatouille-22648203-366-500.jpg",  
                                  "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = project_media.Movie("Midnight in Paris", "Storyline",
                                        "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg", 
                                        "https://www.youtube.com/watch?v=atLg2wQQxvU")

hunger_games = project_media.Movie("Hunger Games", "Storyline",
                                   "https://reelisticviewsdotcom.files.wordpress.com/2016/10/the-hunger-games-1.jpg",
                                   "https://www.youtube.com/watch?v=PbA63a7H0bo")

# movies below is a list of movie instances. This will be the input into the open_movies_page() function in fresh_tomatoes.py
movies = [toy_story, fellowship_of_the_rings, the_notebook, super_bad, fight_club, moana, harry_potter_one, white_chicks, parent_trap,
          love_actually, home_alone, sing, kill_bill, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
