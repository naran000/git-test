import java.time.LocalDate;
import java.time.LocalTime;
import java.time.Instant;

public class TimeDemo {
    public static void main(String[] args) {
        // 仅获取日期
        LocalDate date = LocalDate.now();
        System.out.println("今天日期: " + date);

        // 仅获取时间
        LocalTime time = LocalTime.now();
        System.out.println("当前时刻: " + time);

        // 获取当前时间戳 (毫秒)
        long currentTimeMillis = System.currentTimeMillis();
        System.out.println("当前毫秒数: " + currentTimeMillis);
        
        // 获取带纳秒的瞬时时间
        Instant instant = Instant.now();
        System.out.println("标准瞬时时间: " + instant);
    }
}
