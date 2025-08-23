// script com 3 menus completos


#include <iostream>
#include <limits> // Para usar numeric_limits
#include <stdlib.h>
#include <cstdlib>
#include <string>
using namespace std;

// declara��o de variaveis
    int entrada, saida, idade, horas, dias;
    string descricao, nome, funcionario, cargo;
    float altura, num1, num2, salhora, saldia, salmes, vt, inss, fgts, liquido;
    double peso;
int main() {
    int opcao;
    system("clear");
    int escolha;
    while (escolha != 4) {
        system("clear");
        cout << "Menu:\n";
        cout << "1. Menu I\n";
        cout << "2. Menu II \n";
        cout << "3. Menu III \n";
        cout << "4. Sair\n";
        cout << "Escolha uma op��o: "; cin >> escolha;
        switch (escolha) {
          case 1: cout << "Voc� escolheu a op��o Menu I\n";
            // Exibe o menu I *****************************************
            do {
            cout <<"====| MENU PRINCIPAL II |====" << endl << endl;
            cout << "Op��o 1 - CADASTRO DE PRODUTOS" << endl;
            cout << "Op��o 2 - CADASTRO DE PESSOAS" << endl;
            cout << "Op��o 3 - CALCULADORA " << endl;
            cout << "Op��o 0 - Sair"  << endl;
            cout << "Escolha uma op��o: "; cin >> opcao;
            // Limpa o buffer do teclado (evitar entradas inv�lidas)
            cin.ignore(numeric_limits<streamsize>::max(),'\n');
            // Processa a op��o escolhida
                switch (opcao) {
                    case 1:
                        system("clear");
                        cout <<"====| CADASTRO DE PRODUTOS |====" << endl;
                        cout << "Descricao do Produto: ";  getline(cin, descricao);
                        cout << "Quantidade de Entrada: "; cin >> entrada;
                        cout << "Quantidade de Saida: "; cin >> saida;
                        cout <<"====| ESTOQUE DE PRODUTOS |====" << endl;
                        cout <<"Produto Digitado:" << descricao << endl;
                        cout <<"Estoque Atual: " << entrada - saida << endl;
                        if (saida >= entrada) { cout << "Repor Estoque" << endl;}
                        else { cout << "Estoque OK" << endl;}
                        cout <<"===========| FIM |============" << endl;
                        cout << "Fun��o 1 executada." << endl;
                        break;
                    case 2:
                            system("clear");
                        cout <<"====| CADASTRO DE PESSOAS |====" << endl << endl;
                        cout << "Digite seu nome: ";  getline(cin, nome);
                        cout << "Digite sua idade: "; cin >> idade;
                        cout << "Digite sua altura:"; cin >> altura;
                        cout << "Digite seu peso:";   cin >> peso;
                        cout <<"========| RESULTADOS |=========" << endl << endl;
                        cout << "Ol�, " << nome << "! Voc� tem " << idade << " anos." << endl;
                        cout << "sua altura de " << altura << " e seu peso de " << peso << endl;
                        cout <<"===========| FIM |============" << endl;
                        cout << "Fun��o 2 executada." << endl;
                        break;
                    case 3:
                        system("clear");
                        cout <<"======| CALCULADORA  |======" << endl << endl;
                        cout << "Primeiro numero: ";  cin >> num1;
                        cout << "Segundo numero: ";   cin >> num2;
                        cout <<"======| RESULTADOS  |======" << endl << endl;
                        cout << "Soma         : " << num1 + num2 << endl;
                        cout << "Subtracao    : " << num1 - num2 << endl;
                        cout << "Multiplicacao: " << num1 * num2 << endl;
                        cout << "Divisao      : " << num1 / num2 << endl;
                        cout <<"==========| FIM |==========" << endl;
                        cout << "Fun��o 3 executada." << endl;
                        break;
                    case 0:
                        cout << "Saindo...\n";
                        break;
                    default:
                        cout << "Op��o inv�lida. Tente novamente.\n";
                }
            } while (opcao != 0);
            break;
        case 2: cout << "Voc� escolheu a op��o Menu II\n";
              system("clear");
            // Exibe o menu
            do {
            cout <<"====| MENU PRINCIPAL - CONTROLE DE PAGAMENTO |====" << endl << endl;
            cout << "Op��o 1 - CADASTRO DE DADOS" << endl;
            cout << "Op��o 2 - CONSULTA DE DADOS" << endl;
            cout << "Op��o 3 - CALCULO DOS DESCONTOS " << endl;
            cout << "Op��o 0 - SAIR"  << endl;
            cout << "Escolha uma op��o: "; cin >> opcao;
            // Limpa o buffer do teclado (evitar entradas inv�lidas)
            cin.ignore(numeric_limits<streamsize>::max(),'\n');
            switch (opcao) {
              case 1:
                  system("clear");
                  cout <<"======| CONTROLE DE PAGAMENTO  |======" << endl << endl;
                  cout << "Digite o Nome do funcionario: "; getline (cin, funcionario);
                  cout << "Digite o Cargo do funcionario: "; getline (cin, cargo);
                  cout << "Digite a Quantidade de Horas Diarias: "; cin >> horas;
                  cout << "Digite o Valor do Salario por Hora: "; cin >> salhora;
                  cout << "Digite a Quantidade de dias trabalhados: ";   cin >> dias ;
                  cout << "\n======| DADOS CADASTRADOS  |======" << endl << endl;
              break;
              case 2:
                 system("clear");
                  cout <<"======| RESULTADOS DO FUNCIONARIO |======" << endl << endl;
                  cout << "Nome do funcionario: " << funcionario << endl;
                  cout << "Cargo do funcionario: " << cargo << endl;
                  saldia = horas * salhora ; // Calculando o salario por dia
                  cout << "Salario por Dia: " << saldia << endl;
                  salmes= saldia * dias; // Calculando o salario por mes
                  cout << "Salario por mes: " << salmes << endl << endl ;
              break;
              case 3:
                  system("clear");
                  cout <<"======| CALCULANDO DESCONTOS |======" << endl << endl;
                  cout << "Nome do funcionario: " << funcionario << endl;
                  // Calculando os descontos
                  vt = salmes * 0.06; // Vale transporte de 6% do salario
                  cout << "Desconto de Vale transporte de 6%: " << vt << endl;
                  inss = salmes * 0.07; // Desconto de INSS 7% do salario
                  cout << "Desconto do INSS de 7%: " << inss << endl;
                  fgts = salmes * 0.08; // Desconto do FGTS 8% do salario
                  cout << "Desconto do FGTS de 8%: " << fgts << endl;
                  // Calculando o salario liquido a receber
                  liquido = salmes - ( vt + inss + fgts );
                  cout << "Salario Liquido a receber: " << liquido << endl << endl;
              break;
              case 0:
                  cout << "Saindo...\n";
                  break;
              default:
                        cout << "Op��o inv�lida. Tente novamente.\n";
              break;
               }
            } while (opcao != 0);
          cout <<"==========| SISTEMA FINALIZADO |=========" << endl << endl;
          break;
        case 3:

            int escolha;
            do {
            cout << "\nMenu:\n";
            cout << "1. Calculadora\n";
            cout << "2. Calcula a Media\n";
            cout << "3. Contador\n";
            cout << "4. Dias da Semana\n";
            cout << "5. Sair\n";
            cout << "Escolha uma op��o: ";
            cin >> escolha;
            // Tratamento de entrada inv�lida
            while (cin.fail() || escolha < 1 || escolha > 5) {
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
                cout << "Op��o inv�lida. Digite um n�mero entre 1 e 5: ";
                cin >> escolha;
            }
            switch (escolha) {
              case 1:
                cout << "Voc� escolheu a Calculadora\n";
                // Adicione aqui o c�digo para a op��o 1
                float num1, num2;
                //Recebendo os dados
                cout << "Primeiro numero: "; cin >> num1;
                cout << "Segundo numero: "; cin >> num2;
                //Exibindo as opera��es
                cout << "Soma         : " << num1 + num2 << endl;
                cout << "Subtracao    : " << num1 - num2 << endl;
                cout << "Multiplicacao: " << num1 * num2 << endl;
                cout << "Divisao      : " << num1 / num2 << endl;
                break;

              case 2:
                cout << "Voc� escolheu a Calcula a Media\n";
                float nota1, nota2, nota3, nota4, media;
                cout <<"======| CALCULA MEDIA DE NOTAS  |======" << endl << endl;
                cout << "Digite a primeira nota: ";  cin >> nota1;
                cout << "Digite a segunda nota: ";   cin >> nota2;
                cout << "Digite a terceira nota: ";  cin >> nota3;
                cout << "Digite a quarta nota: ";    cin >> nota4;
                media = (nota1 + nota2 + nota3 + nota4) / 4;
                cout <<"======| RESULTADOS  |======" << endl << endl;
                cout << "A media: " << media << endl;
                if (media >= 7) {
                    cout << "Aprovado" << endl;
                } else {
                    cout << "Reprovado" << endl;
                }
                break;
              case 3:
                   cout << "Voc� escolheu o Contador\n";
                   int numero;
                    cout << "Digite um Numero maior que 0 :" ;
                    cin >> numero;
                    for (int i = numero; i >= 0; --i) {
                        cout << "Contando:" << i << endl;
                    }
                break;
              case 4:
               cout << "Voc� escolheu os Dias da Semana\n";
               int dia;
                cout << "Digite de 1-7 para dias da semana: ";
                cin >> dia;
                switch (dia) {
                    case 1:
                        cout << "Domingo" << endl;
                        break;
                    case 2:
                        cout << "Segunda-feira" << endl;
                        break;
                    case 3:
                        cout << "Ter�a-feira" << endl;
                        break;
                    default:
                        cout << "Dia inv�lido" << endl;
                }
               break;
            case 5:
                cout << "Saindo...\n";
                break;
            }
          } while (escolha != 5);
          return 0;
        cout << "Op��o inv�lida. Tente novamente.\n";

    case 4:
        cout << "Saindo...\n";
        break;
}
    //default:
        cout << "Op��o inv�lida. Tente novamente.\n";
  return 0;
 }
}


















