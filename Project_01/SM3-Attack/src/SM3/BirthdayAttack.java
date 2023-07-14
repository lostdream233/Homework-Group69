package SM3;

import java.util.ArrayList;
import java.util.Random;
import java.util.List;

public class BirthdayAttack {
    public BirthdayAttack(int tarBit, int strLen) {
        this.tarBit = tarBit;
        this.strLen = strLen;
        preStr = new ArrayList<>();
        preHash = new ArrayList<>();
        preSubHash = new ArrayList<>();
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

    public List<String> attack() {
        SM3 sm3 = new SM3();
        String str, hash, subHash;
        boolean flag = false;

        List<String> res = new ArrayList<>();
        int count = 0;
        do {
            str = randomString(strLen);
            hash = sm3.hash(str);

            subHash = hash.substring(0, tarBit / 4);

            if (preSubHash.contains(subHash)) {
                flag = true;
                int index = preSubHash.indexOf(subHash);
                res.add(preStr.get(index));
                res.add(str);
                res.add(preHash.get(index));
                res.add(hash);
            } else {
                preStr.add(str);
                preHash.add(hash);
                preSubHash.add(subHash);
            }
            count++;
        } while (!flag);

        System.out.println("Total times: " + count);

        return res;
    }

    private final List<String> preStr, preHash, preSubHash;
    private final int tarBit;
    private final int strLen;
}
