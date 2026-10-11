Problem

You are building a logging system that stores recent message characters in a fixed-size circular buffer.

The buffer maintains two independent pointers:

writeIndex — where the next write begins

readIndex — where the next read begins

Both pointers wrap back to the beginning after reaching the end of the buffer.

Implement the CircularMessageBuffer class:

CircularMessageBuffer(int capacity)

void write(String message)

String read(int length)
write(message) stores every character beginning at writeIndex. Existing characters may be overwritten, and the write pointer advances by the message length.

read(length) returns characters beginning at readIndex. Reading does not remove data, and the read pointer advances by the requested length.

Initially, every buffer position contains the null character "\0".

Example I

Input:
["CircularMessageBuffer", "write", "read", "write", "read"]
[[4], ["abcd"], [2], ["xy"], [4]]

Output:
[null, null, "ab", null, "cdxy"]
Example II

Input:
["CircularMessageBuffer", "read", "write", "read"]
[[5], [3], ["xy"], [4]]

Output:
[null, "\0\0\0", null, "\0\0xy"]