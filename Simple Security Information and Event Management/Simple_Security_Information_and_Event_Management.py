import wmi

def get_event_logs():
    # إنشاء كائن WMI للتفاعل مع Event Viewer
    c = wmi.WMI()
    
    # قائمة لحفظ السجلات التي تم جمعها
    logs = []
    
    # قراءة السجلات من سجل النظام (System Log)
    print("Reading System Logs...")
    for log in c.Win32_NTLogEvent(Logfile='System'):
        log_info = f"Event ID: {log.EventCode}, Message: {log.Message}, Time: {log.TimeGenerated}"
        print(log_info)  # عرض السجل في الشاشة
        logs.append(log_info)  # إضافة السجل إلى القائمة
    
    return logs

def save_logs_to_file(logs, file_name='event_logs.txt'):
    # حفظ السجلات في ملف نصي
    with open(file_name, 'w') as file:
        for log in logs:
            file.write(log + "\n")
    print(f"Logs saved to {file_name}")

def main():
    # قراءة السجلات
    logs = get_event_logs()
    
    # حفظ السجلات في ملف نصي
    save_logs_to_file(logs)

# تشغيل البرنامج
if __name__ == '__main__':
    main()

