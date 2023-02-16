import argparse

import torch

from benchsuite import settings, SVM
from benchsuite import LassoDNA, LassoSimple, LassoMedium, LassoHard, LassoHigh
from benchsuite.lunarlander import LunarLanderBenchmark
from benchsuite.mopta08 import Mopta08
from benchsuite.robotpushing import RobotPushingBenchmark

if __name__ == '__main__':

    benchmark_options = dict(
        lasso_dna=LassoDNA,
        lasso_simple=LassoSimple,
        lasso_medium=LassoMedium,
        lasso_hard=LassoHard,
        lasso_high=LassoHigh,
        svm=SVM,
        mopta08=Mopta08,
        lunarlander=LunarLanderBenchmark,
        robotpushing=RobotPushingBenchmark,
    )

    parser = argparse.ArgumentParser(
        prog='BenchSuite',
        description='Provides some benchmarks',
        epilog='Enjoy the program!'
    )
    parser.add_argument(
        "--name",
        help=f"Name of the benchmark. Options: {list(benchmark_options.keys())}",
        type=str,
        required=True
        )
    parser.add_argument("--x", "-x", help="The point", type=float, nargs="+", required=True)
    args = parser.parse_args()

    if args.name not in benchmark_options:
        raise RuntimeError(f"Unknown benchmark {args.name}")
    else:
        bench = benchmark_options[args.name]()

    x = torch.tensor(args.x, dtype=settings.DTYPE, device=settings.DEVICE)

    y = bench(x)
    print(y.detach().cpu().numpy().tolist()[0])
