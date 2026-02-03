import numpy as np
import robosuite as suite
 
# 创建环境实例
env = suite.make(
    env_name="Lift",  # 任务名称，可以尝试其他任务，例如 "Stack" 或 "Door"
    robots="Panda",  # 使用的机器人类型，可以尝试其他机器人，例如 "Sawyer" 或 "Jaco"
    has_renderer=True,  # 是否启用屏幕渲染器（在屏幕上显示环境）
    has_offscreen_renderer=False,  # 是否启用离屏渲染器（用于生成图像等）
    use_camera_obs=False,  # 是否使用摄像头观察
)
 
# 重置环境（初始化环境状态）
obs = env.reset()
 
# 循环运行1000步
for i in range(1000):
    action = np.random.randn(*env.action_spec[0].shape) * 0.1 # 生成随机动作，动作幅度乘以0.1限制动作大小
    obs, reward, done, info = env.step(action) # 在环境中执行动作，获取观察值、奖励、是否完成等信息
    env.render() # 在屏幕上渲染当前环境状态
 
    # 检查是否需要重置环境
    if done:
        print(f"Episode ended at step {i}. Resetting environment.")
        obs = env.reset()