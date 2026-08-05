from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1

        gene_type = ['A','C','G','T']
        visited = set()
        bank = set(bank)
        process = deque()
        process.append((startGene, 0)) #current Gene, steps
        visited.add(startGene)

        while process:
            curr_gene, steps = process.popleft()
            
            for i in range(8):
                for tp in gene_type:
                    if curr_gene[i] == tp: # nothing changed
                        continue
                    
                    next_gene = curr_gene[:i] + tp + curr_gene[i+1:]
                    if next_gene not in visited and next_gene in bank:
                        if next_gene == endGene:
                            return steps + 1
                        else:
                            visited.add(next_gene)
                            process.append((next_gene, steps + 1))

        return -1