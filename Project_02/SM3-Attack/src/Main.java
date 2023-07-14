import SM3.*;

import java.util.List;

public class Main {
    public static void main(String[] args) {
        final int tarBit = 32;
        final int strLen = 16;

        RhoMethod rhoMethod = new RhoMethod(tarBit, strLen);
        BirthdayAttack birthdayAttack = new BirthdayAttack(tarBit, strLen);

        long startTime = System.currentTimeMillis();
        //List<String> res = birthdayAttack.attack();
        List<String> res = rhoMethod.attack();
        long endTime = System.currentTimeMillis();
        long elapsedTime = endTime - startTime;
        System.out.println("Target bits: " + tarBit + "bits");
        System.out.println("Length of str: " + strLen);
        System.out.println("Elapsed Time: " + elapsedTime + "ms\n");

        System.out.println("str1: " + res.get(0));
        System.out.println("HashValue: " + res.get(2) + '\n');

        System.out.println("str2: " + res.get(1));
        System.out.println("HashValue: " + res.get(3) + '\n');
    }
}
