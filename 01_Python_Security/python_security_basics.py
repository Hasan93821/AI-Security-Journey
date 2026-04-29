# تمرين 2.1

attacker_ips = ["185.22.34.67", "45.76.12.89", "185.22.34.67", "91.234.56.78"]
timestamps = ["2026-04-29 08:15", "2026-04-29 08:17", "2026-04-29 08:20"]

print("=== تحليل هجمات محتملة ===\n")

# 1. اطبع عدد الـ IPs الموجودة في القائمة
print("1. عدد الـ IPs في القائمة:", len(attacker_ips))

# 2. حساب تكرار كل IP باستخدام Dictionary
ip_count = {}
for ip in attacker_ips:
    if ip in ip_count:
        ip_count[ip] += 1
    else:
        ip_count[ip] = 1

print("\n2. تكرار كل IP:")
for ip, count in ip_count.items():
    print(f"   IP: {ip} → ظهر {count} مرات")

# كشف الـ IP المكرر
print("\n   IPs المشبوهة (تكررت):")
for ip, count in ip_count.items():
    if count > 1:
        print(f"   ⚠️  {ip} (تكرر {count} مرات)")

# 3. إنشاء قاموس يربط كل IP بقائمة الأوقات
ip_timestamps = {}
for ip, timestamp in zip(attacker_ips, timestamps):
    if ip in ip_timestamps:
        ip_timestamps[ip].append(timestamp)
    else:
        ip_timestamps[ip] = [timestamp]

print("\n3. كل IP مع أوقات ظهوره:")
for ip, times in ip_timestamps.items():
    print(f"   IP: {ip} → الأوقات: {times}")