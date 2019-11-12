# Interact

An easy to use real time file synchronization application built using Python.
<img src="https://user-images.githubusercontent.com/43802499/68604424-71f7df00-04d0-11ea-9773-1d51344c8318.png" align="right"
     title="Interact" width="35%" height="20%">

## Getting Started

These instructions will get you a copy of the project and ready for use on your local machine.

### Prerequisites

  #### Quick Access
  - Click on the link to download the tool - [Interact.zip](https://github.com/KrishnanSG/Interact/files/3835348/Interact.zip)
  
  - Extract the zip folder
  
  #### Developer Style
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

#### Quick Access
> Use the following commands if you have downloaded the tool using steps described in quick access.

1. Open your favourite terminal

2. Creating host server
     ```
          ./Interact.exe <filename> --host
     ```
3. Ask your friend to connect to the server
    ```
        ./Interact <filename>

        Provide inputs for the prompt messages.
    ```

#### Developer Stlye

1. Creating host server
    ```
        python main.py <filename> --host
    ```

2. Ask your friend to connect to the server
    ```
        python main.py <filename>

        Provide inputs for the prompt messages.
    ```

3. Enjoy Interact :) . We automatically detect for modification made in the file, so just save the file.

> You may use the following command to get help regarding the tool
```
     ./Interact.exe --help or python main.py --help
```

## How does this work?

Most of the file synchronziers send the complete file across the network for every sync cycle, this causes unnecessary data transfer.

Let's consider this case where you make a modification on line 10 but your file containing 1000 lines is sent across the network.

" To solve this problem **Interact** was developed. "

### How we do it?

**BloomFilter**

A Bloom filter is a space-efficient probabilistic data structure that is used to test whether an element is a member of a set. Check out this [link](https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/) to know more.

### The protocol

We will be using a few terms in the due course of the explanation.
- **Host** - the user who has intiated the P2P server.
- **Client** - the user who connects to the host.
- **User1** - the user who initates the sync cycle (would have made some modification to the file).
- **User2** - the user whose file will get updated.
- **getMissingContent()** - a function to find the missing contents.
- **syncFile()** - a function to merge (reproduce the changes on the destination).

![Sync-Protocol](https://user-images.githubusercontent.com/43802499/68604316-31986100-04d0-11ea-9f65-fce7b3cd8357.png)

### Conclusion
The algorithm developed does synchronization effieciently since the size of the BloomFiter transmitted is in **bits** while the file would be in **MBs**.

The total average transmition cost was found out to be size_of_BloomFilter (Few btyes) + number of lines modified (a few 100 bytes).

## Authors

* **Krishnan S G** - [@KrishnanSG](https://github.com/KrishnanSG)
* **Sivagiri Visakan** - [@SivagiriVisakan](https://github.com/SivagiriVisakan)
