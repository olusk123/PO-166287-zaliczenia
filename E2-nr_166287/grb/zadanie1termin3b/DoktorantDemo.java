package zadanie1termin3b;

import java.util.ArrayList;

public class DoktorantDemo {
    public static void main(String[] args){

        Student s = new Doktorant("nowy1",1);
        System.out.println(s.getName());
        Doktorant d = (Doktorant) s;
        System.out.println(d.getName());
        ArrayList<Doktorant> doktoraty = new ArrayList<>();
        doktoraty.add(new Doktorant("doktoratA",1));
        doktoraty.add(new Doktorant("doktoratB",2));
        doktoraty.add(new Doktorant("doktoratD",4));
        doktoraty.add(new Doktorant("doktoratE",5));
        doktoraty.add(new Doktorant("doktoratC",6));

        System.out.println();

        doktoraty.sort(new SortCompare());
        for(Doktorant des: doktoraty){
            System.out.println(des.getName());
        }
        System.out.println();

        Doktorant d1 = new Doktorant("nowyKrotki",1);
        Doktorant d2 = new Doktorant("nowyDlozszy",2);
        System.out.println(d1.compareTo(d2));





    }
}
