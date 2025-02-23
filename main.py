import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.bot import DefaultBotProperties

import config
from handlers import router

async def main():
    bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    db = Dispatcher(storage=MemoryStorage())
    db.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await db.start_polling(bot, allowed_updates=db.resolve_used_update_types())

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
