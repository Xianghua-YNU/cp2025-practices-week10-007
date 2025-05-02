# 导入 numpy 库，用于高效的数值计算和数组操作
import numpy as np
# 导入 matplotlib 库的 pyplot 模块，用于绘制各种类型的图表
import matplotlib.pyplot as plt
# 从 scipy 库的 integrate 模块导入 cumulative_trapezoid 函数，用于计算累积梯形积分
from scipy.integrate import cumulative_trapezoid

def main():
    # 读取数据：使用 numpy 的 loadtxt 函数从 'velocities.txt' 文件中读取数据
    data = np.loadtxt('C:\\Users\\32874\\Desktop\\新建 文本文档 (2).txt')
    # 提取时间数据：从 data 数组中选取所有行的第 0 列，赋值给变量 t 作为时间数据
    t = data[:, 0]
    # 提取速度数据：从 data 数组中选取所有行的第 1 列，赋值给变量 v 作为速度数据
    v = data[:, 1]

    # 计算总距离：使用 numpy 的 trapz 函数，通过梯形积分法根据速度 v 和时间 t 计算总距离
    total_distance = np.trapz(v, t)
    # 打印总距离：使用 f - 字符串格式化输出总运行距离，单位为米
    print(f"总运行距离: {total_distance} 米")

    # 计算累积距离：使用 scipy 的 cumulative_trapezoid 函数，根据速度 v 和时间 t 计算累积距离，初始值设为 0
    cumulative_distance = cumulative_trapezoid(v, t, initial=0)

    # 创建图表：创建一个新的绘图窗口
    plt.figure()
    # 绘制速度曲线：绘制速度 v 随时间 t 变化的曲线，并设置标签为 '速度'
    plt.plot(t, v, label='速度')
    # 绘制累积距离曲线：绘制累积距离随时间 t 变化的曲线，并设置标签为 '累积距离'
    plt.plot(t, cumulative_distance, label='累积距离')
    # 设置 x 轴标签：设置 x 轴的标签为 '时间 (秒)'
    plt.xlabel('时间 (秒)')
    # 设置 y 轴标签：设置 y 轴的标签为 '速度 (米/秒) / 距离 (米)'
    plt.ylabel('速度 (米/秒) / 距离 (米)')
    # 设置图表标题：设置图表的标题为 '速度与距离随时间变化'
    plt.title('速度与距离随时间变化')
    # 显示图例：显示图例，用于区分不同曲线所代表的含义
    plt.legend()
    # 显示图表：显示绘制好的图表
    plt.show()

# 确保只有当该脚本作为主程序直接运行时，才会调用 main 函数
if __name__ == "__main__":
    main()
