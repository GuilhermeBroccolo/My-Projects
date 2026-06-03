package Exercicios.testes;
import java.util.Scanner;
import java.util.Random;

public class exer {
    public static void main(String[] args) {
        //String nome = "Johnny";
        //String sobrenome = "Cortez";
        //System.out.println("Olá " + nome + " " + sobrenome);
        
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite seu nome: ");
        String nome = scanner.nextLine();

        System.out.println("Digite o seu sobrenome: ");
        String sobrenome = scanner.nextLine();
        
        System.out.println("Olá " + nome + " " + sobrenome);

        System.out.println("Digite a sua idade: ");
        int idade = scanner.nextInt();
        
        if (idade < 0) {
            System.out.println("Idade inválida!");
            return;
        }
        if (idade >=18) {
            System.out.println("Você é maior de idade!");
        } else {
            System.out.println("Você é menor de idade!");
        }

        System.out.println("Você tem " + idade + " anos! " );
        
        Random random = new Random();
        int numeroSecreto = random.nextInt(10) + 1;  // Número de 1 a 10
        int tentativa = -1;
        
        while (tentativa != numeroSecreto) {
            System.out.println("Qual é o seu palpite? ");
            tentativa = scanner.nextInt();
            
            if (tentativa < 1 || tentativa > 10) {
                System.out.println("Por favor, digite um número entre 1 e 10!");
            } else if (tentativa < numeroSecreto) {
                System.out.println("O número é maior!");
            } else if (tentativa > numeroSecreto) {
                System.out.println("O número é menor!");
            } else {
                System.out.println("Parabéns! Você acertou! O número era " + numeroSecreto);
            }
        }

        scanner.close();
    }
}