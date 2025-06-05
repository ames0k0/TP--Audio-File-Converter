from typing import Annotated, Sequence

from pydantic import BaseModel
from fastapi import FastAPI, Query, UploadFile, File


app = FastAPI(title="Audio file converter")


class AudioConverterGetOut(BaseModel):
    SUPPORTED_INPUT_FILE_TYPES: Sequence[str]
    SUPPORTED_EXPORT_FILE_FORMATS: Sequence[str]


@app.get(
    "/audio/convert",
    response_model=AudioConverterGetOut
)
async def get_audio_converter():
    return {
        "SUPPORTED_INPUT_FILE_TYPES": [],
        "SUPPORTED_EXPORT_FILE_FORMATS": [],
    }


@app.post(
    "/audio/convert"
)
async def post_audio_converter(
    export_file_format: Annotated[
        str,
        Query(description="Format to convert Audio file"),
    ],
    file: Annotated[
        UploadFile,
        File(description="Audio file to convert"),
    ],
) -> str:
    return "OK"


if __name__ == "__main__":
    import os
    import uvicorn

    uvicorn.run(
        app=app,
        host=os.getenv("UVICORN_HOST"),
        port=int(
            os.getenv("UVICORN_PORT")
        ),
    )

