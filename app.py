from __future__ import division
from flask import Flask, render_template, request, redirect, url_for
import random
import json

app = Flask(__name__)

url = "/var/www/league/html/AbilityPoro/"

# url = ""

@app.route("/")
def index():
    championList = get_champion_ids()
    championIcons = []
    championIds = {}
    for key in championList:
        championIds[championList[key]] = key
        championIcons.append(championList[key])
    championIcons.sort()
    with open(url + 'static/data/5.11Champions.json') as f:
        before = json.load(f)
    with open(url + 'static/data/5.14Champions.json') as f:
        after = json.load(f)
    return render_template('index.html', champions=championIcons, championIds=championIds, before=before , after=after)

@app.route("/<championName>")
def show_champion_details(championName):
    championList = get_champion_ids()
    championIds = {}
    for key in championList:
        championIds[championList[key]] = key
    with open('static/data/5.11Champions.json') as f:
        before = json.load(f)
    with open('static/data/5.14Champions.json') as f:
        after = json.load(f)
    itemNames = get_item_ids()
    for champion in before:
        items = []
        for item in before[champion]['items']:
            if len(items) == 0:
                items.append(item)
            else:
                thing = False
                for i in range(len(items)):
                    if before[champion]['items'][item] > before[champion]['items'][items[i]]:
                        items.insert(i, item)
                        thing = True
                        break
                if not thing:
                    items.append(item)
        print(items)
        before[champion]['itemsSorted'] = items
    for champion in after:
        items = []
        for item in after[champion]['items']:
            if len(items) == 0:
                items.append(item)
            else:
                thing = False
                for i in range(len(items)):
                    if after[champion]['items'][item] > after[champion]['items'][items[i]]:
                        items.insert(i, item)
                        thing = True
                        break
                if not thing:
                    items.append(item)
        print(items)
        after[champion]['itemsSorted'] = items
    return render_template('champion.html', championName=championName, championIds=championIds, itemNames=itemNames, before=before , after=after)

@app.route("/items")
def items():
    itemList = get_item_ids()
    itemNames = []
    for key in itemList:
        itemNames.append(itemList[key])
    itemNames.sort()
    itemDict = {}
    for itemId in itemList:
        itemDict[itemList[itemId]] = itemId
    return render_template('items.html', itemNames=itemNames, itemDict=itemDict)

def get_champion_ids():
    return {1: 'Annie', 2: 'Olaf', 3: 'Galio', 4: 'TwistedFate', 5: 'XinZhao', 6: 'Urgot', 7: 'Leblanc',
    8: 'Vladimir', 9: 'FiddleSticks', 266: 'Aatrox', 267: 'Nami', 268: 'Azir', 13: 'Ryze', 14: 'Sion',
    15: 'Sivir', 16: 'Soraka', 17: 'Teemo', 18: 'Tristana', 19: 'Warwick', 20: 'Nunu', 21: 'MissFortune',
    22: 'Ashe', 23: 'Tryndamere', 24: 'Jax', 25: 'Morgana', 26: 'Zilean', 27: 'Singed', 28: 'Evelynn',
    29: 'Twitch', 30: 'Karthus', 31: 'Chogath', 32: 'Amumu', 33: 'Rammus', 34: 'Anivia', 35: 'Shaco',
    36: 'DrMundo', 37: 'Sona', 38: 'Kassadin', 39: 'Irelia', 40: 'Janna', 41: 'Gangplank', 42: 'Corki',
    43: 'Karma', 44: 'Taric', 45: 'Veigar', 48: 'Trundle', 50: 'Swain', 51: 'Caitlyn', 53: 'Blitzcrank',
    54: 'Malphite', 55: 'Katarina', 56: 'Nocturne', 57: 'Maokai', 58: 'Renekton', 59: 'JarvanIV', 60:
    'Elise', 10: 'Kayle', 62: 'Wukong', 63: 'Brand', 64: 'LeeSin', 67: 'Vayne', 68: 'Rumble', 69:
    'Cassiopeia', 72: 'Skarner', 12: 'Alistar', 74: 'Heimerdinger', 75: 'Nasus', 76: 'Nidalee', 77: 'Udyr',
    78: 'Poppy', 79: 'Gragas', 11: 'MasterYi', 81: 'Ezreal', 82: 'Mordekaiser', 83: 'Yorick', 84: 'Akali',
    85: 'Kennen', 86: 'Garen', 89: 'Leona', 90: 'Malzahar', 91: 'Talon', 92: 'Riven', 96: 'KogMaw',
    98: 'Shen', 99: 'Lux', 101: 'Xerath', 102: 'Shyvana', 103: 'Ahri', 104: 'Graves', 105: 'Fizz',
    106: 'Volibear', 107: 'Rengar', 110: 'Varus', 61: 'Orianna', 112: 'Viktor', 113: 'Sejuani',
    114: 'Fiora', 115: 'Ziggs', 117: 'Lulu', 119: 'Draven', 120: 'Hecarim', 121: 'Khazix', 122: 'Darius',
    126: 'Jayce', 127: 'Lissandra', 131: 'Diana', 133: 'Quinn', 134: 'Syndra', 143: 'Zyra', 150: 'Gnar',
    154: 'Zac', 111: 'Nautilus', 412: 'Thresh', 157: 'Yasuo', 161: 'Velkoz', 421: 'RekSai', 429: 'Kalista',
    432: 'Bard', 201: 'Braum', 222: 'Jinx', 80: 'Pantheon', 236: 'Lucian', 238: 'Zed', 245: 'Ekko', 254: 'Vi',
    223: 'TahmKench'}

def get_item_ids():
    return {3072: 'The Bloodthirster', 2049: 'Sightstone', 2050: "Explorer's Ward", 3075: 'Thornmail',
    1029: 'Cloth Armor', 3078: 'Trinity Force', 1031: 'Chain Vest', 1033: 'Null-Magic Mantle',
    3082: "Warden's Mail", 3083: "Warmog's Armor", 1036: 'Long Sword', 1037: 'Pickaxe', 1038: 'B. F. Sword',
    3599: 'The Black Spear', 3089: "Rabadon's Deathcap", 1042: 'Dagger', 1043: 'Recurve Bow',
    3092: "Frost Queen's Claim", 3093: 'Avarice Blade', 3096: "Nomad's Medallion",
    1028: 'Ruby Crystal', 3098: 'Frostfang', 1051: "Brawler's Gloves", 1052: 'Amplifying Tome',
    1053: 'Vampiric Scepter', 1054: "Doran's Shield", 2053: 'Raptor Cloak', 1056: "Doran's Ring",
    1057: 'Negatron Cloak', 1058: 'Needlessly Large Rod', 3108: 'Fiendish Codex', 3110: 'Frozen Heart',
    3111: "Mercury's Treads", 3087: 'Statikk Shiv', 3113: 'Aether Wisp',
    3114: 'Forbidden Idol', 3115: "Nashor's Tooth", 3116: "Rylai's Crystal Scepter", 3117: 'Boots of Mobility',
    3124: "Guinsoo's Rageblade", 3086: 'Zeal', 3134: 'The Brutalizer', 3135: 'Void Staff', 3136: 'Haunting Guise',
    3139: 'Mercurial Scimitar', 3140: 'Quicksilver Sash', 3141: 'Sword of the Occult', 3142: "Youmuu's Ghostblade",
    3143: "Randuin's Omen", 3144: 'Bilgewater Cutlass', 3145: 'Hextech Revolver', 3146: 'Hextech Gunblade',
    3085: "Runaan's Hurricane (Ranged Only)", 3152: 'Will of the Ancients', 3153: 'Blade of the Ruined King',
    3155: 'Hexdrinker', 3156: 'Maw of Malmortius', 3157: "Zhonya's Hourglass", 3158: 'Ionian Boots of Lucidity',
    2137: 'Elixir of Ruin', 2138: 'Elixir of Iron', 2139: 'Elixir of Sorcery', 2140: 'Elixir of Wrath',
    3165: 'Morellonomicon', 1026: 'Blasting Wand', 3172: 'Zephyr',
    3174: "Athene's Unholy Grail", 3091: "Wit's End", 3190: 'Locket of the Iron Solari', 3191: "Seeker's Armguard",
    3706: "Stalker's Blade", 3707: 'Enchantment: Warrior', 3708: 'Enchantment: Magus', 3709: 'Enchantment: Cinderhulk',
    3198: 'Perfect Hex Core', 3711: "Poacher's Knife", 3200: 'Prototype Hex Core', 3713: "Ranger's Trailblazer",
    3714: 'Enchantment: Warrior', 3715: "Skirmisher's Sabre", 3716: 'Enchantment: Magus',
    3717: 'Enchantment: Cinderhulk', 3718: 'Enchantment: Devourer', 3719: 'Enchantment: Warrior',
    3720: 'Enchantment: Magus', 3721: 'Enchantment: Cinderhulk', 3722: 'Enchantment: Devourer',
    3211: "Spectre's Cowl", 3724: 'Enchantment: Magus', 3725: 'Enchantment: Cinderhulk',
    3726: 'Enchantment: Devourer', 3222: "Mikael's Crucible", 3097: "Targon's Brace",
    3074: 'Ravenous Hydra (Melee Only)', 3751: "Bami's Cinder", 3100: 'Lich Bane',
    3101: 'Stinger', 1055: "Doran's Blade", 3105: 'Aegis of the Legion', 3285: "Luden's Echo",
    3800: 'Righteous Glory', 3801: 'Crystalline Bracer',
    3301: 'Ancient Coin', 3302: 'Relic Shield', 3303: "Spellthief's Edge", 3196: 'The Hex Core mk-1',
    3197: 'The Hex Core mk-2', 3027: 'Rod of Ages', 3710: 'Enchantment: Devourer', 3028: 'Chalice of Harmony',
    3077: 'Tiamat (Melee Only)', 3031: 'Infinity Edge',
    3723: 'Enchantment: Warrior', 3401: 'Face of the Mountain', 3050: "Zeke's Herald", 1027: 'Sapphire Crystal',
    3151: "Liandry's Torment", 3504: 'Ardent Censer', 3508: 'Essence Reaver', 3512: "Zz'Rot Portal",
    3001: 'Abyssal Scepter', 3003: "Archangel's Staff", 3004: 'Manamune', 3006: "Berserker's Greaves",
    3009: 'Boots of Swiftness', 3010: 'Catalyst the Protector', 3020: "Sorcerer's Shoes", 3022: 'Frozen Mallet',
    3023: 'Twin Shadows', 3024: 'Glacial Shroud', 3025: 'Iceborn Gauntlet', 3026: 'Guardian Angel',
    2003: 'Health Potion', 2004: 'Mana Potion', 3065: 'Spirit Visage', 2010: 'Total Biscuit of Rejuvenation',
    3035: 'Last Whisper', 3040: "Seraph's Embrace",
    3041: "Mejai's Soulstealer", 3042: 'Muramana', 2043: 'Vision Ward', 3044: 'Phage', 3046: 'Phantom Dancer',
    3047: 'Ninja Tabi', 1039: "Hunter's Machete", 1001: 'Boots of Speed', 3102: "Banshee's Veil",
    1004: 'Faerie Charm', 3068: 'Sunfire Cape', 1006: 'Rejuvenation Bead', 2045: 'Ruby Sightstone',
    3056: 'Ohmwrecker', 3057: 'Sheen', 1011: "Giant's Belt", 3060: 'Banner of Command', 2041: 'Crystalline Flask',
    1018: 'Cloak of Agility', 3067: 'Kindlegem', 2044: 'Stealth Ward', 3069: 'Talisman of Ascension',
    3070: 'Tear of the Goddess', 3071: 'The Black Cleaver'}

app.jinja_env.globals.update(get_champion_ids=get_champion_ids)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=1337)
