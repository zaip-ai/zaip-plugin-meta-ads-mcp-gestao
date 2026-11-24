# Meta Ads MCP – Gestão

Cole esta mensagem no **Codex** ou no **Dot** da pessoa que vai usar os anúncios:

```text
instale esse plugin https://github.com/zaip-ai/zaip-plugin-meta-ads-mcp-gestao
```

Ao receber o pedido, o Codex instala o pacote no perfil local. No **ChatGPT Work no navegador**, o assistente deve procurar o plugin no workspace atual e, se faltar, usar o **Plugin Creator** para criar ali uma cópia privada com o servidor MCP oficial e devolver o link dela. A [skill de instalação](plugins/meta-ads-gestao/skills/configurar-meta-ads-mcp/SKILL.md) traz os passos para o assistente. A pessoa pode continuar na conversa em que já está autenticada.

## Vincular sua conta Facebook quando quiser

1. Abra o link que o assistente devolver e selecione **Instalar** se o ChatGPT oferecer essa opção.
2. Quando quiser vincular o Facebook, abra **Plugins → Instalados → Meta Ads MCP – Gestão**. Escolha **Conectar**. Se o plugin listar o app da Meta separadamente, abra o app para encontrar o botão.
3. Na tela oficial da Meta, escolha a sua conta, revise as permissões e selecione os ativos. Ao retornar ao ChatGPT, confira **Contas conectadas**. Nunca envie senha, código ou token pelo chat.

O pacote usa OAuth com registro dinâmico de cliente (DCR) e começa sem credenciais. No catálogo local do Codex, a autenticação fica para o uso. No Work, a interface e as políticas do workspace determinam se **Conectar** aparece nos detalhes ou se o host pede autorização antes. Uma instalação em perfil já conectado preserva o vínculo existente. [Como o ChatGPT gerencia conexões](https://help.openai.com/en/articles/20001494-connecting-and-managing-app-accounts-in-chatgpt)

Se o assistente só devolver um tutorial, peça: “Use o Plugin Creator nesta conversa. Salve o pacote privado no meu workspace, devolva o link e deixe a conexão Facebook para mim.” O arquivo pronto para o assistente é o [pacote portátil do plugin](dist/meta-ads-gestao.zip). Ele contém as skills e a definição do MCP, sem vínculo com o workspace de origem. Um upload aceito confirma o salvamento. Se o cliente informar **Somente desktop** ou os detalhes não mostrarem o app com **Conectar**, use o cadastro web abaixo para obter uma conexão MCP registrada no workspace. [Limites da importação pelo GitHub](https://help.openai.com/en/articles/20001504-importing-and-syncing-plugin-marketplaces-from-github)

**Alternativa com navegador.** Se o fluxo padrão parar no cadastro web e você quiser que o assistente conduza os cliques, envie `Use $configurar-meta-ads-no-chatgpt com Computer Use e retome de onde parou.` A [skill com navegador](plugins/meta-ads-gestao/skills/configurar-meta-ads-no-chatgpt/SKILL.md) deixa o login e o consentimento sob seu controle. Se preferir receber os arquivos avulsos, anexe ao chat a [skill padrão](skills/configurar-meta-ads-mcp/SKILL.md) e o [ícone PNG](assets/meta-ads-icon.png) junto com a mesma mensagem.

## Como configurar manualmente

Use estes passos quando o cadastro do conector precisar ser feito pela pessoa ou pelo administrador do workspace.

1. Abra **Plugins → Pessoal** na conta e no espaço de trabalho em que usará o conector. Procure **Meta Ads MCP – Gestão** e confira se os detalhes mostram o servidor `https://mcp.facebook.com/ads`. Se já estiver conectado ao servidor correto, siga para o teste abaixo. Se o conector já aparece com **Conectar**, o cadastro está pronto. [Abrir Plugins no ChatGPT](https://chatgpt.com/plugins)
2. Se o conector estiver ausente, abra **Plugins → + → Adicionar servidor MCP personalizado**.
3. Em **Nome**, digite **Meta Ads MCP – Gestão**. Em **Escolher ícone**, selecione o arquivo [meta-ads-icon.png](assets/meta-ads-icon.png) que você baixou. Se quiser preencher a descrição, use “Consulte relatórios e gerencie campanhas nas contas autorizadas pela Meta. Alterações somente após confirmação explícita.”
4. Em **URL do servidor**, cole `https://mcp.facebook.com/ads`. Selecione **OAuth** para autorizar o acesso pela Meta. Nas configurações avançadas, aguarde o ChatGPT identificar as opções do servidor. Escolha **Registro dinâmico de cliente (DCR)** se essa opção aparecer.
5. Confira as permissões oferecidas conforme a tabela abaixo. Revise o aviso na tela e escolha **Criar como plugin**. Se aparecer **Instalar**, instale na sua conta. Para deixar o vínculo pendente, pare nos detalhes do plugin assim que aparecer **Conectar**. Se o host exigir consentimento já no cadastro, a própria pessoa decide se deseja prosseguir.

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
