import sqlite3 as sq
import random


async def db_connect():
    global db, cur

    db = sq.connect('Lang.db')
    cur = db.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS word(id INTEGER PRIMARY KEY AUTOINCREMENT, 
                title TEXT, designation TEXT)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS word_repetition(id INTEGER, 
                title TEXT, designation TEXT)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS rules(id INT, 
                title TEXT, designation TEXT)''')

    db.commit()


async def get_ten_words():
    res = cur.execute('SELECT * FROM word').fetchall()
    
    if len(res)>0:
        wrd = random.choice(res)
    else:
        wrd = '0'

    return wrd


async def get_repetition_words():
    res = cur.execute('SELECT * FROM word_repetition').fetchall()
    
    if len(res)>0:
        wrd = random.choice(res)
    else:
        wrd = '0'

    return wrd


async def add_in_repetititon(n_word):
    cur.execute('INSERT INTO word_repetition(id, title, designation) VALUES(?, ?, ?)', n_word)

    db.commit()


async def del_wrd(word):
    cur.execute(f'DELETE FROM word WHERE id={word[0]}')

    db.commit()

def get_title_prop():
    rules = cur.execute('SELECT * FROM rules').fetchall()

    if len(rules)>0:
        return rules
    else:
        return "Правил пока нет."
    

def get_rule(int):
    return cur.execute(f'SELECT * FROM rules WHERE id = {int}').fetchall()