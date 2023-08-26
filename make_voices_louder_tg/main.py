import os
from threading import Thread

from flask import Flask
import pyrogram
from replit import Database

from make_voices_louder_tg.functionality import normalize_audio

flask_app = Flask(__name__)
app: pyrogram.Client | None = None

db = Database(os.environ['REPLIT_DB_URL'])


def handle_awake():
    if not app.is_connected:
        run_all_in_thread()
    return ''


def do():
    global app

    app = pyrogram.Client(
            'make_voices_louder_tg',
            session_string=db['tg_session_string']
    )

    @app.on_message(pyrogram.filters.voice)
    async def me(client: pyrogram.Client, message: pyrogram.types.Message):
        print(vars(message))
        print(message.voice)
        file = await app.download_media(message, in_memory=True)
        await client.send_voice(
            'me',
            voice=normalize_audio(bytes(file.getbuffer()))
        )

    app.run()


def run_all_in_thread():
    thread = Thread(target=do)
    thread.start()


def main():
    run_all_in_thread()
    flask_app.run('0.0.0.0', 3000)


if __name__ == '__main__':
    main()

