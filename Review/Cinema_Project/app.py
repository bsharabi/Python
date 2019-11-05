import room
import movie
import cinema


print("-------------------------------------------------------------------------")
my_cinema=cinema.Cinema()

movie1=movie.Movie("Avatar",35)
movie2=movie.Movie("Alice",12)

room1=room.Room(movie1)
room2=room.Room(movie2)

my_cinema.Insert_Room(room1)
my_cinema.Insert_Room(room2)


my_cinema.order_seats(4,"Avatar")
my_cinema.order_seats(6,"Alice")

print(my_cinema.GetInfo())