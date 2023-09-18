

i = 0 # index for S
j = 0 # index for S_prime
all_event_matches = [] # stores FIRST index where S_i matches S_prime_j

while i < len(S) and j < len(S_prime):
    if S[i] == S_prime[j]:
        all_event_matches.append(i) # store first occurrence index of event match
        i += 1
        j += 1
    else:
        i += 1

    if j == len(S_prime):
        return matches # return match occurrences {m_1, ..., m_k}
    else:
        return null



