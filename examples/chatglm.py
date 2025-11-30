from modelscope.models.nlp import ChatGLMConfig
from modelscope.models.nlp.chatglm.text_generation import ChatGLMModel

config = ChatGLMConfig(vocab_size = 150528)

model = ChatGLMModel(config)
print(model)
