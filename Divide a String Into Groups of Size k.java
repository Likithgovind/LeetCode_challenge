import java.util.*;
class Solution
{
    public String[] divideString(String s, int k, char fill)
    {
        while (s.length()%k!=0)
        {
            s+=fill;
        }
        List<String> l=new ArrayList<>();
        for(int i=0;i<s.length();i+=k)
        {
            l.add(s.substring(i,i+k));
        }
        return l.toArray(new String[0]);
    }
}
