from uuid import uuid4

import aiofiles
from fastapi import UploadFile, Request


async def save_image(image: UploadFile, request: Request) -> str:
    """ save file to 'images' dir """
    out_file_path = f"images/{uuid4()}.{image.filename.split('.')[-1]}"
    async with aiofiles.open(out_file_path, 'wb') as out_file:
        content = await image.read()
        await out_file.write(content)
    return f"{request.base_url}{out_file_path}"
