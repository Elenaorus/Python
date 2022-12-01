package HomeWork2;

import javax.swing.tree.TreeNode;
import java.util.ArrayList;
import java.util.List;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
public class Task3 {
    public List<String> binaryTreePaths(TreeNode root) {


        List<String> res = new ArrayList<>();
        if (root == null) return res;


        helper(root, "", res);
        return res;
    }

    public void helper(TreeNode root, String s, List<String> res) {
        if (root.left == null && root.right == null) res.add(s + root.val);
        if (root.left != null) helper(root.left, s + root.val + "->", res);
        if (root.right != null) helper(root.right, s + root.val + "->", res);
    }
}
