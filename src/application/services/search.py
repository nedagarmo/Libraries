from iservice import IService


class SearchBook(IService):

    def do(self, **kwargs):
        """
        Busca un libro que coincida con los parámetros de búsqueda
        :param kwargs: campos por el que se filtrarán los datos
        :return: lista de objetos que coincidan con el criterio de búsqueda
        """
        return []
