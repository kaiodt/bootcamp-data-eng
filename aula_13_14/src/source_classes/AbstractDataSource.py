from abc import ABC, abstractmethod


class AbstractDataSource(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_data(self):
        msg = 'Not implemented.'
        raise NotImplementedError(msg)

    @abstractmethod
    def update_full_dataframe(self):
        msg = 'Not implemented.'
        raise NotImplementedError(msg)

    @abstractmethod
    def save_data(self):
        msg = 'Not implemented.'
        raise NotImplementedError(msg)

    @abstractmethod
    def update_data(self):
        msg = 'Not implemented.'
        raise NotImplementedError(msg)
