from token import OP
from typing import List, Optional
from pydantic import BaseModel

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List["Comment"]] = None # self referencing

Comment.model_rebuild() #required to have this line after self referencing to avoid performance degradation

comment = Comment(id=1, content="This is a comment")
print(comment)

comment_with_replies = Comment(id=2, content="This is a comment with replies", replies=[Comment(id=3, content="This is a reply")])
print(comment_with_replies)

print(comment_with_replies.model_dump_json(indent=2))

comment_with_replies2 = Comment(id=4, content="This is a comment with replies", replies=[Comment(id=5, content="This is a reply"), Comment(id=6, content="This is another reply")])
print(comment_with_replies2)

print(comment_with_replies2.model_dump_json(indent=4))
