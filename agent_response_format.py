from typing import List
from pydantic import BaseModel, Field

class Source(BaseModel):
    """Schema for source url"""
    url:str = Field(description="The url of source")

class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""
    answer:str = Field(description="The agent search results")
    url:str = Field(description="The url of the source")
    # sources:List[] = Field(default_factory=list, description="The list of source in search result")