from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When we call AlbumRepository#all
We get a list of Album objects reflecting the seed data.
"""
def test_get_all_album_records(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repo = AlbumRepository(db_connection)

    album = repo.all()

    assert album == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2)
    ]
    

"""
When we call #find with an id
We get the record with that id
"""
def test_get_the_record_with_given_id(db_connection):
    db_connection.seed("seeds/music_library.sql")
    album_repo = AlbumRepository(db_connection)
    album = album_repo.find(2)
    assert album == Album(2, 'Surfer Rosa', 1988, 1)

"""
When we call #create
We get a new record in the database
"""
def test_create_new_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    album_repo = AlbumRepository(db_connection)
    album = Album(None, "New Album Title", 2023, 1)
    album_repo.create(album)
    result = album_repo.all()

    assert result == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2),
        Album(13, "New Album Title", 2023, 1)
    ]

"""
When we call #delete
We remove a record from the database
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    album_repo = AlbumRepository(db_connection)
    album_repo.delete(2)
    result = album_repo.all()

    assert result == [
        Album(1, 'Doolittle', 1989, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2),
    ]
