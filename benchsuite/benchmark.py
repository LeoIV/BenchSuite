import abc

import torch


class Benchmark(abc.ABC):

    def __init__(
            self,
            name: str,
            dim: int,
            lb: torch.Tensor,
            ub: torch.Tensor,
    ):
        self.name = name
        self.dim = dim

    @abc.abstractmethod
    def __call__(self, x: torch.Tensor) -> torch.Tensor:
        raise NotImplementedError()
