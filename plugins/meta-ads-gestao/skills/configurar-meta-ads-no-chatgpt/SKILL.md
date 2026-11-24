---
name: configurar-meta-ads-no-chatgpt
description: Acompanhe o cadastro web do Meta Ads MCP por Computer Use somente quando o fluxo padrão parar em uma etapa do ChatGPT e a pessoa escolher ajuda no navegador.
---

# Alternativa com Computer Use

Retome a etapa pendente da skill padrão [Configurar Meta Ads MCP](../configurar-meta-ads-mcp/SKILL.md) somente após a pessoa aceitar o controle do navegador. O pedido inicial “instale esse plugin” aciona a skill padrão. Se o bloqueio for permissão do workspace, oriente a pessoa a procurar o administrador. A automação exige as mesmas permissões.

1. **Abra o ChatGPT no navegador do usuário.** Use a ferramenta de controle do navegador. Se o usuário indicou uma aba, selecione-a. Caso contrário, reutilize uma aba visível de `https://chatgpt.com/` ou abra o site em uma nova aba visível no navegador dele. Confira o endereço e os controles exibidos antes de agir. Se a ferramenta não conseguir acessar a aba, peça ao usuário que disponibilize o acesso e retome deste ponto.

2. **Deixe o usuário fazer login.** Se o ChatGPT mostrar a opção de entrar, diga “Abri o ChatGPT no seu navegador. Faça login nessa aba e me avise quando terminar.” Entregue o controle e aguarde, sem solicitar senha ou código no chat. Depois do aviso, confira a sessão na aba. Se já houver uma sessão ativa, prossiga diretamente. Se houver dúvida sobre qual workspace usar, confirme com o usuário antes de criar a conexão.

3. **Procure o plugin existente.** Abra as configurações de plugins ou aplicativos do workspace e procure **Meta Ads MCP – Gestão**. Abra os detalhes e confira o servidor quando o endereço estiver visível. Reutilize a entrada correspondente a `https://mcp.facebook.com/ads`. Se o nome coincidir mas o endereço apontar para outro servidor, esclareça a divergência com o usuário. Se já houver uma conta conectada, preserve-a e avance para a conferência do logo e da conexão.

4. **Preencha o cadastro quando necessário.** Na área de plugins, procure **Add custom MCP server** ou o controle equivalente que a tela oferecer. Use o nome **Meta Ads MCP – Gestão**, o endereço `https://mcp.facebook.com/ads`, autenticação **OAuth** e a opção **Create as a plugin**, quando disponível. Se houver escolha de registro do cliente OAuth, use o registro dinâmico (DCR) previsto em `mcp.json`. Para o campo de descrição, use “Consulte relatórios e gerencie campanhas, conjuntos, anúncios e criativos nas contas autorizadas pela Meta. Alterações somente após confirmação explícita.”

5. **Use o logo do pacote.** No campo de ícone, envie o [PNG da Meta incluído no plugin](../../assets/meta-icon.png). Resolva o caminho a partir da pasta desta skill para que o seletor de arquivos receba o arquivo correto mesmo após a instalação. Confira na prévia o símbolo azul da Meta sobre fundo branco e salve. Se o seletor exigir interação manual, indique o caminho absoluto desse PNG ao usuário e retome quando ele selecionar o arquivo. Para um plugin existente com o logo correto, basta conferi-lo. Se faltar o logo, procure o campo na edição dos detalhes. Se a interface ou a permissão impedir o ajuste, informe a pendência específica.

6. **Conecte a conta Meta.** Quando ainda faltar uma conta, acione **Conectar**. Se a criação já tiver aberto o OAuth, continue nessa tela. Explique os escopos de leitura, gestão e acesso ampliado conforme a skill padrão. Deixe o usuário escolher os ativos e conceder as permissões diretamente na Meta. Aguarde o retorno ao ChatGPT e confira a conta em **Contas conectadas**. Use **Conectar outra conta** somente se o usuário tiver pedido uma conexão adicional.

7. **Verifique pelo ChatGPT.** Confira o nome, o logo e a conta conectada na tela de detalhes. Com esse plugin selecionado no mesmo workspace, faça uma consulta de leitura para listar as contas de anúncios acessíveis. Uma lista vazia é uma resposta válida e deve ser relatada como tal. Informe separadamente o que a tela confirmou e o resultado da consulta. Em caso de erro de acesso ou de permissão, indique a etapa pendente. Se houver mais de uma conta, pergunte qual usar e aguarde. Com a conta escolhida, consulte os últimos sete dias e informe as datas, a moeda e as métricas retornadas. Liste as ações de gestão disponíveis sem executá-las. Aplique os escopos e o requisito de confirmação explícita de cada alteração descritos na skill padrão.
