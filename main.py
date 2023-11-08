import argparse
import os
from pathlib import Path
from benchsuite.benchmarks import get_benchmark
from glob import glob

dir = Path(__file__).parent.absolute()  # noqa

import torch

from benchsuite import settings

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='BenchSuite',
        description='Provides some benchmarks',
        epilog='Enjoy the program!'
    )
    parser.add_argument(
        "--name",
        help=f"Name of the container. Options: {glob('recpies/containers/*')}",
        type=str,
        required=True
    )
    parser.add_argument(
        "--benchmark_name",
        help=f"Name of the benchmark. Options: {[]}",
        type=str,
        required=True
    )
    parser.add_argument("--x", "-x", help="The point", type=float, nargs="+", required=True)
    args = parser.parse_args()

    #if args.name not in benchmark_options:
    #    raise RuntimeError(f"Unknown benchmark {args.name}")
    #else:
    bench = get_benchmark(args.name, args.benchmark_name)

    x = torch.tensor(args.x, dtype=settings.DTYPE, device=settings.DEVICE)
    # scale x to the correct range
    x = bench.lb + (bench.ub - bench.lb) * x
    
    # set LIBSVMDATA_HOME /tmp/libsvmdata

    y = bench(x)
    print(y.detach().cpu().numpy().tolist()[0])
