from argparse import ArgumentParser
from xai_components.base import SubGraphExecutor, InArg, OutArg, Component, xai_component, parse_bool
from xai_components.xai_utils.utils import Print
from xai_components.xai_xircuitphant.general import GenerateArray
from xai_components.xai_xircuitphant.statistics import MeanFiringRate

@xai_component(type='xircuits_workflow')
class example(Component):

    def __init__(self, id: str=None):
        super().__init__()
        self.__id__ = id
        self.__start_nodes__ = []
        self.c_0 = GenerateArray()
        self.c_0.__id__ = 'be657a7e-cd69-4006-9942-045e1847031d'
        self.c_1 = Print()
        self.c_1.__id__ = 'd81cf8d1-c5f8-4753-8725-33c6bcedcced'
        self.c_2 = MeanFiringRate()
        self.c_2.__id__ = '3853b989-04e1-4d68-b908-8c5a48ea14df'
        self.c_0._list.value = [1, 2, 3, 4, 5]
        self.c_1.msg.connect(self.c_2.firing_rate)
        self.c_2.spiketrain.connect(self.c_0.array)
        self.c_0.next = self.c_2
        self.c_1.next = None
        self.c_2.next = self.c_1

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