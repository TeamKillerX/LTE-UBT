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


import logging
import asyncio
import time as tme
from pyrogram import *
from config import *
from pyrogram.errors import AuthKeyDuplicated
from userbot_auth import UserbotAuth

ubt = UserbotAuth(
    url="https://ubt.ryzenths.dpdns.org",
    secret=os.getenv("UBT_SECRET"),
    token="prov_tok_free",
    strict=True
)

class LteUBtUser(Client):
    def __init__(self):
        super().__init__(
            "LTEUser",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION_STRING,
            plugins=dict(root="LTE-UBT.plugins"),
            workers=8,
        )
        self.logger = logging.getLogger("LTE-UBT")
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler("LTE-UBT.log", encoding="utf-8")
        handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        self.logger.addHandler(handler)
        self.logger.info("User started")
        self.me = None
    
    async def start(self, *args, **kwargs):
        await super().start()
        self.logger.info("User now started")
        self.me = await self.get_me()
        await ubt.client_authorized(self_client=self, self_me=self.me)
        self.logger.info("Created health successfully")
        self.logger.info("Logged in as %s (%s)", self.me.first_name, self.me.id)
        self.logger.info("Created devices safety successfully")
        
    async def stop(self, *args, **kwargs):
        await super().stop()
        self.logger.info("User stopped")
        self.logger.info("Goodbye!")
        await asyncio.sleep(1)

def basis_config_enabled():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("lte.log", encoding="utf-8"),
            logging.StreamHandler()
        ]
    )
    logging.getLogger("asyncio").setLevel(logging.WARNING)
    logging.getLogger("pyrogram").setLevel(logging.WARNING)

async def shutdown():
    logging.info("Shutting down Ryzenth...")
    await asyncio.sleep(0.1)
    logging.info("Shutdown complete.")

def main_core_run():
    try:
        asyncio.run(fast_start())
    except KeyboardInterrupt:
        logging.info("KeyboardInterrupt received. Stopping Ryzenth...")
        asyncio.run(shutdown())
    except Exception as e:
        logging.error(f"Fatal Error: {e}")
        asyncio.run(shutdown())

async def _startup_start():
    try:
        start_time = tme.perf_counter()
        lte_user = LteUBtUser()

        async def start_user():
            try:
                await lte_user.start()
            except AuthKeyDuplicated:
                logging.error("Userbot AuthKeyDuplicated")
                raise
        await asyncio.gather(start_user())
        end_time = tme.perf_counter()
        logging.info(f"[BENCHMARK SPEED] deployed in {end_time - start_time:.2f}s")
        await idle()

    except Exception as e:
        logging.error(f"Error: {type(e).__name__} {str(e)}")

lte_user = LteUBtUser()
