import base64

data = "CmRlZiBsb29rQW5kU2F5KHRoaW5nKToKICAgIHNvcnRlZCA9IFtdCiAgICBzY2"
data += "91bnQxID0gLTEKICAgIHNjb3VudDIgPSAwCiAgICBmb3IgaSBpbiByYW5nZSh"
data += "sZW4odGhpbmcpKToKICAgICAgICBpZiBpICE9IDAgYW5kIHRoaW5nW2ldID09"
data += "IHNvcnRlZFtzY291bnQxXVtzY291bnQyXToKICAgICAgICAgICAgc29ydGVkW"
data += "3Njb3VudDFdLmFwcGVuZCh0aGluZ1tpXSkKICAgICAgICAgICAgc2NvdW50Mi"
data += "ArPSAxCiAgICAgICAgZWxzZToKICAgICAgICAgICAgc29ydGVkLmFwcGVuZCh"
data += "bdGhpbmdbaV1dKQogICAgICAgICAgICBzY291bnQxICs9IDEKICAgICAgICAg"
data += "ICAgc2NvdW50MiA9IDAKICAgIHJldHVybiAiIi5qb2luKGxpc3QobWFwKGxhb"
data += "WJkYSBlOnN0cihsZW4oZSkpK3N0cihlWzBdKSxzb3J0ZWQpKSkK"

exec(base64.b64decode(data).decode("utf-8"))
