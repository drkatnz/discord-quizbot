# discord-quizbot

A trivia bot for discord, written in python. Runs a quiz where the first user to ten questions wins.

## Pre-requisites:

Requires:
- [discord.py](https://github.com/Rapptz/discord.py)
- an app setup on discord, [instructions available here.](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token)
- the App Bot User Token from the discord api (above)

## Example usage

Simply run with:

`python bot.py APP_BOT_USER_TOKEN`

## Interactions on discord

Users can start a quiz with !ask or !quiz, stop a running quiz with !stop or !halt, move onto the next question with !next, or force the bot to exit with !logoff.  !scores will give the current scoreboard.  First user to ten questions right wins. Users can only answer questions or progress to the next question from the same channel the bot is running the quiz in. The quiz can be halted or started from any channel. Only one quiz may run at a time.

## Known limitations

- Punctuation in quiz answers must be provided identically to the answer in the corpus.
- will not stop on it's own, must be manually stopped by a user.
- doesn't consider admin access for stop/start commands.


## Data files

Currently supports the same format data files as [MoxQuizz](http://moxquizz.de), an IRC trivia bot that works on eggdrop.  By default it will load everything in this directory into the quiz corpus.



