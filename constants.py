CHALLENGE_USER = "CHALLENGE_USER"
ACCEPT_CHALLENGE = "ACCEPT_CHALLENGE"
SEARCH_LADDER = "SEARCH_LADDER"
BOT_MODES = [CHALLENGE_USER, ACCEPT_CHALLENGE, SEARCH_LADDER]
DEFAULT_MODE = "gen7randombattle"

STANDARD_BATTLE = "standard_battle"
RANDOM_BATTLE = "random_battle"

PICK_SAFEST = "safest"
PICK_NASH_EQUILIBRIUM = "nash"

SCORING_MULTIPLIER = "scoring_multiplier"

START_STRING = "|start"
RQID = 'rqid'
TEAM_PREVIEW_POKE = "poke"
START_TEAM_PREVIEW = "|clearpoke"

COMMAND = "!"

MOVES = "moves"
ABILITIES = "abilities"
ITEMS = "items"
COUNT = "count"
SETS = "sets"

UNKNOWN_ITEM = "unknown_item"

UNKOWN_POKEMON_FORMES = ['silvally', 'arceus']

SMOGON_HAS_STATS_PAGE_SUFFIXES = ["ubers", "ou", "uu", "ru", "nu", "pu", "lc", "oublitz"]

# a lookup for the opponent's name given the bot's name
# this has to do with the Pokemon-Showdown PROTOCOL
ID_LOOKUP = {
    "p1": "p2",
    "p2": "p1"
}

# mutator strings
MUTATOR_SWITCH = "switch"
MUTATOR_APPLY_VOLATILE_STATUS = "apply_volatile_status"
MUTATOR_REMOVE_VOLATILE_STATUS = "remove_volatile_status"
MUTATOR_DAMAGE = "damage"
MUTATOR_HEAL = "heal"
MUTATOR_BOOST = "boost"
MUTATOR_UNBOOST = "unboost"
MUTATOR_APPLY_STATUS = "apply_status"
MUTATOR_REMOVE_STATUS = "remove_status"
MUTATOR_SIDE_START = "side_start"
MUTATOR_SIDE_END = "side_end"
MUTATOR_DISABLE_MOVE = "disable_move"
MUTATOR_ENABLE_MOVE = "enable_move"
MUTATOR_WEATHER_START = "weather_start"
MUTATOR_WEATHER_END = "weather_end"
MUTATOR_FIELD_START = "field_start"
MUTATOR_FIELD_END = "field_end"
MUTATOR_TOGGLE_TRICKROOM = "toggle_trickroom"


DAMAGE = 'damage'
HEAL = "heal"
HEAL_TARGET = "heal_target"

BATTLE_TAG = 'battleTag'
FORCE_SWITCH = 'forceSwitch'
WAIT = 'wait'
TRAPPED = "trapped"
MAYBE_TRAPPED = "maybeTrapped"
ITEM = "item"

CONDITION = "condition"
DISABLED = "disabled"
PP = "pp"
CURRENT_PP = 'current_pp'

SELF = "self"
NORMAL = 'normal'
OPPONENT = "opponent"
ALLY_SIDE = "allySide"
ALL_ADJACENT_FOES = "allAdjacentFoes"
FOESIDE = "foeSide"
ALL_ADJACENT = "allAdjacent"
ALL = "all"
RANDOM_NORMAL = "randomNormal"

REFLECTABLE = "reflectable"

FLAGS = 'flags'

MOVE_TARGET_SELF = [SELF, ALLY_SIDE, ALL]
MOVE_TARGET_OPPONENT = [NORMAL, OPPONENT, ALL_ADJACENT, ALL_ADJACENT_FOES, ALL, RANDOM_NORMAL]

DO_NOTHING_MOVE = 'splash'

MOVES = "moves"
ID = "id"
BASESTATS = "baseStats"
LEVEL = "level"
NAME = "name"
STATUS = "status"
TYPES = "types"
TYPE = "type"
BASE_POWER = "basePower"
WEIGHT = "weight"

SIDE = "side"
POKEMON = "pokemon"
FNT = "fnt"

SWITCH_STRING = "switch"
WIN_STRING = "|win|"
CHAT_STRING = "|c|"
TIME_LEFT = "Time left:"
DETAILS = "details"

CAN_MEGA_EVO = "canMegaEvo"
CAN_ULTRA_BURST = "canUltraBurst"
CAN_Z_MOVE = "canZMove"
ZMOVE = "zmove"
ULTRA_BURST = "ultra"
MEGA = "mega"

ACTIVE = "active"
RESERVE = "reserve"
SIDE_CONDITIONS = "side_conditions"
WEATHER = "weather"
FIELD = "field"

PRIORITY = "priority"
STATS = "stats"
MAXHP = "maxhp"
BOOSTS = "boosts"
TARGET = "target"

HITPOINTS = "hp"
ATTACK = "attack"
DEFENSE = "defense"
SPECIAL_ATTACK = "special-attack"
SPECIAL_DEFENSE = "special-defense"
SPEED = "speed"
ACCURACY = "accuracy"
EVASION = "evasion"

ATTACK_BOOST = "attack_boost"
DEFENSE_BOOST = "defense_boost"
SPECIAL_ATTACK_BOOST = "special_attack_boost"
SPECIAL_DEFENSE_BOOST = "special_defense_boost"
SPEED_BOOST = "speed_boost"
ACCURACY_BOOST = "accuracy_boost"
EVASION_BOOST = "evasion_boost"

ABILITY = 'ability'
REQUEST_DICT_ABILITY = ABILITY
MOST_LIKELY_ABILITY = 'most_likely_ability'

MAX_BOOSTS = 6

STAT_ABBREVIATION_LOOKUPS = {
    "atk": ATTACK,
    "def": DEFENSE,
    "spa": SPECIAL_ATTACK,
    "spd": SPECIAL_DEFENSE,
    "spe": SPEED,
    "accuracy": ACCURACY,
    "evasion": EVASION
}

STAT_STRINGS = [ATTACK, DEFENSE, SPECIAL_ATTACK, SPECIAL_DEFENSE, SPEED]

HIDDEN_POWER = 'hiddenpower'
HIDDEN_POWER_TYPE_STRING_INDEX = -1
HIDDEN_POWER_ACTIVE_MOVE_BASE_DAMAGE_STRING = "60"
HIDDEN_POWER_RESERVE_MOVE_BASE_DAMAGE_STRING = ""

FAINTED = "dead"

PHYSICAL = "physical"
SPECIAL = "special"
CATEGORY = "category"

DAMAGING_CATEGORIES = [PHYSICAL, SPECIAL]

CRASH = "crash"
RECOIL = "recoil"
DRAIN = "drain"
CONTACT = "contact"
CHARGE = "charge"
POWDER = "powder"
DRAG = "drag"
SOUND = "sound"

VOLATILE_STATUS = "volatileStatus"
SECONDARY = "secondary"
CHANCE = "chance"
LOCKED_MOVE = "lockedmove"

# Side-Effects
REFLECT = 'reflect'
LIGHT_SCREEN = 'lightscreen'
AURORA_VEIL = 'auroraveil'
SAFEGUARD = 'safeguard'
TAILWIND = 'tailwind'
STICKY_WEB = 'stickyweb'
WISH = "wish"
HEALING_WISH = 'healingwish'

# weather
RAIN = "raindance"
SUN = "sunnyday"
SAND = "sandstorm"
HAIL = "hail"
DESOLATE_LAND = "desolateland"
HEAVY_RAIN = "primordialsea"

IRREVERSIBLE_WEATHER = {DESOLATE_LAND, HEAVY_RAIN}

# Hazards
STEALTH_ROCK = 'stealthrock'
SPIKES = 'spikes'
TOXIC_SPIKES = 'toxicspikes'

HAZARD_CLEARING_MOVES = ['rapidspin', 'defog']

RAPID_SPIN_CLEARS = [
    STEALTH_ROCK,
    SPIKES,
    TOXIC_SPIKES,
    STICKY_WEB,
]

DEFOG_CLEARS = [
    STEALTH_ROCK,
    SPIKES,
    TOXIC_SPIKES,
    STICKY_WEB,
    REFLECT,
    LIGHT_SCREEN,
    AURORA_VEIL
]

TRICK_ROOM = "trickroom"

TERRAIN = "terrain"
ELECTRIC_TERRAIN = "electricterrain"
GRASSY_TERRAIN = "grassyterrain"
MISTY_TERRAIN = "mistyterrain"
PSYCHIC_TERRAIN = "psychicterrain"

# switch-out moves
SWITCH_OUT_MOVES = {"uturn", "voltswitch", "partingshot"}

# volatile statuses
FLINCH = "flinch"
CONFUSION = "confusion"
LEECH_SEED = "leechseed"
SUBSTITUTE = "substitute"
TAUNT = "taunt"
ROOST = "roost"
PROTECT = "protect"
BANEFUL_BUNKER = "banefulbunker"
SPIKY_SHIELD = "spikyshield"

PROTECT_VOLATILE_STATUSES = [PROTECT, BANEFUL_BUNKER, SPIKY_SHIELD]

# non-volatile statuses
SLEEP = "slp"
BURN = "brn"
FROZEN = "frz"
PARALYZED = "par"
POISON = "psn"
TOXIC = "tox"
TOXIC_COUNT = "toxic_count"
NON_VOLATILE_STATUSES = {SLEEP, BURN, FROZEN, PARALYZED, POISON, TOXIC}

# chances to break out of non-volatile statuses
WAKE_UP_PERCENT = 0.33
THAW_PERCENT = 0.20
FULLY_PARALYZED_PERCENT = 0.25

THAW_IF_USES = {'scald', 'flamewheel', 'sacredfire', 'flareblitz', 'fusionflare', 'steameruption'}
THAW_IF_HIT_BY = {'scald', 'steameruption'}

IMMUNE_TO_SLEEP_ABILITIES = {'insomnia', 'sweetveil', 'vitalspirit'}
IMMUNE_TO_BURN_ABILITIES = {'waterveil', 'waterbubble'}
IMMUNE_TO_FROZEN_ABILITIES = {'magmaarmor'}
IMMUNE_TO_POISON_ABILITIES = {'immunity'}
IMMUNE_TO_PARALYSIS_ABILITIES = {'limber'}

CHOICE_ITEMS = {'choicescarf', 'choiceband', 'choicespecs'}
