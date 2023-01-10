albums = [("Welcome To My Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilia May", 2011),
          ("Ride The Lightning", "Metallica", 1984),
          ]

print(len(albums))

for (name, artist, year) in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

for album in albums:
    name, artist, year = album
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))
