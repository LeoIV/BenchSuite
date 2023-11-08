Added containerized high-dimensional benchmarks for mujoco (swimmer, hopper etc.), EBO (lunar lander, rover, robot pushing), other (SVM, MOPTA08) and LassoBench.

To run:
build the relevant container (from recipes/[mujoco, lasso, ebo, other]):

```
sudo singularity build **mujuco_container.sif** recipes/mujoco
```

Call the relevant benchmark:


./mujuco_container.sif --benchmark_name swimmer -x 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
```

Benchmarks (benchmark_name, dim):
Mujoco: Swimmer (swimmer, 16), Hopper (hopper, 33), Walker (walker, 102), Half-Cheetah (cheetah, 102), Ant (ant, 888), Humanoid (humanoid, 6392)
EBO: Lunar lander (lunar, 12D), Robot pushing (robot, 14D), Rover (rover, 100D)
LassoBench: Real-DNA (dna, 180D), Synthetic-High (high, 300D), Synthetic-Hard (hard, 1000D)