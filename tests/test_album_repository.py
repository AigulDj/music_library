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
        Album('Doolittle', 1989, 1),
        Album('Surfer Rosa', 1988, 1),
        Album('Waterloo', 1974, 2),
        Album('Super Trouper', 1980, 2),
        Album('Bossanova', 1990, 1),
        Album('Lover', 2019, 3),
        Album('Folklore', 2020, 3),
        Album('I Put a Spell on You', 1965, 4),
        Album('Baltimore', 1978, 4),
        Album('Here Comes the Sun', 1971, 4),
        Album('Fodder on My Wings', 1982, 4),
        Album('Ring Ring', 1973, 2)
    ]