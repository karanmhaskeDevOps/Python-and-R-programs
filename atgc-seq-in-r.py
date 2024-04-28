dna_sequence <- "ATCGATCGATCGTACG"
dna_sequence <- toupper(dna_sequence)
total_bases <- nchar(dna_sequence)

bases <- c("A", "T", "G", "C")
pairs <- c("AT", "GC")

for (base in bases) {
  count <- sum(dna_sequence == base)
  cat(base, ": ", count, "(", count/total_bases*100, "%)\n")
}

for (pair in pairs) {
  count <- sum(grepl(pair, dna_sequence))
  cat(pair, " pairs: ", count, "(", count/(total_bases-1)*100, "%)\n")
}
