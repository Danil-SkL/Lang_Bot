from aiogram import Bot, Dispatcher, executor, types
from ButtonBot import *
from aiogram.dispatcher.filters.state import StatesGroup, State


TOKEN_API = '6129891753:AAFbKG74I07eZG1dfVffC-bgPtDs1_LilWM'


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


class NewWordState(StatesGroup):

    decision = State()


async def on_startup(_):
    await db_connect()
    print('Подключение завершенно!')


@dp.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Главное меню бота',
                           reply_markup=MainMenu())
    await message.delete()


@dp.callback_query_handler(text='id_back')
async def cmd_back(call):
    await call.message.answer(text='Главное меню',
                              reply_markup=MainMenu())
    await call.message.delete()


@dp.callback_query_handler(text='id_word')
async def cmd_word(call):
    await call.message.answer(text='Меню слов',
                              reply_markup=WordMenu())
    await call.message.delete()


@dp.callback_query_handler(text='id_new_word')
async def cmd_mew_word(call):
    await call.message.answer(text='Здесь вы изучаете новые слова',
                              reply_markup=NewWord())
    await call.message.delete()


@dp.callback_query_handler(text='id_start_word')
async def cmd_start_word(call):
    global word
    word = await get_ten_words()
    await call.message.answer(text=f'{word[0]} - {word[1]}, знакомо ли вам это слово?',
                                reply_markup=yes_or_not())
    await call.message.delete()


@dp.callback_query_handler(text='id_yes')
async def cmd_yes(call):
    await call.message.answer(text='Отлично!',
                              reply_markup=continue_yes_or_not())
    await add_in_repetititon(word)
    await del_wrd(word)
    await call.message.delete()


@dp.callback_query_handler(text='id_no')
async def cmd_yes(call):
    await call.message.answer(text='Слово повториться!',
                              reply_markup=continue_yes_or_not())
    await call.message.delete()


@dp.callback_query_handler(text='id_proposal')
async def cmd_new_proposal(call):
    await call.message.answer(text='Здесь вы изучаете слова с помощью предложений',
                              reply_markup=new_proposal())
    await call.message.delete()
    

@dp.callback_query_handler(text='id_repetition')
async def cmd_repetition(call):
    await call.message.answer(text='Здесь вы повторяете пройденные слова',
                              reply_markup=repetition_word())
    await call.message.delete()


@dp.callback_query_handler(text='id_start_repetition')
async def cmd_repetition(call):
    rep_wrd = await get_repetition_words()
    if rep_wrd == '0':
        await call.message.answer(text='Этот список пока пуст.',
                                  reply_markup=continue_repetition())
        await call.message.delete()
    else:
        await call.message.answer(text=f'{rep_wrd[0]} - {rep_wrd[1]}, помните ли вы это слово?',
                                  reply_markup=continue_repetition())
        await call.message.delete()


if __name__=='__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)