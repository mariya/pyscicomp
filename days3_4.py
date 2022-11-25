import pyrust

dna = "GCCCC"
gc = 1
assert pyrust.gc_content(dna) == gc
print("Confirmed: {} should has a gc content of {}".format(dna, gc))

dna = "TTTTAA"
gc = 0
assert pyrust.gc_content(dna) == gc
print("Confirmed: {} should has a gc content of {}".format(dna, gc))

dna = "TTTTTTCGCG"
gc = 0.4
assert pyrust.gc_content(dna) == gc
print("Confirmed: {} should has a gc content of {}".format(dna, gc))
