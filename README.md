# Meta Ads MCP – Gestão

Este plugin da ZAIP conecta o cliente ao [servidor MCP oficial da Meta](https://developers.facebook.com/documentation/ads-commerce/ads-ai-connectors/ads-mcp-server/ads-mcp-server-overview) por HTTPS e OAuth. As credenciais, os IDs de contas de anúncios e os dados de campanhas ficam fora do pacote.

## ChatGPT Work

1. Um administrador com importação de marketplaces habilitada acessa **Admin → Plugins → Add → Import marketplace** e informa `https://github.com/zaip-ai/zaip-plugin-meta-ads-mcp-gestao`. Confira o resultado da importação e disponibilize o plugin no diretório do workspace. [Guia oficial](https://learn.chatgpt.com/docs/enterprise/plugin-management).
2. Cada pessoa instala pelo diretório e entra na Meta pela tela de OAuth, com sua própria conta. Aprove somente os acessos necessários para a conta de anúncios pertinente. A autorização não transfere acesso de outro usuário.
3. Depois de conectar, teste uma consulta de leitura: “Liste minhas contas de anúncios acessíveis e não faça alterações.” Verifique se o plugin aparece no dot antes de pedir o primeiro relatório.

Um link do GitHub não instala nem autoriza automaticamente o plugin. A disponibilidade depende dos controles do workspace, da interface do ChatGPT e da conta Meta. Se o workspace não puder importar o marketplace, um administrador pode configurar o endpoint `https://mcp.facebook.com/ads` manualmente por OAuth em **Plugins → Add custom MCP server**. [Ajuda do ChatGPT](https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt).

## Codex

Em clientes compatíveis, adicione o marketplace da ZAIP com o comando abaixo.

```sh
codex plugin marketplace add https://github.com/zaip-ai/zaip-plugin-meta-ads-mcp-gestao
```

Instale **Meta Ads MCP – Gestão** e conclua o OAuth. [Guia de plugins](https://developers.openai.com/plugins/build/plugins).

## Permissões

A configuração de gestão solicita `ads_read`, `ads_management` e `ads_mcp_management`. Se a necessidade for somente relatórios, não conceda `ads_management`: use uma conexão separada de leitura. Nunca cole tokens ou senhas em chat ou issues. Antes de aplicar alterações em campanhas, estabeleça o escopo; antes de publicar, ativar, alterar gastos ou excluir, revise os itens afetados e obtenha aprovação explícita.
