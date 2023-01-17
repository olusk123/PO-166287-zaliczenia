import java.nio.channels.Pipe;
import java.time.LocalDate;
import java.util.Objects;

public class Publikacja {
    private String tytul;
    private  double cena;
    private LocalDate dataWydania;
    private static int ile=0;

    public Publikacja(String tytul, double cena, int rok, int miesiac, int dzien) {
        this.tytul = tytul;
        this.cena = cena;
        this.dataWydania = LocalDate.of(rok, miesiac, dzien);
        ile++;
    }
    public Publikacja(String tytul, double cena) {
        this.tytul = tytul;
        this.cena = cena;
        this.dataWydania = LocalDate.now();
    }


    public String getTytul() {
        return tytul;
    }

    public double getCena() {
        return cena;
    }

    public void setDataWydania(int rok,int miesiac,int dzien) {
        this.dataWydania = LocalDate.of(rok, miesiac, dzien);
    }

    @Override
    public String toString() {
        if(Objects.equals(this.tytul, "Publikacja Nieznana")){
            return this.getClass().getName() + "[" + this.dataWydania + "], "
                    + "[" +this.cena + "], ";
        }
        return this.getClass().getName() + "[" + this.tytul + "], "
                + "[" + this.dataWydania + "], "
                + "[" +this.cena + "]";

    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Publikacja that = (Publikacja) o;
        return Double.compare(that.cena, cena) == 0 && Objects.equals(tytul, that.tytul) && Objects.equals(dataWydania, that.dataWydania);
    }

    @Override
    public int hashCode() {
        return Objects.hash(tytul, cena, dataWydania);
    }
    public double zwiekszCene(double procent){
        double w = this.cena *= procent*100;
        return w;
    }
    public static int getIle() {
        return ile;
    }

}

