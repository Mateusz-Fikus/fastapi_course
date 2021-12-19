from fastapi import HTTPException


def http_exception_todo_not_found():
    return HTTPException(status_code=404, detail="Todo not found")
