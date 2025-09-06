import telebot

# 🔑 حط التوكن حقك هنا
TOKEN = "8286428933:AAF6MmG_FFJajXiyNIwRn3q7sx7P3jdgw4Y"
bot = telebot.TeleBot(TOKEN)

# ⚠️ التحذير يظهر بكل درس
WARNING = "\n\n⚠️ تنبيه: أنا غير مسؤول عن أي استخدام خاطئ للمعلومات. الهدف تعليمي فقط."

# 🚀 /start
@bot.message_handler(commands=['start'])
def start(message):
    text = (
        "هلا فيك 👋\n"
        "أنا بوت لتعليم الأمن السيبراني والهكر الأخلاقي للمبتدئين.\n\n"
        "اكتب /help عشان تشوف الأوامر."
        + WARNING
    )
    bot.send_message(message.chat.id, text)

# 📖 /help
@bot.message_handler(commands=['help'])
def help(message):
    text = (
        "📌 قائمة الأوامر:\n"
        "/start - بدء البوت\n"
        "/about - عن البوت\n"
        "/lessons - قائمة الدروس\n"
    )
    bot.send_message(message.chat.id, text)

# ℹ️ /about
@bot.message_handler(commands=['about'])
def about(message):
    text = (
        "🤖 هذا البوت مخصص لتقديم شروحات عن الأمن السيبراني "
        "والهاكينغ الأخلاقي للمبتدئين، مع تركيز على أجهزة الكمبيوتر (PC)."
        + WARNING
    )
    bot.send_message(message.chat.id, text)

# 📚 /lessons
@bot.message_handler(commands=['lessons'])
def all_lessons(message):
    text = (
        "📚 قائمة الدروس:\n\n"
        "🖥️ الكمبيوتر و PC:\n"
        "/os - أنظمة التشغيل\n"
        "/network - الشبكات\n"
        "/tools - أدوات مهمة\n\n"
        "🔐 الأمن السيبراني:\n"
        "/cyberbasics - مقدمة الأمن السيبراني\n"
        "/attacks - أنواع الهجمات\n"
        "/defense - طرق الحماية\n\n"
        "🕵️ الهاكينغ الأخلاقي:\n"
        "/ethical - عن الهاكر الأخلاقي\n"
        "/pentest - خطوات اختبار الاختراق\n"
        "/linux - أوامر لينكس"
    )
    bot.send_message(message.chat.id, text)

# === دروس الكمبيوتر ===
@bot.message_handler(commands=['os'])
def os_lesson(message):
    text = (
        "🖥️ أنظمة التشغيل:\n"
        "- Windows: الأكثر استخدامًا، سهل لكن مستهدف بكثرة.\n"
        "- Linux: الأقوى للهكر والأمن السيبراني.\n"
        "- macOS: آمن لكن محدود للهاكينغ."
        + WARNING
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['network'])
def network_lesson(message):
    text = (
        "🌐 أساسيات الشبكات:\n"
        "- IP Address: عنوان الجهاز.\n"
        "- DNS: يترجم المواقع لعناوين.\n"
        "- Firewall: جدار ناري للحماية."
        + WARNING
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['tools'])
def tools_lesson(message):
    text = (
        "🛠️ أدوات مهمة:\n"
        "- Wireshark: لتحليل الشبكات.\n"
        "- Nmap: لفحص الأجهزة.\n"
        "- Burp Suite: لاختبار الثغرات."
        + WARNING
    )
    bot.send_message(message.chat.id, text)

# === الأمن السيبراني ===
@bot.message_handler(commands=['cyberbasics'])
def cyberbasics(message):
    text = (
        "🔐 مقدمة الأمن السيبراني:\n"
        "هو علم حماية الأنظمة والشبكات من الاختراقات."
        + WARNING
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['attacks'])
def attacks(message):
    text = (
        "⚔️ أنواع الهجمات:\n"
        "- Phishing: التصيد.\n"
        "- DDoS: هجمات الحرمان من الخدمة.\n"
        "- SQL Injection: استغلال قواعد البيانات."
        + WARNING
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['defense'])
def defense(message):
    text = (
        "🛡️ طرق الحماية:\n"
        "- استخدام جدار ناري.\n"
        "- تحديث الأنظمة.\n"
        "- كلمات مرور قوية."
        + WARNING
    )
    bot.send_message(message.chat.id, text)

# === الهاكينغ الأخلاقي ===
@bot.message_handler(commands=['ethical'])
def ethical(message):
    text = (
        "🕵️ الهاكر الأخلاقي:\n"
        "شخص مختص باكتشاف الثغرات وحماية الأنظمة بشكل قانوني."
        + WARNING
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['pentest'])
def pentest(message):
    text = (
        "🛠️ خطوات اختبار الاختراق:\n"
        "1- Recon (جمع المعلومات)\n"
        "2- Scanning (فحص)\n"
        "3- Exploitation (استغلال)\n"
        "4- Report (تقرير)"
        + WARNING
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['linux'])
def linux(message):
    text = (
        "🐧 أوامر لينكس الأساسية:\n"
        "- ls → عرض الملفات\n"
        "- cd → تغيير المجلد\n"
        "- ifconfig → عرض الشبكة"
        + WARNING
    )
    bot.send_message(message.chat.id, text)

# 🟢 تشغيل البوت
print("✅ البوت يشتغل...")
bot.infinity_polling()
