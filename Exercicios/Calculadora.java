package Exercicios;
import java.util.Scanner;

public class Calculadora {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        String operacao;

        while (true) {
            System.out.println("\nQual operação você deseja realizar?");
            System.out.println("S  = Soma");
            System.out.println("SB = Subtração");
            System.out.println("M  = Multiplicação");
            System.out.println("D  = Divisão");
            System.out.println("SAIR = Encerrar programa");

            System.out.print("Digite a operação correspondente: ");
            operacao = scanner.nextLine().toUpperCase();

            if (operacao.equals("SAIR")) {
                try {
                    Thread.sleep(1000); // pausa 1 segundo
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
                System.out.println("Programa encerrado.");
                break;
            }

            if (operacao.equals("S") || operacao.equals("SB")
                || operacao.equals("M") || operacao.equals("D")) {
                
                    System.out.print("Digite o primeiro valor: ");
                double num1 = scanner.nextDouble();

                System.out.print("Digite o segundo valor: ");
                double num2 = scanner.nextDouble();
                scanner.nextLine();

                double resultado = 0;

                if (operacao.equals("S")) {
                    resultado = num1 + num2;

                } else if (operacao.equals("SB")) {
                    resultado = num1 - num2;

                } else if (operacao.equals("M")) {
                    resultado = num1 * num2;

                } else if (operacao.equals("D")) {
                    if (num2 == 0) {
                        System.out.println("Erro: Não é possível dividir por zero!");
                        continue;
                    }
                    resultado = num1 / num2;
                }

                System.out.println("O resultado da operação é: " + resultado);

            } else {
                System.out.println("Operação inválida. Escolha uma operação válida.");
            }
        }

        scanner.close();
    }
}