from telegram.ext import *

API_KEY = '1973632643:AAFCcPOXw9Gkxx-gDa2S6SmHYcblX_HHJBk' # token of bot

# this function replay to users
def handle_message(update, context):
    text = str(update.message.text).lower()


    if text == "/start":
        update.message.reply_text(f"Hi, {update['message']['chat']['first_name']}\n Welcome to foody\n Please enter M for menu list")
    
    elif text == "m":
        update.message.reply_text(f'''MENU:\nIndian Food\nChinese Food\nSea Food''')
    
    elif text == "indian food":
        update.message.reply_text(f'''INDIAN FOOD:\nVeg Food\nNon-Veg Food''')
    
    elif text == "chinese food":
        update.message.reply_text(f'''CHINESE FOOD:\nSzechwan Fried Rice\nHot Sour Soup\nChicken Chilli''')
    
    elif text == "sea food":
        update.message.reply_text(f'''SEA FOOD:\nPrawn Pollichathu\nLobster Malay Curry\nFish Koliwada''')
    
    elif text == "veg food":
        update.message.reply_text(f'''VEG FOOD:\nPanner Tikka\nDahi Kebab\nKadai Mushroom''')
    
    elif text == "non-veg food" or text == "non veg food":
        update.message.reply_text(f'''NON-VEG FOOD:\nGrilled Chicken\nButter Chicken\nChicken 65''')
    
    elif text == "panner tikka":
        handle_message.cost += 1
        update.message.reply_text(f'''Your order has been Received.\nDo you want Roti or Rice then enter any one of them otherwise enter No''')
    
    elif text == "dahi kebab":
        handle_message.cost += 1
        update.message.reply_text(f'''Your order has been Received.\nDo you want Roti or Rice then enter any one of them otherwise enter No''')
    
    elif text == "kadai mushroom":
        handle_message.cost += 1
        update.message.reply_text(f'''Your order has been Received.\nDo you want Roti or Rice then enter any one of them otherwise enter No''')
    
    elif text == "grilled chicken":
        handle_message.cost += 1
        update.message.reply_text(f'''Your order has been Received.\nDo you want Roti or Rice then enter any one of them otherwise enter No''')
    
    elif text == "butter chicken":
        handle_message.cost += 1
        update.message.reply_text(f'''Your order has been Received.\nDo you want Roti or Rice then enter any one of them otherwise enter No''')
    
    elif text == "chicken 65":
        handle_message.cost += 1
        update.message.reply_text(f'''Your order has been Received.\nDo you want Roti or Rice then enter any one of them otherwise enter No''')
    
    elif text == "prawn pollichathu":
        handle_message.cost += 1
        update.message.reply_text(f'''Your order has been Received.\nDo you want Roti or Rice then enter any one of them otherwise enter No''')
    
    elif text == "fish koliwada":
        handle_message.cost += 1
        update.message.reply_text(f'''Your order has been Received.\nDo you want Roti or Rice then enter any one of them otherwise enter No''')
    
    elif text == "lobster malay curry":
        handle_message.cost += 1
        update.message.reply_text(f'''Your order has been Received.\nDo you want Roti or Rice then enter any one of them otherwise enter No''')

    elif text == "roti":
        update.message.reply_text(f'''How many {text} do you want? ''')
    
    elif text == "rice":
        update.message.reply_text(f'''Quantity?''')

    elif text.isnumeric():
        handle_message.other += int(text)
        update.message.reply_text(f'''Your order has been saved.\nDo you want anything else?\n(Yes/No)''')
    
    elif text == "szechwan rice":
        handle_message.cost += 1
        update.message.reply_text(f'''Your order has been Received.\nDo you want anything else?\n(Yes/No)''')
    
    elif text == "hot sour soup":
        handle_message.cost += 1
        update.message.reply_text(f'''Your order has been Received.\nDo you want anything else?\n(Yes/No)''')
    
    elif text == "chicken chilli":
        handle_message.cost += 1
        update.message.reply_text(f'''Your order has been Received.\nDo you want anything else?\n(Yes/No)''')
    
    elif text == "yes":
        update.message.reply_text(f'''Please enter M for menu list.''')
    
    elif text == "no":
        total_cost = (handle_message.cost * 100) + (handle_message.other * 5)
        update.message.reply_text(f'''Thank You {update['message']['chat']['first_name']} for ordering.\nTotal cost is {total_cost} ''')
        handle_message.cost = 0
        handle_message.other = 0
    # print(handle_message.cost,handle_message.other)  <---- This was for testing output
handle_message.cost = 0
handle_message.other = 0
    
if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    updater.start_polling(1.0)
    updater.idle()
