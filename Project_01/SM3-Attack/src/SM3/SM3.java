package SM3;

import org.bouncycastle.crypto.digests.SM3Digest;
import org.bouncycastle.util.encoders.Hex;

public class SM3 {
    public String hash(String data) {
        byte[] dataBytes = data.getBytes();

        SM3Digest sm3Digest = new SM3Digest();
        sm3Digest.update(dataBytes, 0, dataBytes.length);

        byte[] hashBytes = new byte[sm3Digest.getDigestSize()];
        sm3Digest.doFinal(hashBytes, 0);

        return Hex.toHexString(hashBytes);
    }
}
