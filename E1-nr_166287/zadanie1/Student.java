package zadanie1;

import java.util.*;

public class Student extends Person implements Clonable,Comparable<Student>{
    private final int id;
    private Date dateOfStart = null;

    public Student(String name, int id) {
        super(name);
        this.id = id;
        this.dateOfStart = new java.util.Date();
    }

    public Date getDateOfStart() {
        return dateOfStart;
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
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Student student = (Student) o;
        return id == student.id && Objects.equals(dateOfStart, student.dateOfStart);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, dateOfStart);
    }

    @Override
    protected Object clone() throws CloneNotSupportedException {
        return super.clone();
    }

    @Override
    public int compareTo(@org.jetbrains.annotations.NotNull zadanie1.Student o) {
        int res =
    }
}
