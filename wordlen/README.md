### Word Length

Count the length of unique words (e.g., there were five unique words of length four, etc.).  

(N.B. This is a two-stage MR.  First, do wordcount to get a list of the unique words.  The second map has key-value the length of the words and 1, respectively.  Then add the values; this is the same reduce as the first MR stage.)
