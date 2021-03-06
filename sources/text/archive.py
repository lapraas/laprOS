from sources.general import ALL_GENRES, ALL_RATINGS, ALL_SITE_ABBREVIATIONS, BOT_PREFIX, Cmd, MAX_CHAR_NAME_LEN, MAX_CHAR_SPECIES_LEN, MAX_LINK_URL_LEN, MAX_RATING_REASON_LEN, MAX_SUMMARY_LEN, MAX_TITLE_LEN

cogName = "Archive Cog"
cog = {
    "name": cogName,
    "description": "This part of the bot handles the addition, removal, and editing of stories to the story archive. All commands here must either be used in your server's dedicated archive channel or in direct messages with the bot. For a walkthrough on how to add your story, use the Retrieval Cog's `archiveguide` command."
}

errorNotInArchiveChannel = "This part of the bot can only be used in the channel that hosts story links or a direct message channel with the bot."
errorNoPost = "You don't have a post in the archive channel on this server."

archivePostMessageWait = "Please wait..."
archivePostMessagePrefix = "**Writer**:"
archivePostMessageBody = lambda authorID, formattedStory: f"{archivePostMessagePrefix} <@{authorID}>\n\n{formattedStory}\n\n====="
archivePostEmbed = lambda formattedPost: {
    "title": "Stories",
    "description": formattedPost
}
_errorNotFound = lambda title: f"Couldn't find a story titled \"{title}\"."
focus = Cmd(
    "focus",
    f"Focuses the story with the given title in the issuer's archive post. If ",
    usage = [
        "Null Protocol",
        "Song of the Solus",
        "1"
    ],
    errorIndex = lambda index: f"The number you entered ({index}) was more than the number of stories you have.",
    errorNotFound = _errorNotFound
)
getMyPost = Cmd(
    "getmypost",
    f"Sends a copy of the issuer's post to their direct message channel. This command can't be used outside of direct messages.",
    errorNoDM = "This command can only be used in direct messages."
)
_maxLenErrorText = lambda tooLong, maxLen: lambda realLen: f"That {tooLong} is {realLen} characters long. It must be shorter than {maxLen} characters long."
_errorLenTitle = _maxLenErrorText("story title", MAX_TITLE_LEN)
addStory = Cmd(
    "addstory", "createstory",
    "Adds a new story with the given title to the issuer's archive post, creating a post if none exists for them.",
    usage = [
        "Pokemon Mystery Dungeon: Null Protocol"
    ],
    errorLen = _errorLenTitle,
    errorDup = lambda storyTitle: f"You already have a story titled \"{storyTitle}\".",
    errorCooldown = lambda time: f"Another user has created a story in the last ten minutes. Adding one now would mess up the formatting for the posts. Please wait {time} more minutes to add your story."
)
removeStory = Cmd(
    "removestory", "deletestory",
    """
        Removes the story with the given title from the issuer's archive post.
        **BE WARNED** - This *cannot* be undone.
    """,
    usage = [
        "Pokemon Mystery Dungeon: Null Protocol"
    ],
    errorNotFound = _errorNotFound
)
setTitle = Cmd(
    "settitle",
    f"Sets the title of the story currently focused in the issuer's archive post.\nThe entry must be under {MAX_TITLE_LEN} characters long.",
    usage = [
        "Pokemon Mystery Dungeon: Null Protocol"
    ],
    errorLen = _errorLenTitle
)
addGenre = Cmd(
    "addgenre", "addgenres", "setgenre", "setgenres",
    f"Adds one or more genres to the story currently focused in the issuer's archive post.\nEach entry must be a valid genre.",
    usage = [
        "Adventure",
        "Adventure Friendship"
    ],
    errorInvalid = lambda genre: f"The genre specified ({genre}) is not one of the following:\n\n" + "\n".join(ALL_GENRES),
    errorDup = lambda citedStory, genre: f"Your story, {citedStory}, already has the {genre} genre."
)
removeGenre = Cmd(
    "removegenre", "removegenres",
    f"Removes one or more genres from the story currently focused in the issuer's archive post.",
    usage = [
        "Adventure",
        "Adventure Friendship"
    ],
    errorNotFound = lambda citedStory, targetGenre: f"Your story, {citedStory}, does not have the {targetGenre} genre."
)
setRating = Cmd(
    "setrating", "addrating",
    f"""
        Sets the rating for the story currently focused in the issuer's archive post.
        The entry must be a valid rating.
    """,
    usage = [
        "K+"
    ],
    errorInvalid = lambda citedStory, rating: f"The rating for your story, {citedStory}, must be one of {ALL_RATINGS}, not {rating}."
)
setRatingReason = Cmd(
    "setratingreason", "addratingreason",
    f"""
        Sets the rating reason for the story currently focused in the issuer's archive post.
        The entry must be less than {MAX_RATING_REASON_LEN} characters long and can include spoilers.
    """,
    usage = [
        "Swearing, violence",
        "Swearing, violence, ||main character death||."
    ],
    errorLen = _maxLenErrorText("rating reason", MAX_RATING_REASON_LEN)
)
_characterFormattingText = "To specify a name and a species rather than just a species, use the format: `name, species` where `name` is the desired name for the character and `species` is the desired species."

errorParseCharacterNoSpecies = f"There was no species specified for this character."
addCharacter = Cmd(
    "addcharacter", "addchar", "setcharacter", "setchar",
    f"""
        Adds a character with the given species to the story currently focused in the issuer's archive post.
        {_characterFormattingText}
        The entry for the species of the character must be less than {MAX_CHAR_SPECIES_LEN} characters long. The entry for the name of the character, if desired, must be less than {MAX_CHAR_NAME_LEN} characters long.
    """,
    usage = [
        "Yveltal",
        "Orial, Mienfoo"
    ],
    errorDup = lambda citedStory, species, name: f"Your story, {citedStory}, already has a character with the species {species}" + ("." if not name else f" and the name {name}."),
    errorLenSpecies = _maxLenErrorText("character's species", MAX_CHAR_SPECIES_LEN),
    errorLenName = _maxLenErrorText("character's name", MAX_CHAR_NAME_LEN)
)
removeCharacter = Cmd(
    "removecharacter", "removechar",
    f"Removes a character from the story currently focused in the issuer's archive post.\n{_characterFormattingText}",
    usage = [
        "Mienfoo",
        "Orial, Mienfoo"
    ],
    errorNotFound = lambda citedStory, species, name: f"Your story, {citedStory}, does not have a character with the species {species}" + ("." if not name else f" and the name {name}.")
)
setSummary = Cmd(
    "setsummary", "addsummary",
    f"""
        Sets the summary for the story currently focused in the issuer's archive post.
        If newlines are required, the entry must be surrounded in quotes.
        The entry must be less than {MAX_SUMMARY_LEN} characters long.
    """,
    usage = [
        "Forterra has been swept by the new pandemic mystery dungeons. Pokemon in an ever-moving world are now afraid to travel. ...",
        """"Forterra has been swept by the new pandemic mystery dungeons.
        Pokemon in an ever-moving world are now afraid to travel. ..." """
    ],
    errorLen = _maxLenErrorText("summary", MAX_SUMMARY_LEN)
)
addLink = Cmd(
    "addlink", "setlink",
    f"""
        Adds a link to the story currently focused in the issuer's archive post.
        The first entry must be a valid site abbreviation. The second entry must be the desired URL from that site.
        The second entry must be less than {MAX_LINK_URL_LEN} characters long. If your link is longer than this limit, talk to a moderator.
    """,
    usage = [
        "AO3 https://archiveofourown.org/",
        "FFN https://www.fanfiction.net/"
    ],
    errorDup = lambda citedStory, abbr: f"Your story, {citedStory}, already has a link with the site abbreviation {abbr}. Remove it with the `removelink` command to change it.",
    errorLen = _maxLenErrorText("link URL", MAX_LINK_URL_LEN),
    errorInvalid = lambda citedStory, abbr: f"The site abbreviation for the link you are trying to add to your story, {citedStory}, must be one of " + ", ".join(ALL_SITE_ABBREVIATIONS.keys()) + f", not {abbr}."
)
removeLink = Cmd(
    "removelink",
    f"Removes the link with the given site abbreviation from the story currently focused in the issuer's archive post.",
    usage = [
        "AO3",
        "FFN"
    ],
    errorNotFound = lambda citedStory, abbr: f"Your story, {citedStory}, does not have a link with the site abbreviation {abbr}."
)
multi = Cmd(
    "multi",
    f"""
        Performs multiple commands at once. For each command to work, it has to be on a separate line. It's not necessary to use the bot's prefix (`{BOT_PREFIX}`) before the commands. See usages for a couple of examples on how to format this command.
        Big thanks to love for laying the groundwork for this command.
    """,
    usage = [
        f"""
            {addStory.name} Null Protocol
            {addGenre.name} Adventure Friendship
            {setRating.name} T
            {addCharacter.name} Orial, Mienfoo
        """,
        f"""
            {removeLink.name} AO3
            {addLink.name} AO3 https://archiveofourown.org/
        """
    ],
    errorInvalid = lambda commandName: f"Couldn't find a command named {commandName}. Did you mistype?\n\n",
    errorArgs = lambda commandName: f"There was an incorrect number of arguments for the command {commandName}.\n\n",
    errorQuotes = lambda command: f"There was an issue with the quotes in your command: `{command}`"
)
convert = Cmd(
    "convert",
    f"Adds each story in the archive channel this command is used in to the JSON database (updates from Discord parsing-based database to JSON database). If used without a number, updates all posts, otherwise updates the specified number of latest-added posts.",
    usage = [
        "5"
    ]
)
refreshPost = Cmd(
    "refreshpost", "updatepost",
    f"Re-formats and re-adds reactions to the post for the command's issuer."
)

