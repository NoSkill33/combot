from discord.ext import commands
from discord import app_commands

# niedokończone( NIE DZIAŁA )

# przykładowa komenda / testowa komenda
class testcommand(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @tree.command(name = "test", description = "test")
    async def testcommand(interaction: discord.Interaction):
        await interaction.response.send_message("test")

def setup(bot):
    bot.add.cog(testcommand(bot))