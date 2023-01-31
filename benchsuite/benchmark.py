import abc

import torch


class Benchmark(abc.ABC):

    def __init__(
            self,
            dim: int,
            lb: torch.Tensor,
            ub: torch.Tensor,
    ):
        self.dim = dim
        self.lb = lb
        self.ub = ub

    @abc.abstractmethod
    def __call__(self, x: torch.Tensor) -> torch.Tensor:
        raise NotImplementedError()
