# تمرين اليوم 1 - محلل Logs بسيط

# 1. قائمة من عناوين IP (مثال على log)
ip_list = ["192.168.1.10", "10.0.0.5", "192.168.1.10", "45.67.89.12", "192.168.1.10"]

# 2. قاموس لعدد مرات ظهور كل IP
ip_count = {}

for ip in ip_list:
    if ip in ip_count:
        ip_count[ip] += 1
    else:
        ip_count[ip] = 1

print("نتائج تحليل الـ IPs:")
for ip, count in ip_count.items():
    print(f"IP: {ip} → عدد المرات: {count}")

# 3. كشف IP مشبوه (يظهر أكثر من مرتين)
print("\nIPs مشبوهة (تكرار > 2):")
for ip, count in ip_count.items():
    if count > 2:
        print(f"⚠️  IP مشبوه: {ip} ({count} مرات)")