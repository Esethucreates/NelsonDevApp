from fastapi import FastAPI, Path

app = FastAPI()


def convert_to_string_and_sort(string: str) -> list[str]:
    list_char = [char for char in string]
    list_char.sort()
    return list_char


@app.post("/convert/{string_to_convert}")
async def convert(string_to_convert: str = Path(min_length=1)):
    list_char = convert_to_string_and_sort(string_to_convert)
    return {'word': list_char}
