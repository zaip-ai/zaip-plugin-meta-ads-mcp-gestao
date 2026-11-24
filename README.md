# Meta Ads MCP – Gestão

Plugin da ZAIP para consultar resultados e gerenciar campanhas pelo [servidor MCP oficial da Meta](https://developers.facebook.com/documentation/ads-commerce/ads-ai-connectors/ads-mcp-server/ads-mcp-server-overview). Cada pessoa conecta sua própria conta Meta por OAuth.

## Usar no ChatGPT pelo navegador e no Codex local

**Para usar nos dois clientes, configure a conexão no workspace do ChatGPT e instale o pacote no perfil local do Codex.** A instalação pelo GitHub fica disponível no computador. Para usar pelo navegador, a conta precisa ter acesso a um plugin configurado no ChatGPT web. Os dois clientes acessam o mesmo servidor da Meta por HTTPS.

### Pedido pronto para colar no agente

> Configure o Meta Ads MCP – Gestão para eu usar no navegador e no Codex local. No workspace atual do ChatGPT, procure uma conexão com o servidor https://mcp.facebook.com/ads que funcione na web. Se precisar criá-la, siga a seção do navegador abaixo. Para o Codex, baixe https://github.com/zaip-ai/zaip-plugin-meta-ads-mcp-gestao ou reutilize a cópia existente e instale o plugin no meu perfil de usuário. Abra o OAuth quando eu precisar autorizar a Meta. Verifique o Codex fora da pasta do projeto e o ChatGPT em uma nova conversa no navegador. Em cada cliente, teste somente a listagem das contas de anúncios e informe o resultado.

### ChatGPT no navegador

1. Abra **Plugins** no workspace em que pretende usar o Meta Ads. Se já houver um plugin para o endpoint `https://mcp.facebook.com/ads` disponível na web, abra-o e conecte sua conta Meta. Um pacote importado do GitHub pode receber o selo **Desktop only**, mesmo usando HTTPS. [Disponibilidade de plugins importados](https://learn.chatgpt.com/docs/enterprise/plugin-management#desktop-only-plugins).
2. Para cadastrar o servidor na web, use **Plugins → + → Add custom MCP server**. Informe o nome **Meta Ads MCP – Gestão**, o endpoint `https://mcp.facebook.com/ads` e a autenticação **OAuth**. Selecione **Create as a plugin**, confira as ferramentas descobertas e instale a conexão criada. Esse cadastro é próprio do ChatGPT e usa o mesmo servidor configurado no pacote local. [Guia de conexão de MCPs no ChatGPT](https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt).
3. No Business, o cadastro exige um administrador ou proprietário. No Enterprise/Edu, um membro também pode receber permissão para criar e testar a conexão. Para disponibilizá-la a outros membros, um administrador ou proprietário publica o plugin para os papéis desejados. A disponibilidade depende do plano e das permissões do workspace. [Permissões e publicação](https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt).
4. Depois do OAuth, abra uma nova conversa **no navegador**, selecione o plugin com `@` e peça que liste suas contas de anúncios.

## Instalação local no dot ou no Codex

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

### 2B. Instale no perfil de usuário do Codex

Na raiz da pasta baixada, execute os comandos com o perfil habitual do Codex. O ponto em `marketplace add .` indica a pasta atual. Esse comando registra o catálogo local. O comando seguinte instala o plugin no perfil de usuário ativo. Para conferir o alcance da instalação, abra um terminal em outra pasta com o mesmo perfil e repita os dois comandos de listagem.

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
