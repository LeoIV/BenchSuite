import argparse

import torch

from benchsuite import settings, SVM
from benchsuite import LassoDNA, LassoSimple, LassoMedium, LassoHard, LassoHigh

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='BenchSuite',
        description='Provides some benchmarks',
        epilog='Enjoy the program!')
    parser.add_argument("--name", help="Name of the benchmark", type=str, required=True)
    parser.add_argument("--x", "-x", help="The point", type=float, nargs="+", required=True)
    args = parser.parse_args()

    if args.name == "lasso_dna":
        bench = LassoDNA()
    elif args.name == "lasso_simple":
        bench = LassoSimple()
    elif args.name == "lasso_medium":
        bench = LassoMedium()
    elif args.name == "lasso_hard":
        bench = LassoHard()
    elif args.name == "lasso_high":
        bench = LassoHigh()
    elif args.name == "svm":
        bench = SVM()
    else:
        raise RuntimeError(f"Unknown benchmark {args.name}")

    x = torch.tensor(args.x, dtype=settings.DTYPE, device=settings.DEVICE)

    y = bench(x)
    print(y.detach().cpu().numpy().tolist()[0])
