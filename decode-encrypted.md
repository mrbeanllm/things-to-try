Decode an Encrypted Paragraph Tree (Hard)

A document is stored as a tree of paragraphs. Each node holds a paragraph text — a string of lowercase English letters and spaces, possibly empty — and an ordered list of child nodes.

The document was encoded in two steps:

Substitution cipher. Given a key that is a permutation of the 26 lowercase letters, every letter of every paragraph was substituted: the letter 'a' + i was replaced by key[i]. Spaces were left unchanged.

Pre-order serialization. The tree was flattened into a single string: each node became

"(" + encodedText + serializedChild1 + serializedChild2 + ... + ")"
with children serialized in order. Because paragraph texts never contain parentheses, ( and ) unambiguously mark node boundaries.

Given key and the serialized string s, which encodes exactly one root node, decode the document and return the tree as nested lists: each node is represented as [text, [child1, child2, ...]], where text is the fully decoded paragraph and the second element is the (possibly empty) list of its children in order.

Examples
Example 1

Input:  key = "bcdefghijklmnopqrstuvwxyza"
        s   = "(ij(bc)(de))"
Output: ["hi", [["ab", []], ["cd", []]]]
Here key maps each letter to the next one ('a' -> 'b', ..., 'z' -> 'a'), so decoding maps each letter back: "ij" -> "hi", "bc" -> "ab", "de" -> "cd". The root "hi" has two leaf children.

Example 2

Input:  key = "qwertyuiopasdfghjklzxcvbnm"
        s   = "(ug gf(xh(rgvf))())"
Output: ["go on", [["up", [["down", []]]], ["", []]]]
Under this key, 'g' -> 'u', 'o' -> 'g', 'u' -> 'x', 'p' -> 'h', 'd' -> 'r', 'w' -> 'v', 'n' -> 'f'; spaces are unchanged. The root decodes to "go on" and has two children: "up" (which has one child "down") and a node with empty text.

Constraints
key has length 26 and is a permutation of the lowercase English alphabet.
1 <= s.length <= 10^5, and s is a valid serialization of exactly one root node.
The tree has at most 10^4 nodes.
Every paragraph text consists only of lowercase English letters and spaces, and may be empty.
An O(s.length) solution is expected.

Examples
Example 1
Input
("bcdefghijklmnopqrstuvwxyza", "(ij(bc)(de))")
Output
["hi", [["ab", []], ["cd", []]]]
Notes
This key shifts every letter forward by one, so decoding shifts back: ij->hi, bc->ab, de->cd. The root "hi" has two leaf children.
Example 2
Input
("qwertyuiopasdfghjklzxcvbnm", "(ug gf(xh(rgvf))())")
Output
["go on", [["up", [["down", []]]], ["", []]]]
Notes
Spaces are unchanged. Decoding: "ug gf"->"go on", "xh"->"up", "rgvf"->"down". The root has two children: "up" (with one child "down") and a node with empty text "()".
Constraints
key has length 26 and is a permutation of the lowercase English alphabet.
1 <= s.length <= 10^5, and s is a valid serialization of exactly one root node.
The tree has at most 10^4 nodes.
Every paragraph text consists only of lowercase English letters and spaces, and may be empty.
An O(s.length) solution is expected.

Signature
def solution(key: str, s: str):
Sample call
solution("bcdefghijklmnopqrstuvwxyza", "(ij(bc)(de))")

def solution(key, s):
    # key: permutation of the 26 lowercase letters (encoding map: 'a'+i -> key[i])
    # s:   serialized encoded tree, e.g. "(ij(bc)(de))"
    # Return the decoded tree as nested lists: [text, [child1, child2, ...]]
    pass