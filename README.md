# Interact

An easy to use real time file synchronization application built using Python.

## Getting Started

These instructions will get you a copy of the project and ready for on your local machine.

### Prerequisites
  - Python 3.7

  - Clone this repository using the command:

    ```
      git clone https://github.com/KrishnanSG/Interact.git
      cd Interact
    ```
    
  - Then install a few required dependencies by using your favorite terminal

    ```
      pip install -r requirements.txt
    ```

### How to Use

You're almost there. 
The following steps will guide you on how to use this tool.

1. Creating host server
    ```
        python main.py <filename> --host
    ```

2. Ask your friend to connect to the server
    ```
        python main.py <filename>

        Provide inputs for the prompt messages.
    ```

3. Enjoy the sync. We automatically detect for modification made in the file, so just save the file.

## How does this work?

Most the of the file synchronziers send the complete file across the network for every sync cycle.

### How we do it?
**BloomFilters**

A Bloom filter is a space-efficient probabilistic data structure that is used to test whether an element is a member of a set. Check out this [link](https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/) to know more.

### The protocol
We will be using a few terms in the due course of the explanation.
- **Host** - the user who has intiated the P2P server.
- **Client** - the user who connects to the host.
- **User1** - the user who initates the sync cycle (would have made some modification to the file).
- **User2** - the user whose file will get updated.
- **getMissingContent()** - a function to find the missing contents.
- **syncFile()** - a function to merge (reproduce the changes on the destination).

#### The Sync Cycle
1. A file modification is detected and the sync cycle is initiated.
2. User1 generates the BloomFilter based on the file contents and sends it to User2.
3. On receiving the BloomFilter User2 genrates the BloomFilter based on the file contents and sends it to User1.
4. Call getMissingContent for both users.
5. The missing contents of User1 to User2 is sent.
3. Call merge function on User2's computer.
4. User2 compute hash for the file and sends it to User1.
5. If the hash values match then end of cycle 
   else one more sync cycle is performed or compressed copy of the file is sent, this is decided based on the number of changes and file size.

### Conclusion
The algorithm developed does synchronization effieciently since the size of the BloomFiter transmitted is in **bits** while the file would be in **MBs**.

The total average transmition cost was found out to be size_of_BloomFilter (Few btyes) + number of lines modified (a few 100 bytes).

## Authors

* **Krishnan S G** - [@KrishnanSG](https://github.com/KrishnanSG)
* **Sivagiri Visakan** - [@SivagiriVisakan](https://github.com/SivagiriVisakan)
