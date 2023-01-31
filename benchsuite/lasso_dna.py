import numpy as np
import torch

from benchsuite import settings
from benchsuite.benchmark import Benchmark


class LassoDNA(Benchmark):

    def __init__(self):
        super().__init__(name="lasso_dna", dim=180, lb=torch.zeros(180, device=settings.DEVICE, dtype=settings.DTYPE),
                         ub=torch.ones(180, device=settings.DEVICE, dtype=settings.DTYPE))
        from LassoBench import LassoBench
        self._b: LassoBench.RealBenchmark = LassoBench.RealBenchmark(
            pick_data="dna", mf_opt="discrete_fidelity"
        )

    def __call__(self, x: torch.Tensor) -> torch.Tensor:
        return torch.tensor(self._b.evaluate(x.cpu().numpy().astype(np.double)), device=settings.DEVICE,
                            dtype=settings.DTYPE).unsqueeze(-1)
