# Meta Ads MCP – Gestão

Cole esta mensagem no **Codex** ou no **Dot** da pessoa que vai usar os anúncios:

```text
instale esse plugin https://github.com/zaip-ai/zaip-plugin-meta-ads-mcp-gestao
```

A pessoa pode estar em outro workspace. Basta enviar a frase, sem anexos. Na primeira tentativa, o assistente segue a [skill padrão de instalação](plugins/meta-ads-gestao/skills/configurar-meta-ads-mcp/SKILL.md) sem pedir acesso ao navegador nem outro login no ChatGPT. Quando aparecer a autorização da Meta, a própria pessoa entra, escolhe os ativos e aprova as permissões na tela oficial. Nunca envie senhas, códigos ou tokens no chat.

## O que o assistente faz com o link

1. **No Codex local**, lê o catálogo deste repositório, registra ou atualiza a fonte no perfil da pessoa, instala o plugin e confere a versão. Os comandos estão na skill padrão para o assistente executar. A pessoa só precisa atender ao pedido de conexão quando o cliente apresentar o OAuth.
2. **No Dot ou Work**, procura o conector no workspace onde recebeu a mensagem. Se encontrá-lo, reutiliza a conexão ou apresenta **Instalar → Conectar**. Se o cliente permitir cadastrar o servidor diretamente, o assistente usa essa operação. Um link do GitHub identifica o pacote e seus parâmetros. A instalação no Codex local não registra o conector em outro workspace.
3. **Se o Dot não puder cadastrar o servidor**, o assistente informa a etapa pendente. A pessoa ou um administrador pode usar o caminho manual abaixo uma vez naquele workspace. Os demais usuários com acesso podem instalar a cópia disponibilizada ali e autorizar a própria conta Meta. Ninguém precisa liberar controle do navegador para fazer esses cliques.
4. **Depois da autorização**, o assistente testa a leitura no cliente escolhido e informa o resultado. Um plugin instalado pode ainda estar aguardando a conexão da Meta.

**Alternativa com navegador.** Se o fluxo padrão parar no cadastro web e você quiser que o assistente conduza os cliques, envie `Use $configurar-meta-ads-no-chatgpt com Computer Use e retome de onde parou.` A [skill com navegador](plugins/meta-ads-gestao/skills/configurar-meta-ads-no-chatgpt/SKILL.md) deixa o login e o consentimento sob seu controle. Se preferir receber os arquivos avulsos, anexe ao chat a [skill padrão](skills/configurar-meta-ads-mcp/SKILL.md) e o [ícone PNG](assets/meta-ads-icon.png) junto com a mesma mensagem.

## Como configurar manualmente

Use estes passos quando o cadastro do conector precisar ser feito pela pessoa ou pelo administrador do workspace.

1. Abra **Plugins → Pessoal** na conta e no espaço de trabalho em que usará o conector. Procure **Meta Ads MCP – Gestão** e confira se os detalhes mostram o servidor `https://mcp.facebook.com/ads`. Se já estiver conectado ao servidor correto, siga para o teste abaixo. Se encontrar o conector correto ainda desconectado, clique em **Conectar** e conclua a autorização na Meta. [Abrir Plugins no ChatGPT](https://chatgpt.com/plugins)
2. Se o conector estiver ausente, abra **Plugins → + → Adicionar servidor MCP personalizado**.
3. Em **Nome**, digite **Meta Ads MCP – Gestão**. Em **Escolher ícone**, selecione o arquivo [meta-ads-icon.png](assets/meta-ads-icon.png) que você baixou. Se quiser preencher a descrição, use “Consulte relatórios e gerencie campanhas nas contas autorizadas pela Meta. Alterações somente após confirmação explícita.”
4. Em **URL do servidor**, cole `https://mcp.facebook.com/ads`. Selecione **OAuth** para autorizar o acesso pela Meta. Nas configurações avançadas, aguarde o ChatGPT identificar as opções do servidor. Escolha **Registro dinâmico de cliente (DCR)** se essa opção aparecer.
5. Confira as permissões oferecidas conforme a tabela abaixo. Revise o aviso na tela e escolha **Criar como plugin**. Se aparecer **Instalar**, instale na sua conta. Clique em **Continuar** ou **Conectar**, faça login na página oficial da Meta e autorize os ativos escolhidos. Ao voltar ao ChatGPT, confira a conexão nos detalhes do plugin.

### Quais permissões escolher?

| Para quê | O que autorizar, se a Meta oferecer |
| --- | --- |
| Consultar relatórios | `ads_read` e `ads_mcp_management` para usar o conector e ler os resultados. |
| Gerir campanhas | Acrescente `ads_management` se também quiser fazer alterações. |
| Acessar outros ativos | Escolha apenas o que pretende usar. `business_management` para o portfólio empresarial, `catalog_management` para catálogos, `pages_show_list` para listar Páginas e `pages_manage_ads` para anúncios vinculados às Páginas. |
| Trabalhar com Instagram ou anúncios de parceria | `instagram_basic` para o perfil e mídias do Instagram. Para anúncios de parceria, `facebook_branded_content_ads_brand` no Facebook e `instagram_branded_content_ads_brand` no Instagram. |

O acesso depende do seu perfil e dos ativos escolhidos na Meta. Mesmo com permissão de gestão, o assistente deve apresentar a ação e aguardar sua confirmação explícita antes de cada criação, edição, publicação, ativação, mudança de orçamento ou exclusão. [Referência de permissões da Meta](https://developers.facebook.com/documentation/development/permissions)

## Teste de aceitação após a autorização

Abra uma conversa no cliente em que pretende usar o plugin. No Dot ou no Work, confirme o espaço de trabalho. Se precisar selecionar o plugin, digite **@** e escolha **Meta Ads MCP – Gestão**. Cole este pedido:

```text
Liste minhas contas de anúncios acessíveis. Se a lista estiver vazia, avise e pare. Se houver mais de uma, pergunte qual usar e espere minha escolha. Na conta escolhida, consulte os últimos sete dias. Mostre as datas, a moeda e as métricas disponíveis, como gasto e impressões. Se não houver dados, diga isso.

Confira nas ferramentas do conector quais ações de gestão aparecem para campanhas, conjuntos, anúncios e criativos. Apenas liste essas ações. Não execute nenhuma delas.
```

O teste está completo quando o assistente identifica a conta, traz a resposta da consulta para o período e informa as ações visíveis, inclusive se houver apenas leitura. Uma lista de contas vazia impede testar o relatório. Se você pretende usar o **Dot** e só testou no **Work**, repita o teste no Dot para confirmar que ele também tem acesso.

## Se algo impedir a configuração

- **O botão + não aparece.** Confira a conta e o espaço de trabalho no ChatGPT Web. Peça ao administrador para verificar se o plano e seu perfil permitem criar conectores (**Create plugins with MCPs**) ou se há um plugin aprovado que você pode instalar. [Guia da OpenAI para conexões MCP](https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt)
- **O Work diz “Não foi possível carregar o conector” ou o Dot não o encontra.** Confira **Plugins → Instalados** no mesmo espaço de trabalho. Se houver uma cópia oficial disponível, abra-a, conecte sua conta e selecione o plugin em uma nova conversa. Se faltar o conector, use o cadastro manual acima ou peça ao administrador acesso à cópia do seu espaço de trabalho.
- **A descoberta do OAuth falhou ou o formulário exige credenciais de aplicativo.** Confira a URL HTTPS e tente novamente. Se o formulário continuar bloqueado, informe ao administrador em qual etapa parou. Mantenha senhas, tokens e segredos fora do chat.
- **Só aparece leitura.** Confira se você pediu gestão, se a Meta concedeu `ads_management` para a conta escolhida e se o espaço de trabalho permite essas ações.

Um ZIP exportado de outro plugin pode guardar uma referência ao conector que já foi registrado na conta de origem. Importá-lo não transfere a conexão nem a autorização da Meta. Cada pessoa conclui a autorização na própria conta.
