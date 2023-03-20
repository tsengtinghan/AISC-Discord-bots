# Discord URL Summarizer Bot

This Discord bot listens for URLs posted in a specific input channel and generates a summary of the linked content. The summary is then sent to a designated output channel.

## Features

- Automatically detects URLs in messages.
- Extracts text from the provided URLs.
- Generates a summary of the extracted text using GPT-4.
- Sends the summary to a specified output channel.

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/discord-url-summarizer.git
```

2. Change to the project directory:

```bash
cd discord-url-summarizer
```

3. Install required dependencies:

```bash
pip install -r requirements.txt
```

4. Set up a Discord bot and add it to your server:

- Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new bot.
- Note down the bot token and client ID.
- Enable "Server Members Intent" and "Message Content Intent" for the bot.
- Use the following URL to add the bot to your server, replacing `YOUR_CLIENT_ID` with your bot's client ID:

```
https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&scope=bot&permissions=2048
```

5. Configure the bot:

- Copy the `config_example.ini` file and name it `config.ini`.
- Open the `config.ini` file and add your bot token, input channel, and output channel.

6. Run the bot:

```bash
python main.py
```

## Usage

1. Start the bot with `python main.py`.
2. Post a URL in the input channel.
3. The bot will generate a summary and send it to the output channel.

## Limitations

- The text extraction and summary generation may not work for all websites.
- The bot may not work with private or restricted content.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

Remember to replace placeholders like `yourusername` with the appropriate values for your project.
