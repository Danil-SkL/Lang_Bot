from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from LangSQLite import *


def MainMenu():
    menu = InlineKeyboardMarkup(row_width=2)
    menu1 = InlineKeyboardButton(text='Слова', callback_data='id_word')
    menu2 = InlineKeyboardButton(text='Правила', callback_data='id_rules')
    return menu.add(menu1, menu2)


def WordMenu():
    menu = InlineKeyboardMarkup(row_width=1)
    menu1 = InlineKeyboardButton(text='Новые слова', callback_data='id_new_word')
    menu2 = InlineKeyboardButton(text='Предложения', callback_data='id_proposal')
    menu3 = InlineKeyboardButton(text='Повторение слов', callback_data='id_repetition')
    menu4 = InlineKeyboardButton(text='<<', callback_data='id_back')
    return menu.add(menu1, menu2, menu3, menu4)


def NewWord():
    menu = InlineKeyboardMarkup(row_width=1)
    menu1 = InlineKeyboardButton(text='Начать', callback_data='id_start_word')
    menu2 = InlineKeyboardButton(text='<<', callback_data='id_word')
    return menu.add(menu1, menu2)


def new_proposal():
    menu = InlineKeyboardMarkup(row_width=1)
    menu1 = InlineKeyboardButton(text='Начать', callback_data='id_start_proposal')
    menu2 = InlineKeyboardButton(text='<<', callback_data='id_word')
    return menu.add(menu1, menu2)


def repetition_word():
    menu = InlineKeyboardMarkup(row_width=1)
    menu1 = InlineKeyboardButton(text='Начать', callback_data='id_start_repetition')
    menu2 = InlineKeyboardButton(text='<<', callback_data='id_word')
    return menu.add(menu1, menu2)


def yes_or_not():
    menu = InlineKeyboardMarkup(row_width=2)
    menu1 = InlineKeyboardButton(text='Yes', callback_data='id_yes')
    menu2 = InlineKeyboardButton(text='No', callback_data='id_no')
    return menu.add(menu1, menu2)

def continue_yes_or_not():
    menu = InlineKeyboardMarkup(row_width=2)
    menu1 = InlineKeyboardButton(text='Продолжить', callback_data='id_start_word')
    menu2 = InlineKeyboardButton(text='Вернутся в главное меню', callback_data='id_back')
    return menu.add(menu1, menu2)


def continue_repetition():
    menu = InlineKeyboardMarkup(row_width=2)
    menu1 = InlineKeyboardButton(text='Продолжить', callback_data='id_start_repetition')
    menu2 = InlineKeyboardButton(text='Вернуться в главное меню.', callback_data='id_back')
    return menu.add(menu1, menu2)


def get_rule_menu():
    menu = InlineKeyboardMarkup(row_width=1)
    menu1 = InlineKeyboardButton(text='Основные правила языка.', callback_data='id_basic_rule')
    menu2 = InlineKeyboardButton(text='Правила существительных.', callback_data='id_rules_nouns')
    menu3 = InlineKeyboardButton(text='Прилогательное.', callback_data='id_ajectiv')
    menu4 = InlineKeyboardButton(text='Вернутся в главное меню.', callback_data='id_back')
    return menu.add(menu1, menu2, menu3, menu4)

def basic_rule():
    menu = InlineKeyboardMarkup(row_width=1)
    menu1 = InlineKeyboardButton(text='Правило1', callback_data='id_rule1')
    menu2 = InlineKeyboardButton(text='Правило2', callback_data='id_rule2')
    menu3 = InlineKeyboardButton(text='Правило3', callback_data='id_rule3')
    menu4 = InlineKeyboardButton(text='Правило4', callback_data='id_rule4')
    menu5 = InlineKeyboardButton(text='Вернутся в главное меню.', callback_data='id_back')
    menu6 = InlineKeyboardButton(text='<<', callback_data='id_rules')
    return menu.add(menu1, menu2, menu3, menu4, menu5, menu6)


def rule_menu():
    menu = InlineKeyboardMarkup(row_width=1)
    menu1 = InlineKeyboardButton(text='<<', callback_data='id_basic_rule')
    return menu.add(menu1)
