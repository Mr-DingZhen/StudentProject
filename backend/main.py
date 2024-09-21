"""
@Author: Alice-Yuan
@File: main.py
@Time: 2024/09/14 17:47
"""

import uvicorn
from api import app
from common.constant import HOST, PORT

if __name__ == '__main__':
    uvicorn.run("main:app", host=HOST, port=int(PORT), reload=True)
