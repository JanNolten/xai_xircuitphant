from xai_components.base import InArg, OutArg, InCompArg, Component, xai_component, dynalist, dynatuple
from typing import Union
import elephant
import neo
import quantities as pq
import numpy as np

@xai_component
class GenerateArray(Component):
    """
    Genrates an numpy array from a list.

    ##### inPorts:
    - _list (list): The input list.

    ##### outPorts:
    - array (np.ndarray): The genrated array.
    """
    _list: InCompArg[list]
    array: OutArg[np.ndarray]

    def execute(self, ctx) -> None:
        _list = self._list.value
        self.array.value = np.array(_list)

@xai_component
class GenerateQuantityFromFloat(Component):
    """
    Genrates an quantities.Quantity from a float.
    Currently no unit selection.

    ##### inPorts:
    - _float (float): The input float.

    ##### outPorts:
    - quantity (pq.Quantity): The genrated Quantity.
    """
    _float: InCompArg[float]
    quantity: OutArg[pq.Quantity]

    def execute(self, ctx) -> None:
        _float = self._float.value
        self.quantity.value = _float * pq.s

@xai_component
class GenerateQuantityFromArray(Component):
    """
    Genrates an quantities.Quantity from a array.
    Currently no unit selection.

    ##### inPorts:
    - array (np.ndarray): The input array.

    ##### outPorts:
    - quantity (pq.Quantity): The genrated Quantity.
    """
    array: InCompArg[np.ndarray]
    quantity: OutArg[pq.Quantity]

    def execute(self, ctx) -> None:
        array = self.array.value
        self.quantity.value = array * pq.s

@xai_component
class GenerateSpikeTrain(Component):
    """
    Genrates a neo.SpikeTrain.

    ##### inPorts:
    - data (pq.Quantity): The input data.
    - t_start (pq.Quantity): The start.
    - t_stop (pq.Quantity): The stop.

    ##### outPorts:
    - spiketrain (neo.SpikeTrain): The genrated Spiketrain.
    """
    data: InCompArg[pq.Quantity]
    t_start: InCompArg[pq.Quantity]
    t_stop: InCompArg[pq.Quantity]
    spiketrain: OutArg[neo.SpikeTrain]

    def execute(self, ctx) -> None:
        data = self.data.value
        t_start = self.t_start.value
        t_stop = self.t_stop.value
        self.spiketrain.value = neo.SpikeTrain(data, t_start=t_start, t_stop=t_stop)

@xai_component
class GenerateSpikeTrains(Component):
    """
    Genrates a list of neo.SpikeTrain from two SpikeTrains.

    ##### inPorts:
    - spiketrain_i (neo.SpikeTrain): The input SpikeTrain i.
    - spiketrain_j (neo.SpikeTrain): The input SpikeTrain j.

    ##### outPorts:
    - spiketrains (list[neo.SpikeTrain]): The genrated SpikeTrain list.
    """
    spiketrain_i: InCompArg[neo.SpikeTrain]
    spiketrain_j: InCompArg[neo.SpikeTrain]
    spiketrains: OutArg[list[neo.SpikeTrain]]

    def execute(self, ctx) -> None:
        spiketrain_i = self.spiketrain_i.value
        spiketrain_j = self.spiketrain_j.value
        self.spiketrains.value = [spiketrain_i, spiketrain_j]