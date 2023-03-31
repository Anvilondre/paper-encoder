from cog import BasePredictor, Input
from sentence_transformers import SentenceTransformer


class Encoder(BasePredictor):
    def setup(self):
        self.model = SentenceTransformer('all-mpnet-base-v2')

    def predict(self, text: str = Input(description="Text to encode")) -> list[float]:
        return self.model.encode(text).tolist()
