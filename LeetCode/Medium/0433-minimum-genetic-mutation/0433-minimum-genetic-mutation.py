from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        gene_type = ['A','C','G','T']
        visited = set()
        process = deque()
        process.append((startGene, 0)) #current Gene, steps

        while process:
            curr_gene, steps = process.popleft()
            visited.add(curr_gene)

            for i in range(8):
                for tp in gene_type:
                    if curr_gene[i] == tp: # nothing changed
                        continue
                    
                    next_gene = curr_gene[:i] + tp + curr_gene[i+1:]
                    if next_gene not in visited and next_gene in bank:
                        if next_gene == endGene:
                            return steps + 1
                        else:
                            process.append((next_gene, steps + 1))

        return -1