# Meta Ads MCP – Gestão

Cole esta mensagem no **ChatGPT Work**, no **Dot** ou no **Codex** da pessoa que vai usar os anúncios:

```text
instale esse plugin https://github.com/zaip-ai/zaip-plugin-meta-ads-mcp-gestao
```

## O que acontece no Work

**Para o assistente que recebeu o pedido:** use Computer Use agora e execute a [skill de cadastro do servidor no Work](plugins/meta-ads-gestao/skills/configurar-meta-ads-no-chatgpt/SKILL.md) na aba do usuário. O destino é o conector web no workspace em que a pessoa quer usar os anúncios. O pacote de desktop e o upload de ZIP não criam esse cadastro.

1. O assistente procura a aba do ChatGPT em que você já está logado. Se não houver uma aba autenticada, ele pede que você abra o ChatGPT no seu navegador, entre no workspace desejado e avise para continuar. Se o navegador solicitar acesso à aba pelo Computer Use, permita o acesso à aba que deseja usar.
2. Na mesma aba, ele procura o conector web para `https://mcp.facebook.com/ads`. Se faltar, usa **Adicionar servidor MCP personalizado** para cadastrar **Meta Ads MCP – Gestão** com OAuth e registro dinâmico de cliente (DCR), quando oferecido.
3. O assistente instala o conector, se necessário, abre os detalhes e **para assim que aparece Conectar**. Você decide quando clicar e autorizar sua conta Facebook. Se já houver uma conta vinculada, ele preserva a conexão. Se o ChatGPT abrir a autorização da Meta automaticamente, ele entrega o controle a você nessa tela.

No **Codex local**, o mesmo pedido instala o pacote pelo catálogo do repositório, sem controlar o navegador. A [skill de instalação](plugins/meta-ads-gestao/skills/configurar-meta-ads-mcp/SKILL.md) orienta o assistente nesse caso.

## Como configurar manualmente

Use estes passos quando o cadastro do conector precisar ser feito pela pessoa ou pelo administrador do workspace.

1. Abra **Plugins → Pessoal** na conta e no espaço de trabalho em que usará o conector. Procure **Meta Ads MCP – Gestão** e confira se os detalhes mostram o servidor `https://mcp.facebook.com/ads`. Se já houver uma conta conectada ao servidor correto, a instalação está concluída. Se o conector já aparece com **Conectar**, o cadastro está pronto. [Abrir Plugins no ChatGPT](https://chatgpt.com/plugins)
2. Se o conector estiver ausente, abra **Plugins → + → Adicionar servidor MCP personalizado**.
3. Em **Nome**, digite **Meta Ads MCP – Gestão**. Em **Escolher ícone**, selecione o arquivo [meta-ads-icon.png](assets/meta-ads-icon.png) que você baixou. Se quiser preencher a descrição, use “Consulte relatórios e gerencie campanhas nas contas autorizadas pela Meta. Alterações somente após confirmação explícita.”
4. Em **URL do servidor**, cole `https://mcp.facebook.com/ads`. Selecione **OAuth** para autorizar o acesso pela Meta. Nas configurações avançadas, aguarde o ChatGPT identificar as opções do servidor. Escolha **Registro dinâmico de cliente (DCR)** se essa opção aparecer.
5. Confira as permissões oferecidas conforme a tabela abaixo. Revise o aviso na tela e escolha **Criar como plugin**. Se aparecer **Instalar**, instale na sua conta. Para deixar o vínculo pendente, pare nos detalhes do plugin assim que aparecer **Conectar**. Se o host exigir consentimento já no cadastro, a própria pessoa decide se deseja prosseguir.

### O que significam Read e Write no ChatGPT?

Na tela de detalhes do aplicativo **Meta Ads MCP – Gestão** mostrada no print, o ChatGPT agrupou as ferramentas do conector em **Read (66 ações de leitura)** e **Write (51 ações de escrita)**. Abra cada grupo para ver quais ações aparecem na sua instalação.

- **Read** permite fazer consultas, como ver quanto uma campanha gastou e quantas impressões recebeu. A consulta preserva os dados da campanha.
- **Write** reúne ações que podem mudar dados ou permissões, como pausar um anúncio, alterar um orçamento ou revogar uma autorização de parceria. O assistente deve apresentar a ação e aguardar sua confirmação explícita antes de cada alteração, inclusive criação, edição, publicação, ativação ou exclusão.

Esses números contam as ferramentas exibidas naquela tela. Os **escopos OAuth** abaixo definem o que você autoriza na Meta. Uma ação pode aparecer no ChatGPT e ainda exigir um escopo ou um nível de acesso que você não tem na conta, Página ou catálogo escolhido.

### Quais permissões autorizar na Meta?

Para **consultar relatórios**, use `ads_read` e `ads_mcp_management`, quando oferecidos. Para **gerenciar campanhas**, acrescente `ads_management`. Os demais escopos são opcionais conforme os ativos e as tarefas que você quer autorizar. [Referência de permissões da Meta](https://developers.facebook.com/documentation/development/permissions)

#### Anúncios e relatórios

| Escopo | O que permite |
| --- | --- |
| `ads_read` | Consultar gasto, impressões, cliques e conversões das contas de anúncios autorizadas. O acesso é de leitura. |
| `ads_management` | Consultar, criar e editar campanhas, conjuntos de anúncios e anúncios nas contas autorizadas, inclusive alterar orçamento e status. |
| `ads_mcp_management` | Acessar o servidor MCP de anúncios da Meta. As ações disponíveis dependem também dos demais escopos e do seu acesso aos ativos. |

#### Empresa, catálogo e Páginas

| Escopo | O que permite |
| --- | --- |
| `business_management` | Acessar o portfólio empresarial no Business Manager e consultar ou gerenciar os ativos conforme o papel atribuído ao seu perfil. |
| `catalog_management` | Consultar e gerenciar catálogos de produtos, seus itens e conjuntos de produtos, conforme seu acesso. |
| `pages_show_list` | Listar as Páginas do Facebook às quais você tem acesso. |
| `pages_manage_ads` | Gerenciar anúncios vinculados às Páginas autorizadas. A publicação de posts orgânicos exige outra permissão. |

#### Instagram e anúncios de parceria

| Escopo | O que permite |
| --- | --- |
| `instagram_basic` | Ler dados básicos do perfil profissional e suas mídias. Ler mensagens diretas (DMs) e publicar posts orgânicos exigem outras permissões. |
| `facebook_branded_content_ads_brand` | Ler posts do Facebook em que a marca foi marcada como parceira paga. Permite também consultar, solicitar ou revogar autorizações para veicular anúncios de parceria no Facebook. |
| `instagram_branded_content_ads_brand` | Ler posts do Instagram em que a marca foi marcada como parceira paga e consultar, solicitar ou revogar autorizações para veicular anúncios de parceria no Instagram. |

## Teste de aceitação após a autorização

Abra uma conversa no cliente em que pretende usar o plugin. No Dot ou no Work, confirme o espaço de trabalho. Se precisar selecionar o plugin, digite **@** e escolha **Meta Ads MCP – Gestão**. Cole este pedido:

```text
Liste minhas contas de anúncios acessíveis. Se a lista estiver vazia, avise e pare. Se houver mais de uma, pergunte qual usar e espere minha escolha. Na conta escolhida, consulte os últimos sete dias. Mostre as datas, a moeda e as métricas disponíveis, como gasto e impressões. Se não houver dados, diga isso.

Confira nas ferramentas do conector quais ações de gestão aparecem para campanhas, conjuntos, anúncios e criativos. Apenas liste essas ações. Não execute nenhuma delas.
```

O teste está completo quando o assistente identifica a conta, traz a resposta da consulta para o período e informa as ações visíveis, inclusive se houver apenas leitura. Uma lista de contas vazia impede testar o relatório. Se você pretende usar o **Dot** e só testou no **Work**, repita o teste no Dot para confirmar que ele também tem acesso.

## Se algo impedir a configuração

- **O botão + não aparece.** Confira a conta e o espaço de trabalho no ChatGPT Web. Peça ao administrador para verificar se o plano e seu perfil permitem criar conectores (**Create plugins with MCPs**) ou se há um plugin aprovado que você pode instalar. [Guia da OpenAI para conexões MCP](https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt)
- **O Work diz “Não foi possível carregar o conector” ou o Dot não o encontra.** Confira **Plugins → Instalados** no mesmo espaço de trabalho. Se houver uma cópia oficial disponível, abra os detalhes e confira se o botão **Conectar** está disponível. Se faltar o conector, use o cadastro manual acima ou peça ao administrador acesso à cópia do seu espaço de trabalho.
- **A descoberta do OAuth falhou ou o formulário exige credenciais de aplicativo.** Confira a URL HTTPS e tente novamente. Se o formulário continuar bloqueado, informe ao administrador em qual etapa parou. Mantenha senhas, tokens e segredos fora do chat.
- **Só aparece leitura.** Confira se você pediu gestão, se a Meta concedeu `ads_management` para a conta escolhida e se o espaço de trabalho permite essas ações.

Um ZIP exportado de outro plugin pode guardar uma referência ao conector que já foi registrado na conta de origem. Importá-lo não transfere a conexão nem a autorização da Meta. Cada pessoa conclui a autorização na própria conta.
