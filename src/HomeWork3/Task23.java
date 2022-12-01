package HomeWork3;

import java.util.ArrayList;
import java.util.List;

public class Task23 {
    List<Integer> list = new ArrayList<>();
    List<Integer> listResult = new ArrayList<>();
        list.add(12);
        list.add(21);
        list.add(111);
        list.add(150);
        list.add(1);
        list.add(195);
        for(
    int i;:list)

    {
        if (i % 2 == 0) {
            listResult.add(i);
        }
    }
        list.removeAll(listResult);
        System.out.println(list);
        System.out.println(listResult);
}
