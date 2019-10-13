from environs import Env
import asyncio
import constants
import config
import threading
import concurrent.futures
from config import logger

from data.mods.apply_mods import apply_mods

from teams import load_team
from showdown.battle import Battle
from showdown.run_battle import pokemon_battle
from showdown.run_battle import initialize_battle
from showdown.run_battle import run_start_random_battle
from showdown.run_battle import run_start_standard_battle
from showdown.websocket_client import PSWebsocketClient

import json
from data import all_move_json
from data import pokedex
from copy import deepcopy


def thr(ps_websocket_client, msg, battles):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(parse_message(ps_websocket_client, msg, battles))
    loop.close()


async def showdown():
    env = Env()
    env.read_env()
    config.log_to_file = env.bool("LOG_TO_FILE", config.log_to_file)
    config.save_replay = env.bool("SAVE_REPLAY", config.save_replay)
    config.decision_method = env("DECISION_METHOD", config.decision_method)
    config.use_relative_weights = env.bool("USE_RELATIVE_WEIGHTS", config.use_relative_weights)
    config.gambit_exe_path = env("GAMBIT_PATH", config.gambit_exe_path)
    config.search_depth = int(env("MAX_SEARCH_DEPTH", config.search_depth))
    config.greeting_message = env("GREETING_MESSAGE", config.greeting_message)
    config.battle_ending_message = env("BATTLE_OVER_MESSAGE", config.battle_ending_message)
    logger.setLevel(env("LOG_LEVEL", "DEBUG"))
    websocket_uri = env("WEBSOCKET_URI", "sim.smogon.com:8000")
    username = env("PS_USERNAME")
    password = env("PS_PASSWORD", "")
    bot_mode = env("BOT_MODE")
    team_name = env("TEAM_NAME", None)
    pokemon_mode = env("POKEMON_MODE", constants.DEFAULT_MODE)

    apply_mods(pokemon_mode)
    original_pokedex = deepcopy(pokedex)
    original_move_json = deepcopy(all_move_json)

    ps_websocket_client = await PSWebsocketClient.create(username, password, websocket_uri)
    await ps_websocket_client.login()

    battles = []
    for i in range(5):
        battles.append(Battle('empty'))

    while True:
        msg = await ps_websocket_client.receive_message()

        """ loop = asyncio.get_event_loop()
        t = threading.Thread(target = thr, args=(ps_websocket_client, msg, battles))
        t.start() """

        await parse_message(ps_websocket_client, msg, battles)


async def parse_message(ps_websocket_client, msg, battles):
    split_msg = msg.split('|')

    if split_msg[1].strip() == 'updatechallenges':
        await ps_websocket_client.accept_challenge(split_msg, battles)
        return

    if split_msg[1].strip() == 'init' and split_msg[2].strip() == 'battle':
        battle = None
        for curr in battles:
            if curr.battle_tag == 'pending':
                battle = curr
                battle.battle_tag = split_msg[0].replace('>', '').strip()
                user_name = split_msg[-1].replace('☆', '').strip()
                battle.opponent.account_name = split_msg[4].replace(user_name, '').replace('vs.', '').strip()
                battle.opponent.name = 'pending'
                break
        if battle == None:
            logger.debug("ERROR: can't find pending slot")
        return

    if 'battle' in split_msg[0]:
        battle = None
        i = 0
        for curr in battles:
            if curr.battle_tag == split_msg[0].replace('>', '').strip():
                battle = curr
                break
            i += 1
        if battle == None:
            logger.debug("ERROR: can't find battle slot")
            return
        if battle.opponent.name == 'pending':
            await initialize_battle(ps_websocket_client, battle, split_msg)
        elif battle.started == False:
            if battle.battle_type == constants.STANDARD_BATTLE:
                await run_start_standard_battle(ps_websocket_client, battle, msg)
                return
            else:
                await run_start_random_battle(ps_websocket_client, battle, msg)
                return
        else:
            ended = await pokemon_battle(ps_websocket_client, battle, msg)
            if(ended):
                battles[i] = Battle('empty')
            return

    if split_msg[1].strip() == 'pm' and '$' in split_msg[4]:
        await ps_websocket_client.parse_command(split_msg, battles)
        return



if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(showdown())
