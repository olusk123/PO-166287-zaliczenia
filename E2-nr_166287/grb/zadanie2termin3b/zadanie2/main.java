package zadanie2;

import java.util.ArrayList;
import java.util.Objects;

public class main {

    public static <E extends Comparable<E>> E max(ArrayList<E> array){
        E wynik = null;
        for(E in:array){
            if(wynik == null||in.compareTo(wynik)>0){
                wynik = Objects.requireNonNull(in);
            }
        }
        return wynik;
    }
    public static <E extends Comparable<E>> E min(ArrayList<E> array){
        E wynik = null;
        for(E in:array){
            if(wynik == null||in.compareTo(wynik)<0){
                wynik = Objects.requireNonNull(in);
            }
        }
        return wynik;
    }
    public static void main(String[] args) {
        ArrayList<Integer> init = new ArrayList<>();
        init.add(2);
        init.add(3);
        init.add(1);
        init.add(5);
        init.add(4);
        System.out.println(max(init));
        System.out.println(min(init));

        ArrayList<String> stringowa = new ArrayList<>();
        stringowa.add("nazwa1");
        stringowa.add("nazwa2");
        stringowa.add("nazwa4");
        stringowa.add("nazwa5");
        stringowa.add("nazwa3");
        System.out.println(max(stringowa));
        System.out.println(min(stringowa));

        ArrayList<Double> przec = new ArrayList<>();
        przec.add(3.1);
        przec.add(3.3);
        przec.add(1.2);
        przec.add(1.1);
        przec.add(2.9);
        System.out.println(max(przec));
        System.out.println(min(przec));
    }
}
