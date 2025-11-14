from argparse import ArgumentParser
from xai_components.base import SubGraphExecutor, InArg, OutArg, Component, xai_component, parse_bool
from xai_components.xai_utils.utils import Print
from xai_components.xai_xircuitphant.general import GenerateSpikeTrain, GenerateQuantityFromFloat, GenerateArray, GenerateQuantityFromArray, GenerateSpikeTrains
from xai_components.xai_xircuitphant.statistics import ComplexityPdf, ComplexityInit, MeanFiringRate

@xai_component(type='xircuits_workflow')
class example(Component):

    def __init__(self, id: str=None):
        super().__init__()
        self.__id__ = id
        self.__start_nodes__ = []
        self.c_0 = GenerateQuantityFromFloat()
        self.c_0.__id__ = '2268e4ec-d057-4550-94aa-59ab587ac993'
        self.c_1 = Print()
        self.c_1.__id__ = 'd81cf8d1-c5f8-4753-8725-33c6bcedcced'
        self.c_2 = MeanFiringRate()
        self.c_2.__id__ = '3853b989-04e1-4d68-b908-8c5a48ea14df'
        self.c_3 = GenerateQuantityFromArray()
        self.c_3.__id__ = '319e7847-965a-46bb-b608-7f79b9ece402'
        self.c_4 = GenerateArray()
        self.c_4.__id__ = 'be657a7e-cd69-4006-9942-045e1847031d'
        self.c_5 = GenerateSpikeTrain()
        self.c_5.__id__ = '0941c433-ed7b-4981-b586-51f7efe5945d'
        self.c_6 = GenerateSpikeTrains()
        self.c_6.__id__ = 'adf18444-b2fc-43b9-a4ae-baba2f7f03a0'
        self.c_7 = ComplexityInit()
        self.c_7.__id__ = '65d5464c-2b0e-4db7-8945-27a6ecf1537e'
        self.c_8 = ComplexityPdf()
        self.c_8.__id__ = '38188162-9d0a-42fb-81f3-1d05b52200d1'
        self.c_9 = Print()
        self.c_9.__id__ = '5eccf799-0022-48a3-b978-5e93d345f2fe'
        self.c_10 = ComplexityPdf()
        self.c_10.__id__ = '41fe5bda-df34-4230-ac58-fb6230d9d740'
        self.c_11 = GenerateSpikeTrain()
        self.c_11.__id__ = 'efc01373-6bd4-4041-bab3-5822fdb0ce17'
        self.c_12 = GenerateQuantityFromFloat()
        self.c_12.__id__ = '4ffb9998-c807-43d1-9399-9681d31e7317'
        self.c_0._float.value = 0
        self.c_1.msg.connect(self.c_2.firing_rate)
        self.c_2.spiketrain.connect(self.c_4.array)
        self.c_3.array.connect(self.c_4.array)
        self.c_4._list.value = [1, 2, 3, 4, 5]
        self.c_5.data.connect(self.c_3.quantity)
        self.c_5.t_start.connect(self.c_0.quantity)
        self.c_5.t_stop.connect(self.c_12.quantity)
        self.c_6.spiketrain_i.connect(self.c_11.spiketrain)
        self.c_6.spiketrain_j.connect(self.c_5.spiketrain)
        self.c_7.spiketrains.connect(self.c_6.spiketrains)
        self.c_8.complexity.connect(self.c_7.complexity)
        self.c_9.msg.connect(self.c_10.pdf)
        self.c_10.complexity.connect(self.c_7.complexity)
        self.c_11.data.connect(self.c_3.quantity)
        self.c_11.t_start.connect(self.c_0.quantity)
        self.c_11.t_stop.connect(self.c_12.quantity)
        self.c_12._float.value = 6
        self.c_0.next = self.c_12
        self.c_1.next = self.c_3
        self.c_2.next = self.c_1
        self.c_3.next = self.c_0
        self.c_4.next = self.c_2
        self.c_5.next = self.c_6
        self.c_6.next = self.c_7
        self.c_7.next = self.c_10
        self.c_8.next = None
        self.c_9.next = self.c_8
        self.c_10.next = self.c_9
        self.c_11.next = self.c_5
        self.c_12.next = self.c_11

    def execute(self, ctx):
        for node in self.__start_nodes__:
            if hasattr(node, 'init'):
                node.init(ctx)
        SubGraphExecutor(self.c_4).do(ctx)

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