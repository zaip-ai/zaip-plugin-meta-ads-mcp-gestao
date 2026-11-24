# Meta Ads MCP – Gestão

Plugin da ZAIP para consultar resultados e gerenciar campanhas pelo [servidor MCP oficial da Meta](https://developers.facebook.com/documentation/ads-commerce/ads-ai-connectors/ads-mcp-server/ads-mcp-server-overview). Cada pessoa conecta sua própria conta Meta por OAuth.

## Instalação local no dot ou no Codex

O plugin é distribuído neste repositório do GitHub. **Baixe os arquivos para o computador e instale a partir da pasta baixada, no perfil que você já usa.** O catálogo incluído no repositório permite que o aplicativo encontre o plugin nessa pasta. O servidor MCP roda na infraestrutura da Meta e o plugin se conecta a ele por HTTPS.

### Pedido pronto para colar no agente

> Instale o plugin Meta Ads MCP – Gestão no meu perfil local atual. Baixe https://github.com/zaip-ai/zaip-plugin-meta-ads-mcp-gestao para uma pasta permanente neste computador ou reutilize uma cópia existente deste repositório. Siga o README dessa pasta. No dot desktop, use a fonte local “ZAIP Meta Ads Plugins”. No Codex, registre a pasta com `codex plugin marketplace add .` e instale `meta-ads-gestao@zaip-meta-ads-plugins`. Abra o OAuth da Meta para eu autorizar no navegador. Depois, confirme a conexão com uma consulta de leitura às minhas contas de anúncios.

### 1. Baixe o repositório

Em uma pasta onde deseja guardar o plugin, execute os comandos abaixo. Se já tiver uma cópia, abra a raiz dela. Também é possível usar **Code → Download ZIP** no GitHub e extrair o arquivo. A pasta certa contém este README e o arquivo `.agents/plugins/marketplace.json`.

```sh
git clone --branch main https://github.com/zaip-ai/zaip-plugin-meta-ads-mcp-gestao.git
cd zaip-plugin-meta-ads-mcp-gestao
```

### 2A. Instale no dot (ChatGPT desktop)

1. No aplicativo desktop, abra a pasta baixada como projeto no perfil em que deseja usar o plugin. Reinicie o aplicativo para ele carregar o catálogo do projeto.
2. No modo Work, abra **Plugins** e escolha **ZAIP Meta Ads Plugins** no seletor de fontes. Essa fonte corresponde à pasta que você baixou.
3. Selecione **Meta Ads MCP – Gestão**, clique em **Instalar** e conclua a autorização da Meta quando o aplicativo solicitar. [Guia de instalação de plugins locais](https://developers.openai.com/plugins/build/plugins#install-a-local-plugin-manually).

### 2B. Instale no Codex

Na raiz da pasta baixada, execute os comandos com o perfil habitual do Codex. O ponto em `marketplace add .` indica a pasta atual. Esse comando registra o catálogo local. O comando seguinte instala o plugin.

```sh
codex plugin marketplace add .
codex plugin add meta-ads-gestao@zaip-meta-ads-plugins
codex plugin list --marketplace zaip-meta-ads-plugins --json
codex mcp list
```

Confira se o plugin aparece com `installed: true` e `enabled: true`, e se o servidor `meta-ads` aponta para `https://mcp.facebook.com/ads`. Se o estado for `Not logged in`, execute o comando abaixo e conclua a autorização no navegador com a conta Meta que tem acesso aos anúncios.

```sh
codex mcp login meta-ads --scopes ads_read,ads_management,ads_mcp_management
```

## Confirmar a conexão

Abra uma nova conversa no cliente escolhido e peça: **“Use o plugin Meta Ads MCP – Gestão para listar as contas de anúncios às quais tenho acesso, sem fazer alterações.”** Uma resposta da Meta confirma que a consulta funcionou. Se a lista vier vazia, confira se a identidade autorizada tem acesso à conta de anúncios esperada.

## Permissões

Esta edição de gestão solicita `ads_read`, `ads_management` e `ads_mcp_management`. Para uso exclusivo de relatórios, escolha uma conexão de leitura. Insira credenciais apenas na tela de autorização da Meta. Antes de publicar, ativar ou excluir campanhas ou alterar gastos, revise os itens afetados e obtenha aprovação explícita.
