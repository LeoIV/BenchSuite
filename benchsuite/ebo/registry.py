from benchsuite import BaseRegistry
from benchsuite.ebo.rover import RoverBenchmark
from benchsuite.ebo.robotpushing import RobotPushingBenchmark
from benchsuite.ebo.lunarlander import LunarLanderBenchmark


class EBORegistry(metaclass=BaseRegistry):
    
    BENCHMARKS = {
        'rover': RoverBenchmark,
        'robot': RobotPushingBenchmark,
        'lunar': LunarLanderBenchmark,
    }
    
