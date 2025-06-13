from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8080",
    "http://localhost:5173",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8080",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def convert_to_string_and_sort(string: str) -> list[str]:
    list_char = [char for char in string]
    list_char.sort()
    return list_char


@app.post("/convert/{string_to_convert}")
async def convert(string_to_convert: str = Path(min_length=1)):
    list_char = convert_to_string_and_sort(string_to_convert)
    return {'word': list_char}
