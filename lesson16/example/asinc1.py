import asyncio


async def async_func(n):
    print('Запуск ...', n)
    await asyncio.sleep(n)
    print('... Готово!', n)


async def main():
    # task = asyncio.create_task(async_func())
    await async_func(2)
    print(1212121)
    await async_func(2)



asyncio.run(main())
