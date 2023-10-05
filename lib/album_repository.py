from lib.album import Album

class AlbumRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM albums')
        
        return [
            Album(row["title"], row["release_year"], row["artist_id"])
            for row in rows
            ]


