from aiogram import types, Dispatcher
from create_bot import BOT

from key_and_keyboards import *


# ответ на запуск бота
# @DP.message_handler(commands=['start'])
#async def command_start(message: types.Message, state: FSMContext):
async def command_start(message: types.Message):

    #await FSM_states.state_main.set()
    await BOT.send_message(message.chat.id,\
                           'Приветствую!',
                           reply_markup=kb_start)



# регистрация всех хэндлеров в отдельной ф-ии
# чтобы потом передать именно ее в нужное место
def register_handlers_main(DP: Dispatcher):
	'''
    DP.register_message_handler(command_start, commands=['start'], state='*')
    DP.register_callback_query_handler(callback_button_map, text='map', state='*')
    DP.register_callback_query_handler(callback_button_poisk, text='poisk', state=[FSM_states.state_main, FSM_states.state_map])
    DP.register_callback_query_handler(callback_button_cat, text=cat_lst, state=FSM_states.state_category)
	'''
	DP.register_message_handler(command_start, commands=['start'])