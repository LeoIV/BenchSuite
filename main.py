import argparse

import torch

from benchsuite import settings
from benchsuite.lasso_dna import LassoDNA

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='BenchSuite',
        description='Provides some benchmarks',
        epilog='Enjoy the program!')
    parser.add_argument("--name", help="Name of the benchmark", type=str, default="lasso_dna")
    parser.add_argument("--x", "-x", help="The point", type=float, nargs="+")
    args = parser.parse_args()

    if args.name == "lasso_dna":
        bench = LassoDNA()
    else:
        raise RuntimeError(f"Unknown benchmark {args.name}")

    x = torch.tensor(args.x, dtype=settings.DTYPE, device=settings.DEVICE)

    y = bench(x)
    print(y.detach().cpu().numpy().tolist())
