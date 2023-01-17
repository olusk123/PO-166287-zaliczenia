public class Main {
    public static void main(String[] args){
        Publikacja nowa = new Publikacja("Rewelacyjna Publikacja",100.0);
        System.out.println(nowa);

        System.out.println(Publikacja.getIle());
        Publikacja stara = new Publikacja("Stara Publikacja",20, 1970,12, 12);
        System.out.println(stara);

        System.out.println(Publikacja.getIle());
        System.out.println(stara.equals(nowa));

        Czasopismo superowe = new Czasopismo("Kocham UWM", 420.80, 2023, 12,12, 4);
        System.out.println(superowe);

        Czasopismo znakomite = new Czasopismo("Olsztyn Top", 60.0, 2022, 1, 6, 80);
        System.out.println(znakomite);

        System.out.println(znakomite.equals(superowe));
        Czasopismo identyczne = new Czasopismo("Olsztyn Top", 60.0, 2022, 1, 6, 80);
        System.out.println(znakomite.equals(identyczne));
        nowa.zwiekszCene(20);
        System.out.println(nowa);


    }
}