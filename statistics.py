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


@xai_component
class ComplexityInit(Component):
    """
    Creates on object of elephant.statistics.Complexity an outputs it

    ##### inPorts:
    - spiketrains (list[neo.SpikeTrain]): Spike trains with a common time axis (same t_start and t_stop)

    ##### outPorts:
    - complexity (elephant.statistics.Complexity): The firing rate of the spiketrain.
    """
    spiketrains: InCompArg[list[neo.SpikeTrain]]
    complexity: OutArg[elephant.statistics.Complexity]

    def execute(self, ctx) -> None:
        spiketrains = self.spiketrains.value
        sampling_rate = 1/pq.s
        self.complexity.value = elephant.statistics.Complexity(spiketrains, sampling_rate=sampling_rate)

@xai_component
class ComplexityPdf(Component):
    """
    Calls the pdf method on the passed Complexity object on outputs the result

    ##### inPorts:
    - complexity (elephant.statistics.Complexity): The firing rate of the spiketrain.

    ##### outPorts:
    - pdf (neo.AnalogSignal): Probability density computed from the complexity histogram.
    """
    complexity: InCompArg[elephant.statistics.Complexity]
    pdf: OutArg[neo.AnalogSignal]

    def execute(self, ctx) -> None:
        complexity = self.complexity.value
        self.pdf.value = complexity.pdf()