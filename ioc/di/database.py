from injector import Module, provider, singleton

from database.facade import DatabaseFacade
from ioc.options import Options


class DatabaseModule(Module):

    @singleton
    @provider
    def provide_database_facade(self, options: Options) -> DatabaseFacade:
        return DatabaseFacade(options)
