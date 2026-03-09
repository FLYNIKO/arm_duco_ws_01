import math
def compute_spray_swinging_angle(A, B, C):

    ax, ay = A
    bx, by = B
    cx, cy = C
    # 计算两条边的方向向量
    ABx, ABy = bx - ax, by - ay
    ACx, ACy = cx - ax, cy - ay
    # 定义计算角度的函数（以X轴左侧为0°）
    def compute_angle(x, y):
        # atan2(y, x) 是相对 X轴正向的角度
        # 我们需要相对 X轴负向（左侧）为 0°
        angle_rad = math.atan2(y, x)
        angle_deg = math.degrees(angle_rad)
        # 将角度转换，使得 X轴左侧为0°
        # X轴左方向相当于180°，所以相对左侧角度 = angle_deg - 180
        deg_relative = angle_deg - 180
        # 让角度落在 [-180, 180] 区间
        if deg_relative > 180:
            deg_relative -= 360
        elif deg_relative < -180:
            deg_relative += 360
        return deg_relative
        
    deg_AB = -compute_angle(ABx, ABy)
    deg_AC = -compute_angle(ACx, ACy)
    if deg_AB > deg_AC:
        deg_1 = max(-44, min(45, deg_AB))
        deg_2 = max(-45, min(44, deg_AC))
    else:
        deg_1 = max(-44, min(45, deg_AC))
        deg_2 = max(-45, min(44, deg_AB))

    return [deg_1, deg_2]

if __name__ == "__main__":
    # 示例1: 标准三角形
    a1 = [-0.21, 0.17]
    b1 = [-0.55, -0.25]
    c1 = [-0.35, -0.25]
    result1 = compute_spray_swinging_angle(a1, b1, c1)
    print(f"示例1: A={a1}, B={b1}, C={c1}")
    print(f"边AB与X轴夹角: {result1[0]:.2f}°")
    print(f"边AC与X轴夹角: {result1[1]:.2f}°")
    print()