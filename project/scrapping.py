from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch() #usa um browser da propria biblio
    page = browser.new_page()

    #abre a página do STJ
    page.goto("https://scon.stj.jus.br/SCON/sumstj/")

    # vai para a página de súmulas
    page.click("a[href='/SCON/pesquisar.jsp?b=SUMU&tipo=sumula']")

    #agora eu queremos que ele vá para o select e selecione 100 súmulas
    page.select_option("#qtdDocsPagina", "100")

    #page.screenshot(path="example2.png")

    page.wait_for_load_state("networkidle") #espera a página recarregar depois de mudar para 100 itens

    #nosso dicionario com as súmulas, ramo e numero da súmula
    resultados = {}

    while True:
        # pega as da página atual
        elements = page.locator("div.gridSumula")
        total = elements.count()

        print(f"elementos encontrados nesta página: {total}")

        for i in range(total):
            e = elements.nth(i) #pega a sumula 0, 1, 2 sucessivamente até 100

            #verifica se a súmula foi cancelada, se foi cancelada passa para a próxima
            if e.locator("span.clsINDE").count() > 0:
                continue
            numero_sumula = e.locator("span.numeroSumula").inner_text().strip()
            ramo = e.locator("span.ramoSumula").inner_text().strip()

            #não há um padrão bem defenido para a súmula, então pegamos a div que ela pertence e fazemos algumas alterações
            texto_completo = e.locator("div.blocoVerbete").inner_text().strip()

            # remove o ramo contido no texto.
            sumula = texto_completo.replace(ramo, "").strip()

            resultados[numero_sumula] = {
                    "ramo": ramo,
                    "texto": sumula
                }

        # aqui acabou os primeiros 100 elementos, precisamos agora ir para a próxima página.
        # tenta clicar em "Próxima página"
        next_buttons = page.locator("a.iconeProximaPagina")
        if next_buttons.count() == 0:
            break  # não há próxima página, fim
        next_buttons.first.click()
        page.wait_for_load_state("networkidle")

    # imprime resultados
    '''
    for numero, info in resultados.items():
        print("\nnumero =", numero)
        print("ramo =", info["ramo"])
        print("sumula =", info["texto"])
    '''

    #print(len(resultados))

    browser.close()

def retorna_dicinario():
    return resultados
