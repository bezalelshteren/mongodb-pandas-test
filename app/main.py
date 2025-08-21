from fastapi import FastAPI
from fastapi import HTTPException, Body
import json
import uvicorn
from app.maneger import Maneger

app = FastAPI()


print("is connected")

@app.get("/")
def get_data():
    try:
        manag = Maneger()
        manag.start_all_fanction()
        print(manag.data.to_dict())
        data = manag.data.to_dict()
        json_output = json.dumps(data)
        return json_output
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8004)
