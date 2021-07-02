#exe_6
#1.  don`t understand

#2.
def favorite_book(title):
    return f"«One of my favorite books is {title}»"

print(favorite_book("Alice in Wonderland"))

#3,4
def make_shirt(shirt_size = "L", shirt_text = "I love Python"):
    print("Size of shirt is " + str(shirt_size) + " and Text on the shirt is the following: " + shirt_text)
 
# размер футболки,текст футболки
make_shirt(42, "Footballer shirt")
make_shirt(shirt_size = 42, shirt_text = "Footballer shirt")
make_shirt()

#7
def make_album(artist_name, album_name,line_cnt = ''):
    artist_album = {'artist' : artist_name,'album' : album_name}
    if line_cnt:
        artist_album['lines'] = line_cnt
    return artist_album

album1 = make_album('B.B.King','Thrill Is Gone')
print(album1)
album2 = make_album('Beth Hart','Blues','150')
print(album2)