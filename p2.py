import numpy as np

# Thông số đầu vào
num_rooms = 3  # Số lượng phòng
ac_units = [2, 1, 2]  # Số lượng thiết bị điều hòa trong mỗi phòng
temperature_range = [(20, 25), (22, 26), (21, 24)]  # Khoảng nhiệt độ thoải mái (°C)
external_temp = [30, 28, 27, 29, 31]  # Nhiệt độ bên ngoài tại mỗi thời điểm (°C)
time_steps_p2 = len(external_temp)  # Số khoảng thời gian
cooling_power = [[-2, -1], [-3], [-2, -1]]  # Mức làm lạnh của mỗi thiết bị (°C)
inertia = 0.8  # Quán tính nhiệt của tòa nhà

# === Bài toán P2 (Knapsack Problem) ===

def knapsack_temperature():
    dp = [[0] * (time_steps_p2 + 1) for _ in range(sum(len(p) for p in cooling_power) + 1)]
    items = []

    # Gom các thiết bị điều hòa làm vật phẩm knapsack
    for r, powers in enumerate(cooling_power):
        for power in powers:
            items.append((power, abs(power)))

    for i, (power, cost) in enumerate(items, start=1):
        for t in range(1, time_steps_p2 + 1):
            if t >= abs(power):
                dp[i][t] = max(dp[i - 1][t], dp[i - 1][t - abs(power)] + cost)
            else:
                dp[i][t] = dp[i - 1][t]

    print("\nChi phí tối thiểu (Knapsack):")
    print(dp[-1][-1])

# Gọi hàm Knapsack cho P2
knapsack_temperature()
