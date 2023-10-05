from lib.album import Album

"""
Album constracts with a title, release_year, artist_id
"""
def test_album_constructs():
    album = Album("Test Title", 1988, 1)
    assert album.title == "Test Title"
    assert album.release_year ==  1988
    assert album.artist_id == 1

"""
Compare two identical albums
And have them be equal
"""
def test_albums_are_equal():
    album1 = Album("Test Title", 1999, 1)
    album2 = Album("Test Title", 1999, 1)
    assert album1 == album2

"""
Format albums objects to strings
"""
def test_album_format_to_strings():
    album = Album("Test Title", 1978, 1)
    assert str(album) == "Album(Test Title, 1978, 1)"
