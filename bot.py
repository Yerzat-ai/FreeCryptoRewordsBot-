import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.enums import ParseMode
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()


# -------- START BUTTON --------
@dp.message(F.text == "/start")
async def start_message(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="START",
                    callback_data="open_menu"
                )
            ]
        ]
    )

    await message.answer(
        "<b>Welcome to the Free Crypto Rewards Bot! 💸</b>\nEarn crypto by completing simple tasks!",
        reply_markup=keyboard
    )


# -------- OPEN MAIN MENU --------
@dp.callback_query(F.data == "open_menu")
async def open_main_menu(callback):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="▶ PLAY", callback_data="play")],
            [InlineKeyboardButton(text="Join Community", url="https://t.me/your_channel_here")]
        ]
    )

    await callback.message.answer_photo(
        photo="https://i.imgur.com/8N9QyEo.jpeg",  # кейін Pepe+Notcoin суретін ауыстырамыз
        caption="Earn Pepe & Notcoin by completing tasks!",
        reply_markup=keyboard
    )


# -------- PLAY OPEN FULLSCREEN MENU --------
@dp.callback_query(F.data == "play")
async def open_fullscreen_menu(callback):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📝 Tasks", callback_data="tasks"),
                InlineKeyboardButton(text="👥 Invite", callback_data="invite")
            ],
            [
                InlineKeyboardButton(text="💼 Wallet", callback_data="wallet"),
                InlineKeyboardButton(text="💳 Withdraw", callback_data="withdraw")
            ]
        ]
    )

    await callback.message.answer(
        "<b>Main Menu</b>\nChoose an option below:",
        reply_markup=keyboard
    )


# --- TEMP EMPTY HANDLERS (толық нұсқасын келесі қадамда қосамыз) ---

@dp.callback_query(F.data == "tasks")
async def tasks_menu(callback):
    await callback.message.answer("📝 Tasks menu (coming next step!)")

@dp.callback_query(F.data == "invite")
async def invite_menu(callback):
    await callback.message.answer("👥 Invite menu (coming next step!)")

@dp.callback_query(F.data == "wallet")
async def wallet_menu(callback):
    await callback.message.answer("💼 Wallet menu (coming next step!)")

@dp.callback_query(F.data == "withdraw")
async def withdraw_menu(callback):
    await callback.message.answer("💳 Withdraw menu (coming next step!)")


# -------- BOT LAUNCH --------
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
