import os
from typing import Annotated, Sequence
from tempfile import NamedTemporaryFile

from pydantic import BaseModel
from starlette.concurrency import run_in_threadpool
from fastapi import FastAPI, HTTPException, Response, Query, UploadFile, File, status

from converter import Converter


app = FastAPI(title="Audio file converter")


class AudioConverterGetOut(BaseModel):
    SUPPORTED_FILE_EXTENSIONS: Sequence[str]
    SUPPORTED_EXPORT_FILE_FORMATS: Sequence[str]


@app.get("/audio/convert")
async def get_audio_converter() -> AudioConverterGetOut:
    return {
        "SUPPORTED_FILE_EXTENSIONS": Converter.SUPPORTED_FILE_EXTENSIONS,
        "SUPPORTED_EXPORT_FILE_FORMATS": Converter.SUPPORTED_EXPORT_FILE_FORMATS,
    }


@app.post("/audio/convert")
async def post_audio_converter(
    export_file_format: Annotated[
        str,
        Query(description="Format to convert Audio file"),
    ],
    file: Annotated[
        UploadFile,
        File(description="Audio file to convert"),
    ],
) -> Response:
    converted_audio_file: bytes | None = None

    converter = Converter()
    filename, fileext = os.path.splitext(file.filename)

    with NamedTemporaryFile(suffix=fileext, mode="wb", delete=False) as ftwb:
        ftwb.write(await file.read())

    try:
        converter.set_input(filepath=ftwb.name)
        converter.set_output(export_file_format=export_file_format)

        converted_audio_file = await run_in_threadpool(converter.convert)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.args[0],
        )
    finally:
        os.remove(ftwb.name)

    return Response(
        content=converted_audio_file,
        media_type=converter.MAP_FILE_FORMAT_TO_FILE_MIMETYPE[export_file_format],
        headers={
            "Content-Disposition": f'attachment; filename="{filename}.{export_file_format}"',
        },
    )


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

