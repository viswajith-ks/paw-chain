# PawChain 🐾

A simple, cat-themed blockchain built in Python for educational purr-poses.

This project is a fun, hands-on introduction to the core concepts of blockchain technology. Instead of dealing with boring, technical jargon, explore the world of `PawBlocks`, `PawTransactions`, and hunting for `Catnip`\!

![hi](https://i.imgur.com/4dSv0jH.gif)

-----

## 📖 About the Project

The goal of PawChain is to demystify blockchain by building a simple, functional model from scratch. It covers the essential components that make a blockchain work, including:

  * **Cryptographic Hashing:** Creating a unique and tamper-proof "scratch mark" for every block.
  * **Immutable Chain:** Linking blocks together using their hashes, creating "the long yarn."
  * **Proof-of-Work:** The process of "hunting" for blocks by solving a computational puzzle.
  * **Digital Signatures:** Using a "Secret Purr" (private key) to leave a unique "Paw Print" (signature) on every transaction.
  * **Decentralized Ledger:** While this project runs locally, it demonstrates how transactions are grouped into blocks and added to a shared chain.

-----

## 🐈 The Cat Terminology

To make learning more fun, I've replaced standard blockchain terms with cat-themed equivalents. Here's a quick translation guide:

| Cat Theme          | Blockchain Term             | Description                                          |
| :----------------- | :-------------------------- | :--------------------------------------------------- |
| **PawChain** | Blockchain                  | The entire chain of blocks, linked together.         |
| **PawBlock** | Block                       | A single container for transactions in the chain.    |
| **PawTransaction** | Transaction                 | An act of sending currency from one user to another. |
| **Catnip** | Currency                    | The digital asset or "coin" of the PawChain.         |
| **Hunt for a Block** | Mining                      | The process of finding a valid hash for a new block.   |
| **Scratch Mark** | Hash                        | The unique, cryptographic fingerprint of a block.    |
| **Cat Tag** | Public Key / Wallet Address | A publicly shareable address used to receive Catnip. |
| **Secret Purr** | Private Key                 | A secret key used to authorize sending Catnip.       |
| **Paw Print** | Digital Signature           | A cryptographic proof that a transaction is authentic. |

-----

## 🚀 Getting Started

Follow these steps to get your own instance of the PawChain running.

### Installation

1.  **Clone the repository (or download the files):**
    ```sh
    git clone https://github.com/your-username/paw-chain.git
    cd paw-chain
    ```
2.  **Create a virtual environment (recommended):**
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```
3.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

### Running the Simulation

1.  **Generate Your Cat Identity:**
    Run the key generator to create your own unique `Cat Tag` and `Secret Purr`.

    ```sh
    python key_generator.py
    ```

    You can copy the `Secret Purr` and paste it into `main.py` to use your new identity.

2.  **Run the PawChain:**
    Execute the main script to start the simulation. It will create the chain, mine blocks, and process transactions.

    ```sh
    python main.py
    ```

-----

## 📂 File Structure

  * `paw_transaction.py`: Defines a single share of Catnip (a transaction).
  * `paw_block.py`: Defines a `PawBlock` that holds a list of transactions.
  * `paw_chain.py`: Manages the entire chain, including mining and validation.
  * `main.py`: The main script that simulates creating and using the PawChain.
  * `key_generator.py`: A utility script to generate new key pairs.

-----

## 🚨 Disclaimer: For Educational Use Only\!

This project was built for learning and fun. It is a **highly simplified model** of a real blockchain and has many security flaws and missing features.

  * **No robust consensus algorithm:** It doesn't handle conflicts between different versions of the chain.
  * **Basic security:** It is vulnerable to many attacks that real cryptocurrencies are designed to prevent.
