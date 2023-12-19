import telebot
import datetime

# Mở file token.txtpy 
with open("token.txt", "r") as f:
    token = f.read().strip()

# Tạo bot
bot = telebot.TeleBot(token)

# Xử lý tin nhắn
@bot.message_handler(commands=['start', 'help', 'time', 'get_group_info'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Xin chào! Tôi là bot Telegram được tạo bằng Python.')
    elif message.text == '/help':
        bot.send_message(message.chat.id, 'Có thể làm gì với tôi?')
    else:
        bot.send_message(message.chat.id, 'Bạn muốn biết thời gian hiện tại không?')

# Xử lý tin nhắn thời gian
@bot.message_handler(commands=['time'])
def time(message):
    now = datetime.datetime.now()
    bot.send_message(message.chat.id, 'Bây giờ là {}'.format(now.strftime('%H:%M:%S')))

# Xử lý tin nhắn lấy tên và ID của nhóm
@bot.message_handler(commands=['get_group_info'])
def get_group_info(message):
    # Lấy ID của nhóm
    group_id = message.chat.id

    # Lấy thông tin về nhóm
    group = bot.get_chat(group_id)

    # Gửi tin nhắn với tên và ID của nhóm
    bot.send_message(message.chat.id, 'Tên nhóm: {}'.format(group.title))
    bot.send_message(message.chat.id, 'ID nhóm: {}'.format(group.id))

# Xử lý tin nhắn
@bot.message_handler(commands=['get_channel_info'])
def get_channel_info(message):
    # Lấy ID của kênh
    channel_id = message.chat.id

    # Lấy thông tin về kênh
    channel = bot.get_chat(channel_id)

    # Gửi tin nhắn với tên và ID của kênh
    bot.send_message(message.chat.id, 'Tên kênh: {}'.format(channel.title))
    bot.send_message(message.chat.id, 'ID kênh: {}'.format(channel.id))

# Xử lý tin nhắn lấy số lượng thành viên trong nhóm
@bot.message_handler(commands=['get_group_members'])
def get_group_members(message):
    # Lấy ID của nhóm
    group_id = message.chat.id

    # Lấy số lượng thành viên trong nhóm
    group_members_count = bot.get_chat_members_count(group_id)

    # Gửi số lượng thành viên cho người dùng
    bot.send_message(message.chat.id, 'Số lượng thành viên trong nhóm này là: {}'.format(group_members_count))




# Chạy bot
bot.polling()
