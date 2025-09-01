from ecdsa import SigningKey, VerifyingKey, SECP256k1
from paw_chain import PawChain
from typing import cast
from paw_transaction import PawTransaction


def main() -> None:
    # A friend's Cat Tag to send Catnip to
    friend_cat_tag: str = (
        "9dc4c1268d18bb8a5a5390bdb1d9740a87a8caf102814c96fd4bbaa1afcc91afe569f147a3e4c6e26988f31f5beb0276afa51255e300fa8645e862b5d2e593fe"
    )
    # Your Secret Purr (private key) in hex
    secret_purr_hex: str = (
        "300302f4475106380db618acebe71ae171a1619f218a2e1072925be2b309b290"
    )
    my_secret_purr: SigningKey = SigningKey.from_string(
        bytes.fromhex(secret_purr_hex), curve=SECP256k1
    )

    # Your public Cat Tag (wallet address) derived from your Secret Purr
    my_cat_tag: str = (
        cast(VerifyingKey, my_secret_purr.get_verifying_key()).to_string().hex()
    )

    # Create our PawChain instance
    paw_chain = PawChain()
    print("The PawChain has been unleashed! 🐈")

    # The first hunter gets the reward for the first block
    print("\nStarting the first hunt for Catnip...")
    paw_chain.hunt_for_treats(my_cat_tag)

    # Create a transaction to share Catnip
    print("\nSharing 100 Catnip with a friend...")
    share1 = PawTransaction(my_cat_tag, friend_cat_tag, 100.0)
    share1.leave_paw_print(my_secret_purr)
    paw_chain.add_treat_to_bowl(share1)

    # Hunt for a new block to confirm the share
    print("\nHunting for a new block...")
    paw_chain.hunt_for_treats(my_cat_tag)

    # Create a second transaction
    print("\nSharing 50 more Catnip...")
    share2 = PawTransaction(my_cat_tag, friend_cat_tag, 50.0)
    share2.leave_paw_print(my_secret_purr)
    paw_chain.add_treat_to_bowl(share2)

    # Hunt again
    print("\nHunting for another block...")
    paw_chain.hunt_for_treats(my_cat_tag)

    # Check the final balances
    print(
        f"\nFinal Catnip stash for our Head Cat: {paw_chain.get_catnip_balance(my_cat_tag)}"
    )
    print(
        f"Final Catnip stash for friend cat: {paw_chain.get_catnip_balance(friend_cat_tag)}"
    )

    print()
    print(
        "Is the yarn unbroken (chain valid)?",
        "Yes, purrfect!" if paw_chain.is_yarn_unbroken() else "No, hisss!",
    )


if __name__ == "__main__":
    main()
