from argparse import ArgumentParser
from xai_components.base import SubGraphExecutor, InArg, OutArg, Component, xai_component, parse_bool
from xai_components.xai_component_library_template.example_components import HelloComponentLibrary

@xai_component(type='xircuits_workflow')
class example(Component):

    def __init__(self, id: str=None):
        super().__init__()
        self.__id__ = id
        self.__start_nodes__ = []
        self.c_0 = HelloComponentLibrary()
        self.c_0.__id__ = '08dc4630-7d62-4230-8ebb-b4907d5d4df7'
        self.c_0.input_str.value = 'new component library!'
        self.c_0.next = None

    def execute(self, ctx):
        for node in self.__start_nodes__:
            if hasattr(node, 'init'):
                node.init(ctx)
        SubGraphExecutor(self.c_0).do(ctx)

def main(args):
    import pprint
    ctx = {}
    ctx['args'] = args
    flow = example()
    flow.next = None
    flow.do(ctx)
if __name__ == '__main__':
    parser = ArgumentParser()
    (args, _) = parser.parse_known_args()
    main(args)
    print('\nFinished Executing')