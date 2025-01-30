from injector import Module, provider, singleton

from database.facade import DatabaseFacade

class DatabaseModule(Module):

    @singleton
    @provider
    def provide_database_facade(self) -> DatabaseFacade:
        return DatabaseFacade()
