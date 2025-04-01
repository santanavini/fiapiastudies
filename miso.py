print('Bem Vindo ao MISO, Seu programa para cultivo de milho ou soja Digital!')
#Menu 1
print('-----------Menu-------------')

print('1. Informações sobre cultivo de milho')
print('2. Informações sobre cultivo de soja')
print('3. Sair') #aqui é a opção de sair
#daqui para baixo possui loop para a função de menu
# Cálculo de área e dados de plantio
# Menu para escolha de opções
while True:
    cultivo = input('Escolha uma opção: ')
    if cultivo == "1":
        cultivo = "Milho"
        print(f"Maravilha, agora podemos seguir com as informações do cultivo de {cultivo}") #aqui é o menu 2
        print('1. Calcular quantidade de sementes a serem plantadas por metro linear')
        print('2. Calcular Manejo de Insumos')
        print('3. Exibir dados estatísticos como média e desvio padrão') #Dados que serão gerados pelo R e apenas exibidos pelo programa
        print('4 Cadastro de Lista de Insumos')
        print('5 Sair')
        calcular = input('O que você gostaria de realizar? ')
        if calcular == "1": # daqui para baixo é o cálculo da quantidade de sementes (unidades não kg) da cultura milho por metro linear
            print("Perfeito, vamos calcular a quantidade de sementes a serem plantadas por metro linear")
            populacao_desejada = int(input("Digite a população desejada de plantas por hectare: "))
            espacamento = float(input("Digite o espaçamento entre linhas ex 0.50: "))
            altura_milho = float(input("Digite a altura do terreno em m²"))
            largura_milho = float(input("Digite a largura do terreno em m²"))
            area_total = int(altura_milho * largura_milho)
            hectares = (10000)
            area_espacamento = int(area_total / espacamento)
            resultado = (populacao_desejada * hectares / area_espacamento) / 10000
            kg_sementesmilho = (populacao_desejada / 3500) #3500 sementes é a média de peso para um kg de sementes
            falha_germinacao = (kg_sementesmilho * 1.1)
            print (f'Levando em consideração a área de {area_espacamento} metros lineares, este cálculo indica que para atingir uma população de {populacao_desejada} com espaçamento de {espacamento} m entre linhas, deve-se semear {resultado} sementes por metro linear.')
            print (f'Você deve utilizar aproximadamente {falha_germinacao:.2f} kg de sementes de milho para cobrir essa área')
        elif calcular == "2": # Calculo de insumos
                print("Perfeito, vamos calcular o manejo de insumos")
                kg_semente = float(input("Digite a quantidade de sementes utilizadas (kg): "))
                area_hectares = float(input("Digite a área total em hectares: "))

        # Cálculo dos insumos (apenas dose máxima)

            ## Tratamento de Sementes (Carboxina + Thiram)
                dose_carboxina_ml = (kg_semente / 60) * 150
                dose_carboxina_kg = (dose_carboxina_ml / 1000) * 0.2  # 200g/L = 0.2 kg/L

            ## Inseticida (Metomil)
                dose_metomil_ml = area_hectares * 600
                dose_metomil_kg = (dose_metomil_ml / 1000) * 0.215  # 215g/L = 0.215 kg/L

            # Exibir resultados corrigidos
                print("### RESULTADO DO CÁLCULO DE INSUMOS ###\n")
                print(f"Para {kg_semente:.2f} kg de sementes e {area_hectares:.2f} hectares de plantio, você precisará de:\n")

                print("Tratamento de Sementes (Carboxina + Thiram):")
                print(f" - {dose_carboxina_ml:.2f} mL de solução e {dose_carboxina_kg:.4f} kg do produto\n")

                print("Inseticida (Metomil):")
                print(f" - {dose_metomil_ml:.2f} mL de solução e {dose_metomil_kg:.2f} kg do produto\n")
        elif calcular == "3": # Calculo de insumos
                print("Perfeito, agora vamos exibir os dados estatisticos de média e desvio padrão")
                break
        elif calcular =="4": # ESSA PARTE TRATA VETORES, ADIÇÃO DE ITENS, EDIÇÃO E EXCLUSÃO
                print("Perfeito, agora vamos acessar a nossa lista de insumos")
                insumos = ["Carboxina", "Metomil"]
                print("----------Menu-----------") #aqui é o menu 3
                print("1 - Cadastrar Insumo")
                print("2 - Alterar Insumo")
                print("3 - Excluir Insumo")
                print("4 - Sair")
                print (insumos)
                insumo_lista = int(input('Escolha uma opção: '))
                if insumo_lista == 1:
                   novo_insumo = input("Insira um novo insumo: ")
                   insumos.append(novo_insumo)
                   print(insumos)
                   break
                elif insumo_lista == 2:
                   print('Insumos atuais:', insumos)
                   antigo = input('Qual insumo deseja alterar? ')
                   if antigo in insumos:
                       novo = input('Digite o novo nome do insumo')
                       index = insumos.index(antigo)
                       insumos[index] = novo
                       print("Lista de insumos atualizada:", insumos)
                   else:
                       print('Insumo não encontrado!')
                elif insumo_lista == 3:
                    print('Insumos atuais:', insumos)
                    excluir = input("Qual insumo deseja excluir? ")
                    if excluir in insumos:
                        index_tres = insumos.index(excluir)
                        insumos.pop(index_tres)
                        print(insumos)
                break
        if calcular == 5:
            print("Você saiu do sistema")




    if cultivo == "2":
        cultivo = "Soja"
        print('1. Calcular quantidade de sementes a serem plantadas por metro linear') #aqui é o menu 4
        print('2. Calcular Manejo de Insumos')
        print('3. Exibir dados estatísticos como média e desvio padrão')  # Dados que serão gerados pelo R e apenas exibidos pelo programa
        print('4. Cadastro de Lista de Insumos')
        print('5. Sair')
        print(f"Maravilha, agora podemos seguir com as informações do cultivo de {cultivo}")
        calcular_soja = input('O que você gostaria fazer? ')
        if calcular_soja == "1":
            populacao_desejada_soja = int(input("Digite a população desejada de plantas por hectare: "))
            germinacao = float(input("Digite a taxa de germinação da semente em %: "))
            total_sementes_soja = (populacao_desejada_soja / germinacao)
            espacamento_soja = float(input("Digite o espaçamento entre linhas ex 0.50: "))
            altura_soja = float(input("Digite a altura do terreno em m²"))
            largura_soja = float(input("Digite a largura do terreno em m²"))
            area_soja = int(altura_soja * largura_soja)
            resultado_soja = int((populacao_desejada_soja / germinacao)) #333.333
            area_espacamento_soja = int(area_soja / espacamento_soja)#20.000
            print(area_espacamento_soja)
            total_soja = float((resultado_soja / area_espacamento_soja))*100
            print(f'Total de sementes necessárias para  cobrir a área de {area_soja}m² é de {resultado_soja} sementes. E para cada metro linear é necessário {int(total_soja)} sementes /metro.')
        break



    else:
        print('Fornecemos informação apenas para milho e soja. Tente novamente.')

    if cultivo == "3":
        print('Você saiu do sistema!')
        break