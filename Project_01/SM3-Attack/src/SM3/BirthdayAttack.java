package SM3;

import java.util.ArrayList;
import java.util.Random;
import java.util.List;

public class BirthdayAttack {
    public BirthdayAttack(int tarBit, int strLen) {
        this.tarBit = tarBit;
        this.strLen = strLen;
    }

    public String randomString(int length) {
        String characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        Random random = new Random();
        StringBuilder sb = new StringBuilder(length);

        for (int i = 0; i < length; i++) {
            int randomIndex = random.nextInt(characters.length());
            char randomChar = characters.charAt(randomIndex);
            sb.append(randomChar);
        }

        return sb.toString();
    }

    public boolean check(String str1, String str2) {
        String substr1 = str1.substring(0, tarBit / 4);
        String substr2 = str2.substring(0, tarBit / 4);

        return substr1.equalsIgnoreCase(substr2);
    }

    public List<String> attack() {
        SM3 sm3 = new SM3();
        String str1, str2, hash1, hash2;
        boolean flag = false;
        do {
            str1 = randomString(strLen);
            str2 = randomString(strLen);

            hash1 = sm3.hash(str1);
            hash2 = sm3.hash(str2);

            flag = check(hash1, hash2);
        } while (!flag);

        List<String> res = new ArrayList<>();
        res.add(str1);
        res.add(str2);
        res.add(hash1);
        res.add(hash2);

        return res;
    }

    private final int tarBit;
    private final int strLen;
}
