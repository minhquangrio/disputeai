import random
import re
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


   

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

#Máy tính
async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Lấy nội dung của tin nhắn và loại bỏ lệnh '/calculate'
    expression = update.message.text.replace('/calculate', '').strip()

    try:
        # Kiểm tra xem biểu thức có hợp lệ không bằng cách sử dụng regex
        if not re.match(r"^[0-9+\-*/.() ]+$", expression):
            raise ValueError("Biểu thức không hợp lệ.")
        
        # Thực hiện phép tính
        result = eval(expression)
        
        # Trả kết quả
        await update.message.reply_text(f"Kết quả của biểu thức '{expression}' là: {result}")
    except Exception as e:
        await update.message.reply_text(f"Đã xảy ra lỗi: {str(e)}")


# Hàm để lấy trích đoạn ngẫu nhiên từ API Quotable
def get_random_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return f"{data['content']} - {data['author']}"
    else:
        return "Không thể lấy trích đoạn ngẫu nhiên."

# Hàm xử lý tính năng thư giãn
async def relax(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    quote = get_random_quote()
    await update.message.reply_text(quote)


app = ApplicationBuilder().token("6814966479:AAE7JjxF1SrnrrD1oALzA7f4JJ2pPqof0TM").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("calculate", calculate))
app.add_handler(CommandHandler("relax", relax))

app.run_polling()