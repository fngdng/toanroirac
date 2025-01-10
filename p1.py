import numpy as np

# === Bài toán P1: Lập lịch hoạt động tối ưu hóa chi phí năng lượng (Tham lam) ===

# Thông số đầu vào
num_devices = 5  # Số lượng thiết bị
energy_consumption = [2, 4, 3, 5, 6]  # Năng lượng tiêu thụ của từng thiết bị (kWh)
energy_price = [3, 2, 5, 1, 4]  # Giá năng lượng tại mỗi thời điểm (đơn vị tiền/kWh)
renewable_energy = [8, 10, 7, 6, 9]  # Năng lượng tái tạo có sẵn tại mỗi thời điểm (kWh)
time_steps = len(energy_price)  # Số khoảng thời gian

# Thuật toán tham lam cho P1
schedule = np.zeros((num_devices, time_steps))
remaining_energy = renewable_energy.copy()

def greedy_schedule():
    for t in range(time_steps):
        # Sắp xếp thiết bị theo giá trị năng lượng/giá tăng dần
        sorted_devices = np.argsort([energy_consumption[i] / energy_price[t] for i in range(num_devices)])
        for device in sorted_devices:
            if remaining_energy[t] >= energy_consumption[device] and np.sum(schedule[device, :]) == 0:
                schedule[device, t] = 1
                remaining_energy[t] -= energy_consumption[device]

    print("\nLịch hoạt động (tham lam):")
    print(schedule)
    total_cost = sum(
        energy_price[t] * sum(schedule[:, t] * energy_consumption) for t in range(time_steps)
    )
    print(f"Chi phí năng lượng tối thiểu (tham lam): {total_cost:.2f}")

# Gọi hàm tham lam cho P1
greedy_schedule()
