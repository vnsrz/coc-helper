from dotenv import load_dotenv
import asyncio
import coc
import os

load_dotenv()

async def main():
    async with coc.Client() as coc_client:
        try:
            await coc_client.login(os.environ.get('EMAIL'), os.environ.get('PASSWORD'))
        except coc.invalidcredentials as error:
            exit(error)

        clan = await coc_client.get_clan(tag=os.environ.get('CLAN_TAG'))
        
        members = []
        async for player in clan.get_detailed_members():
            members.append(player)

        with open('coc_out.txt', 'w', encoding='utf-8') as file:
            lista = "\n".join([f"{player.name}\t{player.trophies}\t{player.town_hall}" for player in members])
            file.write(lista)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass