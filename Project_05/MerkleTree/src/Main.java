import merkle.*;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class Main {
    public static void main(String[] args) {
        SHA256 sha256 = new SHA256();

        List<String> dataList = new ArrayList<String>();
        dataList = Arrays.asList("a", "b", "c", "d");

        MerkleTree merkleTree = new MerkleTree(dataList);
        merkleTree.preorder();
        System.out.println();

        merkleTree.insert("e");
        merkleTree.preorder();
        System.out.println();

        merkleTree.insert("f");
        merkleTree.preorder();
        System.out.println();


    }
}