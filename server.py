from typing import Union
from fastapi import FastAPI, HTTPException
import uuid

from madlib.data import Data
from madlib.madlib import Madlib

app = FastAPI()
data = Data()
sessions = {}


@app.get("/new")
async def new(template: Union[str, None] = None):
    # try:
    madlib = Madlib(data.get_random_story()
                    ) if template is None else Madlib(template)
    # except
    session = str(uuid.uuid4())
    sessions[session] = madlib
    return {"session": session}


@app.get("/{session}")
async def prompt(session: str, answer: Union[str, None] = None):
    madlib = sessions.get(session)

    if madlib is None:
        raise HTTPException(status_code=404, detail="session not found")

    if answer is not None:
        print(answer)
        madlib.give_answer(answer)

    prompt = madlib.get_prompt()
    if prompt is None:
        result = madlib.solve()
        del sessions[session]
        return {"result": result}

    return {"prompt": prompt}
