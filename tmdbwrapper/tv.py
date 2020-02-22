from .import session

class Tv(object):
    def __init__(self, id):
        self.id = id

    def info(self):
        path = f'https://api.themoviedb.org/3/tv/{self.id}'
        response = session.get(path)
        return response.json()

    """
    note that this is a staticmethod, which means it doesn’t need the 
    class to be initialized for it to be used. This is because it 
    doesn’t use any instance variables, and it’s called directly from the class.
    """
    @staticmethod
    def popular():
        path = 'https://api.themoviedb.org/3/tv/popular'
        response = session.get(path)
        return response.json()


    