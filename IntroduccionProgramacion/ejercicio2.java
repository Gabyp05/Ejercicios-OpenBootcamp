public class Main{
    public static void main(String[] args) {
        int numeroIf = 0;

        if (numeroIf>0){
            System.out.println("La variable numeroIf " + numeroIf + " es positivo");
        }
        else if(numeroIf<0){
            System.out.println("La variable numeroIf " + numeroIf + " es negativo");
        } else {
            System.out.println("La variable numeroIf es 0");
        }

        //Bucle while
        int numeroWhile = 1;

        while(numeroWhile < 3){
            numeroWhile++;
            System.out.println("La variable numeroWhile ahora es: " + numeroWhile);
        }

        //Bucle do while
        int numeroDoWhile = 3;
        do{
            numeroDoWhile++;
            System.out.println("La variable numeroDoWhile ahora es: " + numeroDoWhile);
        }while(numeroDoWhile < 3);

        //Bucle for
        for(int numeroFor = 0; numeroFor <= 3; numeroFor++){
            System.out.println("La variable numeroFor ahora es: " + numeroFor);
        }

        //switch
        String estacion = "invierno";
        switch(estacion) {
            case "primavera":
                System.out.println("Estamos en: Primavera");
                break;
            case "verano":
                System.out.println("Estamos en: Verano");
                break;
            case "invierno":
                System.out.println("Estamos en: Invierno");
                break;
            case "otoño":
                System.out.println("Estamos en: Otoño");
                break;
            default:
                System.out.println("Haz ingresado una opcion incorrecta");
        }
    }
}
