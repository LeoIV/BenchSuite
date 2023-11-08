from benchsuite import BaseRegistry

from benchsuite.other.mopta import Mopta08
from benchsuite.other.svm import SVM


class OtherRegistry(metaclass=BaseRegistry):
    
    BENCHMARKS = {
        'svm': SVM,
        'mopta': Mopta08,
    }
    
