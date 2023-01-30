import logging
import sys
from textwrap import dedent
import time

import requests
import telegram
from environs import Env

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler('debug.log', 'w', 'utf-8'),
                        logging.StreamHandler(),
                    ])


def main():
    env = Env()
    env.read_env()
    connection_timeout = 10
    dvmn_token = env('DEVMAN_TOKEN')
    tg_chat_id = env('TELEGRAM_CHAT_ID')
    tg_bot_api_token = env('TELEGRAM_BOT_API_TOKEN')

    tg_bot = telegram.Bot(token=tg_bot_api_token)

    params = {}
    headers = {'Authorization': f'Token {dvmn_token}'}
    long_polling_url = 'https://dvmn.org/api/long_polling/'

    while True:
        try:
            response = requests.get(long_polling_url, headers=headers, params=params)
            response.raise_for_status()
            user_reviews = response.json()

            if user_reviews['status'] == 'found':
                new_attempts = user_reviews['new_attempts']
                for attempt in new_attempts:
                    lesson_title = attempt['lesson_title']
                    lesson_url = attempt['lesson_url']
                    is_negative = attempt['is_negative']

                    if is_negative:
                        result_msg = 'Ты шёл к успеху, братан! Не получилось, не фортануло :D'
                    else:
                        result_msg = 'А ты хорош, бро! Проверяющий был в восторге :D'

                    text = (f'''
                            Преподаватель проверил работу "{lesson_title}"

                            {result_msg}
                            {lesson_url}
                            ''')

                    tg_bot.send_message(text=dedent(text), chat_id=tg_chat_id)

            elif user_reviews['status'] == 'timeout':
                params['timestamp'] = user_reviews['timestamp_to_request']

        except requests.ConnectionError:
            logging.error('Ошибка подключения. Проверьте интернет соединение.')
            time.sleep(connection_timeout)
        except requests.ReadTimeout:
            logging.error('Время ожидания запроса истекло.')
        except KeyboardInterrupt:
            logging.info('Остановлено пользователем.')
            sys.exit(0)


if __name__ == '__main__':
    main()
