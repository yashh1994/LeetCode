class Solution {
    public boolean isCircularSentence(String sentence) {
        String[] words = sentence.split(" ");
        for (int i = 1; i < words.length; i++) {
            String word1 = words[i];
            String word2 = words[i - 1];
            if (word1.charAt(0) != word2.charAt(word2.length() - 1)) {
                return false;
            }
        }
        String lastWord = words[words.length - 1];
        String firstWord = words[0];
        if (lastWord.charAt(lastWord.length() - 1) != firstWord.charAt(0)) {
            return false;
        }
        
        return true;
    }
}
