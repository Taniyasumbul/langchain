from langchain.text_splitter import RecursiveCharacterTextSplitter

text="""
        Welcome to today’s exciting clash between India and Australia!  
The stadium is packed, the pitch looks good for batting, and the crowd is buzzing with energy.

--- First Innings ---
India won the toss and elected to bat first.  
Rohit Sharma and Shubman Gill are at the crease. The first ball is bowled...  
What a shot! Rohit drives through the covers for four.  
Gill follows up with a stylish pull shot for another boundary.  
India is off to a flying start. 
"""
splitter=RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
)

result = splitter.split_text(text)
print(result)

