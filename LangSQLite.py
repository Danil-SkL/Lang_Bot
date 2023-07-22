import sqlite3 as sq
import random


async def db_connect():
    global db, cur

    db = sq.connect('Lang.db')
    cur = db.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS word(title, designation)')
    cur.execute('CREATE TABLE IF NOT EXISTS word_repetition(title, designation)')

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
    cur.execute('INSERT INTO word_repetition(title, designation) VALUES(?, ?)', n_word)

    db.commit()


async def del_wrd(word):
    cur.execute('DELETE FROM word WHERE title=(?, ?)', (str(word[0]), str(word[1])))

    db.commit()