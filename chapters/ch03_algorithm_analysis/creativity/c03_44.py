"""
C-3.44 | Chapter 3: Algorithm Analysis
Type: Creativity
Page: book p.145 (PDF p.167)    ->  python tools/show.py C-3.44
Status: todo            # todo | in-progress | done | skipped
Date:
Time:

Problem:
    Communication security is extremely important in computer networks, and one way many
    network protocols achieve security is to encrypt mes- sages. Typical cryptographic
    schemes for the secure transmission of mes- sages over such networks are based on
    the fact that no efﬁcient algorithms are known for factoring large integers. Hence,
    if we can represent a secret message by a large prime number p, we can transmit,
    over the network, the number r = p · q,w h e r eq > p is another large prime number
    that acts as the encryption key. An eavesdropper who obtains the transmitted num-
    ber r on the network would have to factorr in order to ﬁgure out the secret message
    p. Using factoring to ﬁgure out a message is very difﬁcult without knowing the
    encryption key q. To understand why, consider the following naive factoring
    algorithm: for p in range(2,r): if r%p= =0 : # if p divides r return The secret
    message is p! a. Suppose that the eavesdropper uses the above algorithm and has a
    computer that can carry out in 1 microsecond (1 millionth of a sec- ond) a division
    between two integers of up to 100 bits each. Give an estimate of the time that it
    will take in the worst case to decipher the secret message p if the transmitted
    message r has 100 bits. b. What is the worst- case time complexity of the above
    algorithm? Since the input to the algorithm is just one large number r, assume that
    the input size n is the number of bytes needed to store r,t h a ti s , n = ⌊(log2
    r)/8⌋ + 1, and that each division takes time O(n).

Approach:
    (idea, then time/space complexity)

Notes:
    (gotchas, what you learned)
"""


# your solution here


if __name__ == "__main__":
    pass
