from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.indomie(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Kenalin Nama Gua Indomie`")
    sleep(3)
    await typew.edit("`1 Abad`")
    sleep(1)
    await typew.edit("`Lacak IP Gua AJa Klo Mau Tau Gua Tinggal Di Daerah Mana`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(1)
    await typew.edit("`I LOVE YOU π`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Depresi`")
    sleep(3)
    await typew.edit("`Jangan Pernah Bersyukur`")
    sleep(1)
    await typew.edit("`Dan Selalu Insecure`")
# Create by myself @localheart


CMD_HELP.update({
    "oi": "πΎπ€π’π’ππ£π: `indomie`\
    \nβ³ : Biodata Indomie\
    \n\nπΎπ€π’π’ππ£π: `.sayang`\
    \nβ³ : Gombalan maut`\
    \n\nπΎπ€π’π’ππ£π: `.semangat`\
    \nβ³ : Jan Lupa Semangat."
})
