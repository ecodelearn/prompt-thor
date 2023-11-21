def substituir_assunto_no_prompt():
    # Prompt original
    prompt_original = ("Prompt: \"Crie uma imagem minimalista onde o céu é de um azul claro, "
                       "preenchido com uma miríade de estrelas mais tênues, e talvez um indício de "
                       "uma galáxia distante ou nebulosa para adicionar profundidade e contraste de cor. "
                       "No centro deste pano de fundo tranquilo, a única luz vem de uma série de relâmpagos "
                       "grossos e irregulares. Estes relâmpagos são o ponto focal da imagem, convergindo para "
                       "formar um contorno marcante de um [ASSUNTO] diretamente no centro. Não deve haver "
                       "outros detalhes ou objetos, apenas a forma clara e inconfundível de um [ASSUNTO] "
                       "composto por esses poucos poderosos traços de relâmpago. A imagem deve evocar a "
                       "simplicidade e elegância de um desenho de linha, com o contorno do [ASSUNTO] "
                       "brilhando vividamente contra o sereno céu noturno.\"")

    while True:
        # Perguntar ao usuário o que ele deseja fazer
        escolha = input("Digite '1' para criar um novo prompt ou '2' para sair do programa: ")

        if escolha == '1':
            # Solicitar ao usuário para inserir o assunto desejado
            assunto = input("Digite o assunto desejado para substituir no prompt: ")

            # Substituir [ASSUNTO] no prompt pelo assunto fornecido
            prompt_modificado = prompt_original.replace("ASSUNTO", assunto)
            print("\nPrompt Modificado:\n", prompt_modificado)
        
        elif escolha == '2':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, digite '1' ou '2'.")

# Executar a função
substituir_assunto_no_prompt()
