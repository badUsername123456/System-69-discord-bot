import discord
import json
import requests
from discord.ext import commands
from ._comand_chache import register_commands
from discord import (
    Embed,
    Interaction,
    app_commands,
    Object
)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        APICog(bot),
        guilds=[Object(id=938541999961833574)]
    )


class APICog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        register_commands(self)
        self.bot = bot

    @app_commands.command(description='sends a random picture of a fox')
    async def fox(self, interaction: Interaction):
        async with interaction.channel.typing():
            async def get_fox():
                return json.loads(requests.get('https://randomfox.ca/floof/').text)['image']

            async def btn_interaction(btn_interaction_p):
                embed = btn_interaction_p.message.embeds[0].set_image(url=await get_fox())
                await btn_interaction_p.response.edit_message(embed=embed)

            next_btn = discord.ui.Button(label='next')

            view = discord.ui.View()
            next_btn.callback = btn_interaction

            view.add_item(next_btn)

            ui_embed = discord.Embed(title='A Fox')
            ui_embed.set_image(url=await get_fox())

            await interaction.response.send_message(embed=ui_embed, view=view)

    @app_commands.command(description='sends a random image of a dog')
    async def dog(self, interaction: Interaction):
        async with interaction.channel.typing():
            async def get_dog():
                return json.loads(requests.get('https://dog.ceo/api/breeds/image/random').text)['message']

            async def btn_interaction(_btn_interaction):
                embed = _btn_interaction.message.embeds[0].set_image(url=await get_dog())
                await _btn_interaction.response.edit_message(embed=embed)

            next_btn = discord.ui.Button(label='next')

            view = discord.ui.View()
            next_btn.callback = btn_interaction

            view.add_item(next_btn)

            ui_embed = discord.Embed(title='A Dog')
            ui_embed.set_image(url=await get_dog())

            await interaction.response.send_message(embed=ui_embed, view=view)

    @app_commands.command(description='sends a random image of a cat')
    async def cat(self, interaction: Interaction):
        async with interaction.channel.typing():
            async def get_cat():
                return json.loads(requests.get('https://aws.random.cat/meow').text)['file']

            async def btn_interaction(_btn_interaction):
                embed = _btn_interaction.message.embeds[0].set_image(url=await get_cat())
                await _btn_interaction.response.edit_message(embed=embed)

            next_btn = discord.ui.Button(label='next')

            view = discord.ui.View()
            next_btn.callback = btn_interaction

            view.add_item(next_btn)

            uiEmbed = discord.Embed(title='A complete catalogue')
            uiEmbed.set_image(url=await get_cat())

            await interaction.response.send_message(embed=uiEmbed, view=view)

    @app_commands.command(description='sends a meme')
    async def meme(self, interaction: Interaction):
        async with interaction.channel.typing():
            async def get_meme():
                return json.loads(requests.get('https://meme-api.herokuapp.com/gimme').text)['url']

            async def btn_interaction(_btn_interaction):
                embed = _btn_interaction.message.embeds[0].set_image(url=await get_meme())
                await _btn_interaction.response.edit_message(embed=embed)

            next_btn = discord.ui.Button(label='next')

            view = discord.ui.View()
            next_btn.callback = btn_interaction

            view.add_item(next_btn)

            ui_embed = discord.Embed(title='A meme')
            ui_embed.set_image(url=await get_meme())

        await interaction.response.send_message(embed=ui_embed, view=view)

    @app_commands.command(description='sends a random fact about a cat')
    async def catfact(self, interaction: Interaction):
        async with interaction.channel.typing():
            em = Embed(title='A cat fact', description='learn more about cats here: https://www.catster.com/')
            em.add_field(
                name='Did you know...',
                value=json.loads(requests.get('https://catfact.ninja/fact').text)['fact']
            )

        await interaction.response.send_message(embed=em)

    @app_commands.command(description='sends a random fact about a dog')
    async def dogfact(self, interaction: Interaction):
        async with interaction.channel.typing():
            em = Embed(title='A dog fact', description='learn more about cats here: https://dog-api.kinduff.com/')
            em.add_field(
                name='Did you know...',
                value=json.loads(requests.get('https://dog-api.kinduff.com/api/facts').text)['facts'][0]
            )

        await interaction.response.send_message(embed=em)

    def pass_(self) -> None:
        ...

    def __cog_docs__(self):
        self.pass_()
        return '''
        The cog is a wrapper for all the api related commands.
        These include:
            - fox
            - dog
            - cat
            - meme
            - catfact
            - dogfact
        '''
