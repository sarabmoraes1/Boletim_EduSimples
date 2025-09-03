class Aluno:
    def __init__(self, matricula, nome, n1, n2):
        self.matricula = matricula
        self.nome = nome
        self.n1 = n1
        self.n2 = n2

    def media(self):
        return (self.n1 + self.n2) / 2

    def situacao(self):
        m = self.media()
        if m >= 7:
            return "Aprovado"
        elif m >= 4:
            return "Recuperação"
        else:
            return "Reprovado"

alunos = []

def cadastrar():
    try:
        matricula = input("Digite a matrícula do aluno: ").strip()
        nome = input("Digite o nome do aluno: ").strip()
        n1 = float(input("Digite a primeira nota: "))
        n2 = float(input("Digite a segunda nota: "))
        aluno = Aluno(matricula, nome, n1, n2)
        alunos.append(aluno)
        print(f"Aluno {nome} cadastrado com sucesso!")
    except ValueError:
        print("Erro: Digite valores numéricos válidos para as notas.")

def alterar():
    matricula = input("Digite a matrícula do aluno que deseja alterar: ").strip()
    for a in alunos:
        if a.matricula == matricula:
            try:
                a.nome = input("Digite o novo nome: ").strip()
                n1_input = input("Digite a nova primeira nota: ").replace(',', '.')
                n2_input = input("Digite a nova segunda nota: ").replace(',', '.')
                a.n1 = float(n1_input)
                a.n2 = float(n2_input)
                print("Dados alterados com sucesso!")
                return
            except ValueError:
                print("Erro: Digite valores numéricos válidos para as notas.")
                return
    print("Aluno não encontrado.")


def excluir():
    matricula = input("Digite a matrícula do aluno que deseja excluir: ").strip()
    for a in alunos:
        if a.matricula == matricula:
            alunos.remove(a)
            print(f"Aluno {a.nome} excluído com sucesso!")
            return
    print("Aluno não encontrado.")


def listar():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    print("\nLista de alunos:")
    print("Matrícula | Nome | Nota 1 | Nota 2 | Média | Situação")
    for a in alunos:
        print(f"{a.matricula} | {a.nome} | {a.n1} | {a.n2} | {a.media():.2f} | {a.situacao()}")




while True:
    try:
        opcao = int(input("\nDigite: 1 - Cadastrar, 2 - Alterar, 3 - Excluir, 4 - Listar, 5 - Sair: "))
        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            alterar()
        elif opcao == 3:
            excluir()
        elif opcao == 4:
            listar()
        elif opcao == 5:
            print("Sistema finalizado com sucesso!!!!")
            break
        else:
            print("Opção inválida!")
    except ValueError:
        print("Digite um número válido para a opção.")
