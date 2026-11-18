import asyncio
from pydantic import SecretStr

from agentscope.credential import OpenAICredential
from agentscope.model import OpenAIChatModel
from agentscope.message import UserMsg
from agentscope.agent import Agent

async def main() -> None:

    # Configuração do adaptador (conexão com o modelo)
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

    # Criação do agente
    agente = Agent(
        name="Tutor",
        system_prompt="Responda em PT/BR, de forma breve Apenas a resposta final.",
        model=modelo
    )

    # Envio e recebimento de mensagens
    entrada = UserMsg(name="aluno", content="O que é uma tool?")
    resposta = await agente.reply(entrada)
    print(resposta.get_text_content())

    
if __name__ == "__main__":
    asyncio.run(main())
