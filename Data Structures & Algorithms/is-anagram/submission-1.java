class Solution {
    public boolean isAnagram(String s, String t) {
        s=s.replaceAll("//s", "");
        t=t.replaceAll("//s", "");
        if(s.length()!=t.length()){
            return false;
        }
        // char[] arr1=s.toCharArray();
        // char[] arr2=t.toCharArray();

        // Arrays.sort(arr1);
        // Arrays.sort(arr2);

        // return Arrays.equals(arr1,arr2);
        int[] charCounts=new int[256];
        for(int i=0;i<s.length();i++){
            charCounts[s.charAt(i)]++;
            charCounts[t.charAt(i)]--;
        }

        for(int count:charCounts){
            if(count!=0){
                return false;
            }
            
        }
        return true;
    }
}
