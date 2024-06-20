estacionamento = {}

def menu():
    print("\nMenu:")
    print("1 - Estacionar veículo")
    print("2 - Retirar veículo")
    print("3 - Veículos estacionados")
    print("4 - Está estacionado?")
    print("0 - Sair")
    return int(input("Escolha uma opção: "))

def estacionar_veiculo():
    placa = input("Digite a placa do veículo: ")
    if placa in estacionamento:
        print("Veículo já está estacionado.")
    else:
        marca = input("Digite a marca do veículo: ")
        modelo = input("Digite o modelo do veículo: ")
        cor = input("Digite a cor do veículo: ")
        proprietario = input("Digite o nome do proprietário: ")
        estacionamento[placa] = {'marca': marca, 'modelo': modelo, 'cor': cor, 'proprietario': proprietario}
        print("Veículo estacionado com sucesso.")

def retirar_veiculo():
    placa = input("Digite a placa do veículo a ser retirado: ")
    if placa in estacionamento:
        del estacionamento[placa]
        print("Veículo retirado com sucesso.")
    else:
        print("Veículo não encontrado.")

def veiculos_estacionados():
    if estacionamento:
        print("\nVeículos estacionados:")
        for placa, dados in estacionamento.items():
            print(f"Placa: {placa}, Marca: {dados['marca']}, Modelo: {dados['modelo']}, Cor: {dados['cor']}, Proprietário: {dados['proprietario']}")
    else:
        print("Não há veículos estacionados.")

def esta_estacionado():
    placa = input("Digite a placa do veículo: ")
    if placa in estacionamento:
        print("O veículo está estacionado.")
    else:
        print("O veículo não está estacionado.")

def main():
    while True:
        opcao = menu()
        if opcao == 1:
            estacionar_veiculo()
        elif opcao == 2:
            retirar_veiculo()
        elif opcao == 3:
            veiculos_estacionados()
        elif opcao == 4:
            esta_estacionado()
        elif opcao == 0:
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executando a função principal
if __name__ == "__main__":
    main()