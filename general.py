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
    - array (np.ndarray]): The genrated array.
    """
    _list: InCompArg[list]
    array: OutArg[np.ndarray]

    def execute(self, ctx) -> None:
        _list = self._list.value
        self.array.value = np.array(_list)