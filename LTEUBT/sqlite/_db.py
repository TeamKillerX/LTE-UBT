#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2019-2026 (c) Randy W @xtdevs, @xtsea
#
# from : https://github.com/TeamKillerX
# Channel : @RendyProjects
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import aiosqlite

DB_PATH = "lte.db"

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS prefixes (
                user_id INTEGER PRIMARY KEY,
                prefix TEXT NOT NULL
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS afk (
                user_id INTEGER PRIMARY KEY,
                afk_time TEXT NOT NULL,
                afk_reason TEXT NOT NULL,
                is_afk INTEGER NOT NULL DEFAULT 1
            )
        """)
        await db.commit()

async def set_afk_in_db(user_id: int, afk_time: str, afk_reason: str, is_afk: bool):
    async with aiosqlite.connect(DB_PATH, timeout=10) as db:
        await db.execute("""
            INSERT INTO afk (user_id, afk_time, afk_reason, is_afk)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(user_id) DO UPDATE SET
                afk_time=excluded.afk_time,
                afk_reason=excluded.afk_reason,
                is_afk=excluded.is_afk
        """, (user_id, afk_time, afk_reason, int(is_afk)))
        await db.commit()
        return True

async def is_afk(user_id: int) -> bool:
    async with aiosqlite.connect(DB_PATH, timeout=10) as db:
        cursor = await db.execute(
            "SELECT is_afk FROM afk WHERE user_id=?",
            (user_id,)
        )
        row = await cursor.fetchone()
        await cursor.close()
        return bool(row[0]) if row else False

async def set_prefix_in_db(user_id: int, prefix: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
            INSERT INTO prefixes (user_id, prefix)
            VALUES (?, ?)
            ON CONFLICT(user_id) DO UPDATE SET prefix=excluded.prefix
        ''', (user_id, prefix))
        await db.commit()

async def get_prefix(user_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute('SELECT prefix FROM prefixes WHERE user_id=?', (user_id,))
        result = await cursor.fetchone()
        return result[0] if result else None
