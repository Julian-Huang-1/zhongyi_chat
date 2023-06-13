from aleph_alpha_client import Client
from util import creat_collection,updata_collection
client = Client(token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMzk4NywidG9rZW5faWQiOjIwNTZ9.vN1494VpCWVDNlWQ1w9mEuxOpGRrTj0jRG-XJpt6ll0")
creat_collection("image_collection",5120)

from aleph_alpha_client import EmbeddingRequest, Prompt,Image

vectors = []
payloads = []
for i in range(1,6):
    image = Image.from_file(f"path/to/images/{i}.jpg")
    request = EmbeddingRequest(prompt=Prompt.from_image(image), layers=[-1], pooling=["mean"])
    response = client.embed(request, model="luminous-base")
    payloads.append(i)
    for _,v in response.embeddings.items():
        vectors.append(v)
updata_collection("image_collection",vectors,payloads)

pass