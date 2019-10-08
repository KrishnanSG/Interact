## Messaging format

Each message will have this format
```
1. First byte specifying the message type - int.
    - `2` - Bloom filter request message from client to server - server should reply with type `3` followed by the bloomfilter.
    - `3` - Denotes that a bloom filter is incoming
    - `4` - Denotes that the actual changes are coming through in that request

```

Maybe pad all the messages with some delimiter bytes to seperate the different requests
