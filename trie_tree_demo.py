# This code enable you to recognise a dictionary of pre-defined entities from text, 
# using a trie tree in a efficient way.

def read_drug_name():
    f = open('./drugNames.txt', 'r+', encoding='UTF-8')
    names = []
    for line in f:
        line = line.strip()
        if len(line) > 1:
            names.append(line)
    return names

class Node(object):
    def __init__(self):
        self.child = {}
        self.is_word = False

class Trie():
    def __init__(self, names):
        self.root = Node()
        self.build_trie(names)

    def build_trie(self, names):
        for name in names:
            curr = self.root
            for char in name:
                if char not in curr.child:
                    curr.child[char] = Node()
                curr = curr.child[char]
            curr.is_word = True

    def search_durgs(self, text1):
        res = []
        for i in range(len(text1)):
            curr = self.root
            inc = 0 # increase
            while i+inc<len(text1) and text1[i+inc] in curr.child:
                curr = curr.child[text1[i+inc]]
                if curr.is_word:
                    res.append(text1[i:i+inc+1])
                inc += 1
        return res
        

def build_trie_tree(drug_names):
    return Trie(drug_names)

# This code enable you to recognise a dictionary of pre-defined entities from text, 
# using a trie tree in a efficient way.
def main():
    drug_names = ['ibuprofen','acetaminophen','Advil', 'Motrin']
    script = 'This is demo script from a doctor:\
     Take 1 tablet Advil by mouth every six hours;\
     Take 1 tablet ibuprofen by mouth every six hours'
    trie = build_trie_tree(drug_names)
    recognised_entities = trie.search_durgs(script)
    print(recognised_entities)

if __name__ == '__main__':
    main()
