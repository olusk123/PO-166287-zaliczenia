package zadanie1termin3b;

import java.util.Comparator;

public class SortCompare implements Comparator<Doktorant> {
    @Override
    public int compare(Doktorant o1, Doktorant o2) {
        return o2.getName().compareTo(o1.getName());
    }
}
