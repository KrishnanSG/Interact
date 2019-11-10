## Messaging format

Each message will have this format
```
1. First byte specifying the message type - int.
    - `2` - Bloom filter request message from client to server - server should reply with type `3` followed by the bloomfilter.
    - `3` - Denotes that a bloom filter is incoming
    - `4` - Denotes that the actual changes are coming through in that request

```

Once the BF is exchanged
1. Call getMissingContent for both users
2. Send the missing contents of user 1 to user 2
3. Call merge function on user2 side
4. Send entire file hash value and check on both ends
    if equal
        done
    else
        send the entire compressed file 