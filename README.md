# Meta Ads MCP – Gestão

Plugin da ZAIP para consultar resultados e gerenciar campanhas pelo [servidor MCP oficial da Meta](https://developers.facebook.com/documentation/ads-commerce/ads-ai-connectors/ads-mcp-server/ads-mcp-server-overview). Cada pessoa conecta sua própria conta Meta por OAuth.

## Instalar pelo dot (ChatGPT Work)

Cole este pedido no dot, no workspace em que deseja usar o plugin.

> Instale o plugin **Meta Ads MCP – Gestão** da ZAIP na minha conta do workspace atual. Procure o plugin no diretório e abra a instalação. A origem é https://github.com/zaip-ai/zaip-plugin-meta-ads-mcp-gestao. Se ele ainda precisar ser importado, confira se tenho acesso de administrador e me indique a etapa necessária. Abra a autorização da Meta para que eu escolha a conta. Depois que eu autorizar, use o plugin para listar minhas contas de anúncios acessíveis, sem alterar campanhas.

Se o dot pedir uma ação na interface, siga a etapa correspondente.

1. **Plugin disponível no diretório.** Abra **Plugins**, procure **Meta Ads MCP – Gestão**, selecione **Instalar** e conclua a autorização da Meta quando solicitada.
2. **Plugin ausente do diretório.** Um administrador do workspace abre **Admin → Plugins → Add → Import marketplace**. Em **Source**, informa `https://github.com/zaip-ai/zaip-plugin-meta-ads-mcp-gestao`, deixa **Path** vazio e usa a branch `main`. Depois da importação, confere **Import results** e disponibiliza o plugin para a sua função. Volte ao diretório para instalá-lo. [Guia de importação do ChatGPT](https://learn.chatgpt.com/docs/enterprise/plugin-management).
3. **Plugin marcado como Desktop only.** Abra o mesmo workspace no aplicativo desktop e inicie uma conversa com o plugin. [Disponibilidade de plugins importados](https://learn.chatgpt.com/docs/enterprise/plugin-management#desktop-only-plugins).

## Instalar pelo agente Codex

Cole este pedido no Codex que você já usa. A instalação usa o perfil local ativo do Codex.

> Instale o plugin `meta-ads-gestao@zaip-meta-ads-plugins` no meu perfil atual do Codex. Use o marketplace de https://github.com/zaip-ai/zaip-plugin-meta-ads-mcp-gestao na branch `main` e siga os comandos do README. Se já estiver instalado e habilitado, siga direto para a verificação do MCP. Se faltar autenticação, inicie o OAuth para eu concluir no navegador. Depois, teste a conexão listando minhas contas de anúncios, sem alterar campanhas.

### Comandos para o agente

Confira as fontes com `codex plugin marketplace list`. Na primeira instalação, registre a origem. Se `zaip-meta-ads-plugins` já estiver cadastrado com essa origem, atualize-o com `codex plugin marketplace upgrade zaip-meta-ads-plugins` e siga para a instalação.

```sh
codex plugin marketplace add https://github.com/zaip-ai/zaip-plugin-meta-ads-mcp-gestao --ref main
```

Instale o plugin e confira se a entrada aparece com `installed: true` e `enabled: true`. Em seguida, localize o servidor `meta-ads` em `https://mcp.facebook.com/ads`.

```sh
codex plugin add meta-ads-gestao@zaip-meta-ads-plugins
codex plugin list --marketplace zaip-meta-ads-plugins --json
codex mcp list
```

Se o servidor mostrar `Not logged in`, inicie a autorização. No navegador, confira a identidade Meta e os acessos solicitados.

```sh
codex mcp login meta-ads --scopes ads_read,ads_management,ads_mcp_management
```

## Confirmar a conexão

Abra uma nova conversa no cliente escolhido e peça: **“Use o plugin Meta Ads MCP – Gestão para listar as contas de anúncios às quais tenho acesso, sem fazer alterações.”** Uma resposta da Meta confirma que a consulta funcionou. Se a lista vier vazia, confira se a identidade autorizada tem acesso à conta de anúncios esperada.

## Permissões

Esta edição de gestão solicita `ads_read`, `ads_management` e `ads_mcp_management`. Para uso exclusivo de relatórios, escolha uma conexão de leitura. Insira credenciais apenas na tela de autorização da Meta. Antes de publicar, ativar ou excluir campanhas ou alterar gastos, revise os itens afetados e obtenha aprovação explícita.
