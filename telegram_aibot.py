#Importing Telegram Bot API
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os
#Import Google Gemini AI API
import google.generativeai as genai

#Initializing Telegram Bot Token and Bot Username 
TOKEN: Final = os.getenv("API_KEY")

BOT_USERNAME: Final = '@i_am_just_a_bot'

#Initializing Gemini API token
API_KEY = os.getenv("API_KEY")

genai.configure(api_key=API_KEY)
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 1200,
  "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config
  )

#commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, I am a AI bot for Saimon")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ask some questions like:\
                                    \nGive any prompt for the AI to answerto  or ask\
                                    \n[Who is Supran,Who is Pratyush,Who is Saimon,\
                                    \nWho is Bandre,Who is Mote,Who is Donkey,\
                                    \nTell me about Supran,Tell me about Pratyush,Tell me about Saimon]")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command")

#Responses

def handle_responses(text: str)-> str:
    processed_text: str = text.strip()
    if 'who is saimon' in processed_text.lower():
        return "Saimon is donkey"
    if 'who is donkey' in processed_text.lower():
        return "Donkey is Saimon"
    if 'tell me about saimon' in processed_text.lower() or 'tell me about donkey' in processed_text.lower():
        return 'Saimon is one of a rare and unique creature which has a distict appearence\
             \nas you can see all of the mountains and hills and caves and holes just by looking at his face🤩'
    if 'who is supran' in processed_text.lower():
        return 'Supran is Bandre'
    if 'who is bandre' in processed_text.lower():
        return 'Bandre is supran'
    if 'tell me about bandre' in processed_text.lower() or 'tell me about supran' in processed_text.lower():
        return 'Supran/Bandre is an anomaly of nature which cannot be set in a steady upright position,\
            \nhence the name Bandre which derived from a Nepali word called "Bange" which translates to curved in english.'
    if 'who is pratyush' in processed_text.lower():
        return 'Pratyush is Mote'
    if 'who is mote' in processed_text.lower():
        return 'Mote/Pratyush is the son of Prakash Baniya who is the head of the infamous crime syndicate\
             \ncalled Prakash gang who is also known as Prakash don.'
    if 'tell me about pratyush' in processed_text.lower() or 'tell me about mote' in processed_text.lower():
        return "Pratyush/Mote is an heavenly body as well as a black hole as he has his own gravitational field around him\
             \nwhich not only pulls food in his orbit but also consumes it in light speed"
    chat_session = model.start_chat()
    response = chat_session.send_message(processed_text)
    return response.text

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    
    print(f'User:{update.message.chat.full_name} in {message_type}: "{text}"')

    if message_type == 'group' or message_type == 'supergroup':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME,"").strip()
            response: str = handle_responses(new_text)
        else:
            return
    else:
        response: str = handle_responses(text)
    
    print(f"Bot:{response}")
    await update.message.reply_text(response)
    

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")


if __name__ == "__main__":
    print("Starting bot...")
    app = Application.builder().token(TOKEN).build()

    #commands

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    #messages

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #errors
    app.add_error_handler(error)

    #polling
    print("Polling...")
    app.run_polling(poll_interval= 3)