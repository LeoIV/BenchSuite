from benchsuite import BaseRegistry
from benchsuite.ebo.rover import RoverBenchmark
from benchsuite.ebo.robotpushing import RobotPushingBenchmark
from benchsuite.ebo.lunarlander import LunarLanderBenchmark
from benchsuite.ebo.mpd_rover import MPDRoverBenchmark


class EBORegistry(metaclass=BaseRegistry):
    
    BENCHMARKS = {
        'rover': RoverBenchmark,
        'robot': RobotPushingBenchmark,
        'lunar': LunarLanderBenchmark,
        'mpd_rover': MPDRoverBenchmark,
    }
    