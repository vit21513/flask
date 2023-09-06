import os
import threading

import aiofiles as aiofiles
import aiohttp as aiohttp

# Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
# адреса.
# � После загрузки данных нужно записать их в отдельные
# файлы.
# � Используйте потоки.

list_url = ["https://ya.ru/","https://yandex.ru/","https://mail.ru/","https://rambler.ru","https://hawk.ru/"]
#
# async with aiofiles.open(filename, 'wb') as f:
#                     await f.write(content)


async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
        if response.status == 200:
            content = await response.read()


filename = os.path.join('images', filename)
                async with aiofiles.open(filename, 'wb') as f:
                    await f.write(content)

