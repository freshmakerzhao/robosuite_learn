import numpy as np
import robosuite as suite
from robosuite.controllers import load_composite_controller_config
# 自动加载官方预设的关节速度控制配置
controller_config = load_composite_controller_config(controller="BASIC")
# 修改其中右臂的控制方式为关节速度
# controller_config["part_controller_configs"]["right"]["type"] = "JOINT_VELOCITY"

# 2. 创建环境实例
env = suite.make(
    env_name="Lift",             # [修改点] 使用已注册的 Lift 环境
    robots="FairinoFR5",         # 确保这和你注册的类名一致
    has_renderer=True,           
    has_offscreen_renderer=False, 
    use_camera_obs=False,         
    controller_configs=controller_config,
    render_camera="frontview",   # 使用我们在 robot.xml 定义的相机
    ignore_done=True,            # 调试时防止因方块掉落导致重置
)

print(f"✅ 环境加载成功！当前动作空间维度: {env.action_dim}")

# 3. 重置并运行
obs = env.reset()
for i in range(1000):
    # 产生随机动作 (FR5 是 6 轴，action_dim 应该是 6)
    action = np.random.randn(env.action_dim) * 0.5 
    
    obs, reward, done, info = env.step(action) 
    env.render() 

env.close()