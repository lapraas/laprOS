
import sources.text.archive as ARCH
from sources.general import ALL_GENRES, ALL_RATINGS, ALL_SITE_ABBREVIATIONS, BOT_PREFIX as lap, Cmd, stripLines

cog = {
    "name": "Retrieval Cog",
    "description": "This part of the bot aids in finding stories and has other story-related utilities."
}

setArchiveChannel = Cmd(
    "setarchivechannel",
    "Sets the archive channel for this server.",
    usage = [
        "story-links",
        "792629600860897330",
        "<#792629600860897330>"
    ],
    success = lambda channel: f"Successfully set the archive channel to `{channel}`."
)
setArchive = Cmd(
    "setarchive", "defaultarchive", "setguild", "defaultguild",
    f"""
        Sets the story archive to use when operating the bot in DMs to the one for the guild in which the command is being issued.
    """,
    usage = [
        "PMD Writers' Union",
        "546872429621018635"
    ],
    errorDM = "This command can't be used in direct messages.",
    success = lambda guild: f"Successfully set your archive preference to the story archive in `{guild}`."
)
errorNoArchivePreference = f"You haven't set your archive preference yet. You can do so with the {setArchive.refF()} command."
_listText = lambda item, joinedItems, suffix=True: f"Below is each valid {item}: ```\n{joinedItems}```" + ("" if not suffix else f"\nIf your {item} is not listed here, please let a moderator know.")
listGenres = Cmd(
    "listgenres",
    f"Gets a list of possible story genres to be added with {ARCH.addGenre.refF()}.",
    success = _listText("genre", "\n".join(ALL_GENRES))
)
listSites = Cmd(
    "listsites",
    f"Gets a list of valid site abbreviations to be used with {ARCH.addLink.refF()}.",
    success = _listText("site abbreviation", "\n".join([f"{name} (used for {ALL_SITE_ABBREVIATIONS[name]})" for name in ALL_SITE_ABBREVIATIONS]))
)
listRatings = Cmd(
    "listratings",
    f"Gets a list of valid ratings to be set with {ARCH.setRating.refF()}.",
    success = _listText("rating", ", ".join(ALL_RATINGS), False)
)
archiveGuide = Cmd(
    "archiveguide", "archivehelp",
    f"Shows a help message that explains how to add a story through the {ARCH.cogName}.",
    pages = [
        {
            "title": "Archive Guide",
            "description": f"""
                The main feature of this bot is its story archive. In the archive, stories are displayed in a neat uniform fashion and can be fetched using various search commands. This guide will tell you how to set up a post in your server's archive channel.
                
                Commands used in this guide must either be used in your server's archive channel or in direct messages with the bot. To use the commands in direct messages, you must first select the Discord server you want to add a post to via the {setArchive.refF()} command.
            """
        },
        {
            "title": "Multi and Other Information",
            "description": f"""
                Before we begin, make sure you use the {ARCH.multi.refF()} command if you want to perform multiple commands in one go. It's possible to add all the info for a story in one fell swoop, but only if you use this command. Use `{lap}help {ARCH.multi.name}` for more information.
                
                Also, if you run into a length limit for any of your story info and want to get around it, you may ask one of the moderators for assistance.
            """
        },
        {
            "title": "Adding / Removing a Story, Changing Titles",
            "description": f"""
                Use the {ARCH.addStory.refF()} command to add a new story, and give it your story's name.
                ```{ARCH.addStory.ref()} Null Protocol```
                
                If you want to remove any of your stories, you may use the {ARCH.removeStory.refF()} command and give it the target story's name.
                ```{ARCH.removeStory.ref()} Null Protocol```
                
                If you want to alter a story's name, focus that story in your post and use the {ARCH.setTitle.refF()} command.
                ```{ARCH.setTitle.ref()} Pokemon Mystery Dungeon: Null Protocol```
            """
        },
        {
            "title": "Adding / Removing Genres",
            "description": f"""
                Use the {ARCH.addGenre.refF()} command to give your story a genre. Valid genres can be found using the command {listGenres.refF()}. If you want to add multiple genres at a time, separate each with a space.
                ```{ARCH.addGenre.ref()} Adventure Friendship```
                
                If you want to remove genres from a story, focus that story in your post and use the {ARCH.removeGenre.refF()} command. You may remove multiple genres at a time by separating each with a space.
                ```{ARCH.removeGenre.ref()} Adventure Friendship```
            """
        },
        {
            "title": "Adding a Rating",
            "description": f"""
                Use the {ARCH.setRating.refF()} command to set the rating for your story. Valid ratings can be found using the command {listRatings.refF()}.
                ```{ARCH.setRating.ref()} T```
            """
        },
        {
            "title": "Adding a Rating Reason",
            "description": f"""
                Use the {ARCH.setRatingReason.refF()} command to add a little blurb next to your rating describing why you rated your story the way you did. Note that you can use spoilers in this blurb.
                ```{ARCH.setRatingReason.ref()} Swearing, violence, ||character death||.```
            """
        },
        {
            "title": "Adding / Removing Characters",
            "description": f"""
                Use the {ARCH.addCharacter.refF()} command to add characters to your story. Characters have a species and an optional name. If your character doesn't have/need a name, you can simply enter their species. If your character needs both a species and a name, give their name followed by a comma followed by their species. See the examples below.
                ```{ARCH.addCharacter.ref()} Quil, Cyndaquil
                {ARCH.addCharacter.ref()} Orial, Mienfoo
                {ARCH.addCharacter.ref()} Guildmaster Kess, Archeops
                {ARCH.addCharacter.ref()} Yveltal```
                
                If you wish to remove a character from your story, use the {ARCH.removeCharacter.refF()} command. If the target character has a unique species among all of your characters, you may enter their species. Otherwise you will need to give the name and the species of the target character with the above formatting.
                ```{ARCH.removeCharacter.ref()} Quil, Cyndaquil
                {ARCH.removeCharacter.ref()} Orial, Mienfoo
                {ARCH.removeCharacter.ref()} Guildmaster Kess, Archeops
                {ARCH.removeCharacter.ref()} Yveltal```
            """
        },
        {
            "title": "Adding a Summary",
            "description": f"""
                Use the {ARCH.setSummary.refF()} command to set the summary for your story. If you want to use newlines in this summary, you will have to surround it in quotes.
                ```{ARCH.setSummary.ref()} Forterra has been swept by the new pandemic mystery dungeons... (etc.)```
            """
        },
        {
            "title": "Adding / Removing Links",
            "description": f"""
                Use the {ARCH.addLink.refF()} command to add links to your story. This command takes the abbreviation for the site and the URL itself. The list of valid site abbreviations can be found using the {listSites.refF()} command.
                ```{ARCH.addLink.ref()} AO3 https://archiveofourown.org/```
                
                If you want to remove a link from your story, use the {ARCH.removeLink.refF()} command and give it the site abbreviation for the target link.
                ```{ARCH.removeLink.ref()} AO3```
            """
        }
    ]
)
randomStory = Cmd(
    "randomstory",
    f"Gets a random story from the story archive.",
    error = "Couldn't find a story.",
    embed = lambda title, author, summary, jumpURL: {
        "title": title,
        "description": f"by {author}\n" + (f"```{summary}```" if summary else "No description") + "\n" + jumpURL
    }
)
searchByAuthor = Cmd(
    "searchbyauthor",
    f"Gets a link to the archive post for a given user.",
    usage = [
        "laprOS",
        "785222129061986304",
        "<@785222129061986304>"
    ],
    errorName = lambda name: f"Couldn't find an author with the name `{name}`.",
    errorID = lambda id: f"Couldn't find an author with the ID `{id}`.",
    errorPost = lambda name: f"The specified user, `{name}`, doesn't have a post in the story archive.",
    embed = lambda name, jump: {
        "title": f"Stories by {name}",
        "description": f"Archive post:\n{jump}"
    }
)
