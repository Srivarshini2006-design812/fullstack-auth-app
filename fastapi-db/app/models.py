from pydantic import BaseModel, Field

# -------- INPUT MODEL --------
class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)

# -------- OUTPUT MODEL --------
class UserOut(BaseModel):
    id: int
    name: str
