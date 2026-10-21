"""Adaptador do servidor local usado no projeto. AgentScope 2.0.6."""
from pydantic import SecretStr

from agentscope.model import OpenAIChatModel
from agentscope.credential import OpenAICredential


def criar_modelo() -> OpenAIChatModel:
    """Retorna o adaptador. Construí-lo ainda não faz uma inferência.

    BASE_URL aponta para uma API compatível com chat completions.
    MODEL_NAME deve coincidir com o identificador carregado no servidor.
    API_KEY é fictícia no servidor local sem autenticação.
    """
    credencial = OpenAICredential(
        api_key=SecretStr("lm-studio"),
        base_url="http://127.0.0.1:1234/v1",
    )

    modelo = OpenAIChatModel(
        credential=credencial,
        model="qwen3.5-4b",
        stream=False,
        extra_body={
            "chat_template_kwargs": {
                "enable_thinking": False,
            }
        },
    )

    return modelo