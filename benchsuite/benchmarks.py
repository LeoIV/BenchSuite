from benchsuite import (
    LassoDNA,
    LassoSimple,
    LassoMedium,
    LassoHard,
    LassoHigh,
    SVM,
    Mopta08,
)
from benchsuite.contamination import Contamination
from benchsuite.labs import Labs
from benchsuite.maxsat import MaxSat60

benchmark_options = dict(
    lasso_dna=LassoDNA,
    lasso_simple=LassoSimple,
    lasso_medium=LassoMedium,
    lasso_hard=LassoHard,
    lasso_high=LassoHigh,
    svm=SVM,
    mopta08=Mopta08,
    maxsat60=MaxSat60,
    labs=Labs,
    contamination=Contamination,
)
