public class Demo<T> {
    public static <T> Demo <T> print(T[] arr){
        StringBuilder sb = new StringBuilder();
        for (T ssb: arr) {
            sb.append(ssb).append(",");
        }
        System.out.println(sb);
        return null;
    }
}
