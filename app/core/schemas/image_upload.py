from pydantic import BaseModel, HttpUrl


class UploadedImageResponse(BaseModel):
    image_url: HttpUrl
    image_id: int
