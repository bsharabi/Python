import movie
import cinema
import room


Mymovie1=movie.Movie("Avatar", 15)
Mymovie2=movie.Movie("Alice", 35)


Myroom1=room.Room(Mymovie1)
Myroom2=room.Room(Mymovie2)

Mycinema=cinema.Cinema()

Mycinema.add_room(Myroom1)
Mycinema.add_room(Myroom2)


Mycinema.add_movie(Mymovie1)
Mycinema.add_movie(Mymovie2)

Mycinema.order_seats(2,"Avatar")
Mycinema.order_seats(5,"Alice")

print(Mycinema.get_info())

Mycinema.order_seats(8,"Avatar")
Mycinema.order_seats(5,"Alice")

print(Mycinema.get_info())