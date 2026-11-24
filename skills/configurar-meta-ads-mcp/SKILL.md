---
name: configurar-meta-ads-mcp
description: Instale o Meta Ads MCP – Gestão pelo repositório. No Work ou Dot, cadastre o conector web com Computer Use. No Codex local, instale pelo catálogo.
---

# Instalar o Meta Ads MCP – Gestão

Ao receber “instale esse plugin” com o link do projeto, use o procedimento do cliente em que a pessoa quer usar o plugin.

## No ChatGPT Work ou Dot

Execute diretamente a skill `configurar-meta-ads-no-chatgpt`, incluída no pacote. Se recebeu apenas este arquivo ou o link do GitHub, leia as [instruções de cadastro no Work](https://github.com/zaip-ai/zaip-plugin-meta-ads-mcp-gestao/blob/main/plugins/meta-ads-gestao/skills/configurar-meta-ads-no-chatgpt/SKILL.md) e execute-as com Computer Use. Reutilize a aba do ChatGPT já autenticada. Se faltar, peça que a pessoa abra uma aba com o ChatGPT logado no workspace desejado e aguarde. Procure o conector web, cadastre o servidor somente se faltar e pare no botão **Conectar**, deixando o Facebook com a pessoa. O fluxo do Codex local abaixo só se aplica quando o destino é o Codex.

## No Codex local

1. Trabalhe no perfil local persistente de quem fez o pedido. Confira `codex plugin marketplace list --json` e a origem do catálogo `zaip-meta-ads-plugins`, se existir. Reutilize o catálogo deste repositório. Se o nome já apontar para outra origem, informe o conflito e preserve a configuração existente.
2. Se faltar o catálogo, execute `codex plugin marketplace add https://github.com/zaip-ai/zaip-plugin-meta-ads-mcp-gestao --ref main`. Se o catálogo Git correto já existir, atualize apenas esse catálogo com `codex plugin marketplace upgrade zaip-meta-ads-plugins`. Se for uma fonte local legítima, confira a versão disponível nessa pasta.
3. Consulte `codex plugin list --marketplace zaip-meta-ads-plugins --available --json`. Identifique `meta-ads-gestao` e sua versão. Se faltar a instalação da versão disponível, execute `codex plugin add meta-ads-gestao@zaip-meta-ads-plugins --json`. Verifique a instalação com `codex plugin list --marketplace zaip-meta-ads-plugins --json`. Se o plugin já estiver instalado e habilitado na versão pretendida, prossiga diretamente. Se aparecer desativado, use a opção de habilitar do cliente. Se o chat ainda não carregar as ferramentas após a instalação, oriente abrir uma nova conversa no Codex.
4. Para um pedido de instalação, termine quando o plugin estiver instalado e habilitado. Informe o estado do MCP em `codex mcp list`. Em perfil novo, `not_logged_in` é o resultado esperado. Preserve qualquer vínculo anterior. Deixe a autenticação para quando a pessoa selecionar **Conectar** no cliente. Não execute login nem faça consultas durante a instalação.

## Autorizar e testar no cliente de destino

- Deixe a pessoa escolher os ativos e concluir o OAuth na tela oficial da Meta. Nunca solicite senha, código, token ou segredo no chat. Para leitura, confira `ads_read` e `ads_mcp_management` quando oferecidos. Para gerir campanhas, confira também `ads_management`. Mostre os escopos reais antes do consentimento e respeite a escolha da pessoa.
- Se a pessoa quiser acesso ampliado e a Meta oferecer, explique quais escopos correspondem ao uso pretendido: `business_management` para o portfólio empresarial, `catalog_management` para catálogos, `pages_show_list` e `pages_manage_ads` para Páginas e anúncios vinculados, `instagram_basic` para perfil e mídias, `facebook_branded_content_ads_brand` e `instagram_branded_content_ads_brand` para anúncios de parceria. Não fixe IDs, empresas ou ativos.
- Depois do OAuth, liste as contas acessíveis. Se a lista estiver vazia, informe e pare. Se houver várias, pergunte qual usar e espere a resposta. Consulte os últimos sete dias na conta escolhida e informe datas, moeda e métricas retornadas. Diferencie um período sem dados de uma consulta que falhou. Examine quais ações de gestão aparecem na lista de ferramentas, sem executá-las.
- Informe onde o pacote foi instalado, se a autorização foi concluída e qual consulta funcionou naquele cliente. Se faltou uma etapa, indique qual e como retomá-la. Em usos futuros, apresente a conta, o ativo e a alteração proposta e aguarde confirmação explícita antes de cada criação, edição, publicação, ativação, mudança de orçamento ou exclusão.
