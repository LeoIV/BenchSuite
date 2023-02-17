from benchsuite import LassoDNA, \
    LassoSimple, \
    LassoMedium, \
    LassoHard, \
    LassoHigh, \
    SVM, \
    Mopta08, \
    LunarLanderBenchmark, \
    RobotPushingBenchmark, \
    MujocoSwimmer, \
    MujocoHumanoid, \
    MujocoAnt, \
    MujocoHopper, \
    MujocoWalker, \
    MujocoHalfCheetah

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
    swimmer=MujocoSwimmer,
    humanoid=MujocoHumanoid,
    ant=MujocoAnt,
    hopper=MujocoHopper,
    walker=MujocoWalker,
    halfcheetah=MujocoHalfCheetah,
)
