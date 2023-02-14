package zadanie1termin3b;

import java.util.Comparator;
import java.util.Date;

public class Doktorant extends Student implements Named,Cloneable,Comparable<Doktorant>{
    private final int id;
    private Date dateOfStart = null;

    public Doktorant(String name, int id) {
        super(name);
        this.id = id;
        this.dateOfStart = new Date();
    }

    public int getId() {
        return id;
    }

    public String toString() {
        return "ID = " + id
                + ", dateOfStart = " + dateOfStart
                + "]";
    }

    @Override
    protected Object clone() throws CloneNotSupportedException {
        Doktorant cloned = (Doktorant) super.clone();
        cloned.dateOfStart = (Date) dateOfStart;
        return cloned;
    }


    @Override
    public int compareTo(Doktorant o) {
        return Integer.compare(o.getName().length(), this.getName().length());
    }
}
