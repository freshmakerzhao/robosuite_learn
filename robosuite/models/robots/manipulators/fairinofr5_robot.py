import numpy as np
from robosuite.models.robots.manipulators.manipulator_model import ManipulatorModel
from robosuite.utils.mjcf_utils import xml_path_completion

class FairinoFR5(ManipulatorModel):

    arms = ["right"]

    def __init__(self, idn=0):
        super().__init__(xml_path_completion("robots/fairino_fr5/robot.xml"), idn=idn)

    @property
    def default_base(self):
        return "RethinkMount"

    @property
    def default_gripper(self):
        return {"right": "Robotiq85Gripper"}

    @property
    def default_controller_config(self):
        return {"right": "default_fairino_fr5"}

    @property
    def arm_type(self):
        return "single"

    @property
    def init_qpos(self):
        return np.array([-0.470, -1.735, 2.480, -2.275, -1.590, -1.991])

    @property
    def base_xpos_offset(self):
        return {
            "bins": (-0.5, -0.1, 0),
            "empty": (-0.6, 0, 0),
            "table": lambda table_length: (-0.16 - table_length / 2, 0, 0),
        }

    @property
    def top_offset(self):
        # 用于计算机器人上方安全距离的偏移
        return np.array((0, 0, 1.0))

    @property
    def _horizontal_radius(self):
        return 0.5