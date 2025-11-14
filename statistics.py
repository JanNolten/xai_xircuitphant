from xai_components.base import InArg, OutArg, InCompArg, Component, xai_component, dynalist, dynatuple
from typing import Union
import elephant
import neo
import quantities as pq
import numpy as np

@xai_component
class MeanFiringRate(Component):
    """
    Calls the elephant.statistic.mean_firing_rate function and outputs its result.

    ##### inPorts:
    - spiketrain (neo.Spiketrain, pq.Quantity, np.ndarray): The spike times. Compulsory.

    ##### outPorts:
    - firing_rate (float, pq.Quantity, np.ndarray]): The firing rate of the spiketrain.
    """
    spiketrain: InCompArg[Union[neo.SpikeTrain, pq.Quantity, np.ndarray]]
    firing_rate: OutArg[Union[float, pq.Quantity, np.ndarray]]

    def execute(self, ctx) -> None:
        spiketrain = self.spiketrain.value
        self.firing_rate.value = elephant.statistics.mean_firing_rate(spiketrain)