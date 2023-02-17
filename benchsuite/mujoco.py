import os
from pathlib import Path
from typing import Any

import torch

from benchsuite import settings
from benchsuite.benchmark import Benchmark
from benchsuite.utils.mujoco import func_factories


class MujocoBenchmark(Benchmark):

    def __init__(
        self,
        dim: int,
        ub: torch.Tensor,
        lb: torch.Tensor,
        benchmark: Any
    ):
        super().__init__(dim=dim, lb=lb, ub=ub)
        print("Mujoco benchmark called")
        self.benchmark = benchmark

    def __call__(
        self,
        x: torch.Tensor
    ) -> torch.Tensor:
        print("Mujoco benchmark called")
        if x.ndim == 1:
            x = x.unsqueeze(0)
        y = self.benchmark(x)[0]
        return -torch.tensor(y)


class MujocoSwimmer(MujocoBenchmark):
    def __init__(
        self
    ):
        super().__init__(
            dim=16,
            ub=torch.ones(16, dtype=settings.DTYPE, device=settings.DEVICE),
            lb=-1 * torch.ones(16, dtype=settings.DTYPE, device=settings.DEVICE),
            benchmark=func_factories["swimmer"].make_object()
        )


class MujocoHumanoid(MujocoBenchmark):
    def __init__(
        self
    ):
        super().__init__(
            dim=6392,
            ub=torch.ones(6392, dtype=settings.DTYPE, device=settings.DEVICE),
            lb=-1 * torch.ones(6392, dtype=settings.DTYPE, device=settings.DEVICE),
            benchmark=func_factories["humanoid"].make_object()
        )


class MujocoAnt(MujocoBenchmark):
    def __init__(
        self
    ):
        super().__init__(
            dim=888,
            ub=torch.ones(888, dtype=settings.DTYPE, device=settings.DEVICE),
            lb=-1 * torch.ones(888, dtype=settings.DTYPE, device=settings.DEVICE),
            benchmark=func_factories["ant"].make_object()
        )


class MujocoHopper(MujocoBenchmark):
    def __init__(
        self
    ):
        super().__init__(
            dim=33,
            ub=1.4 * torch.ones(33, dtype=settings.DTYPE, device=settings.DEVICE),
            lb=-1.4 * torch.ones(33, dtype=settings.DTYPE, device=settings.DEVICE),
            benchmark=func_factories["hopper"].make_object()
        )


class MujocoWalker(MujocoBenchmark):
    def __init__(
        self
    ):
        super().__init__(
            dim=102,
            ub=0.9 * torch.ones(102, dtype=settings.DTYPE, device=settings.DEVICE),
            lb=-1.8 * torch.ones(102, dtype=settings.DTYPE, device=settings.DEVICE),
            benchmark=func_factories["walker_2d"].make_object()
        )


class MujocoHalfCheetah(MujocoBenchmark):
    def __init__(
        self
    ):
        super().__init__(
            dim=102,
            ub=torch.ones(102, dtype=settings.DTYPE, device=settings.DEVICE),
            lb=-1.0 * torch.ones(102, dtype=settings.DTYPE, device=settings.DEVICE),
            benchmark=func_factories["half_cheetah"].make_object()
        )
