from injector import Module, provider, singleton

from ioc.options import Options


class OptionsModule(Module):

    @singleton
    @provider
    def provide_options(self) -> Options:
        return Options()
