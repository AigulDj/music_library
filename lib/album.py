class Album:
    def __init__(self, id, title, release_year, artist_id):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id

    def __eq__(self, other) -> bool:
        # return self.__dict__ == other.__dict__
        if isinstance(other, Album):
            # Compare two Album instances based on their attributes
            return (
                self.id == other.id and
                self.title == other.title and
                self.release_year == other.release_year and
                self.artist_id == other.artist_id
            )
        return False


    def __repr__(self) -> str:
        return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_id})"