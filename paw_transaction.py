import hashlib
import time
from typing import Optional, cast
from ecdsa import SigningKey, VerifyingKey, SECP256k1, BadSignatureError


class PawTransaction:
    """
    Represents a single share of Catnip on the PawChain.

    This class is the equivalent of a standard blockchain transaction.
    """

    def __init__(
        self, from_cat_tag: Optional[str], to_cat_tag: str, catnip_amount: float
    ) -> None:
        """
        Initializes a new share of Catnip.

        Args:
            from_cat_tag: The sender's public Cat Tag (wallet address).
            to_cat_tag: The receiver's public Cat Tag (wallet address).
            catnip_amount: The amount of Catnip (currency) being shared.
        """
        self.from_cat_tag: Optional[str] = from_cat_tag
        self.to_cat_tag: str = to_cat_tag
        self.catnip_amount: float = catnip_amount
        self.share_time: int = int(time.time() * 1000)
        self.paw_print: Optional[str] = None  # This will hold the signature

    def __repr__(self) -> str:
        """Provides a developer-friendly string representation of the transaction."""
        return (
            f"PawTransaction(from: {self.from_cat_tag}, to: {self.to_cat_tag}, "
            f"amount: {self.catnip_amount} Catnip)"
        )

    def calculate_treat_hash(self) -> str:
        """
        Calculates the unique hash for this treat share.

        This method performs the core hashing function for a transaction.
        """
        tx_contents = (
            f"{self.from_cat_tag}{self.to_cat_tag}{self.catnip_amount}{self.share_time}"
        )
        return hashlib.sha256(tx_contents.encode("utf-8")).hexdigest()

    def leave_paw_print(self, signing_key: SigningKey) -> None:
        """
        Signs the transaction with a Secret Purr to create a unique Paw Print.

        This method is the equivalent of signing a transaction with a private key.
        The resulting 'paw_print' is the digital signature.

        Args:
            signing_key: The Secret Purr (private key) of the sender.
        """
        public_cat_tag = (
            cast(VerifyingKey, signing_key.get_verifying_key()).to_string().hex()
        )
        if public_cat_tag != self.from_cat_tag:
            raise Exception("You can only leave paw prints for your own Cat Tag!")

        treat_hash = self.calculate_treat_hash()
        signature = signing_key.sign(treat_hash.encode("utf-8"))
        self.paw_print = signature.hex()

    def is_paw_print_valid(self) -> bool:
        """
        Checks if the Paw Print is valid and the treat hasn't been nibbled on.

        This method verifies the digital signature of the transaction. It ensures
        that the transaction was authorized by the sender and has not been altered.
        """
        if self.from_cat_tag is None:  # For reward treats
            return True

        if self.paw_print is None:
            raise Exception("No paw print on this treat share!")

        try:
            public_key_bytes = bytes.fromhex(self.from_cat_tag)
            public_key = VerifyingKey.from_string(public_key_bytes, curve=SECP256k1)
            treat_hash = self.calculate_treat_hash()
            return public_key.verify(
                bytes.fromhex(self.paw_print), treat_hash.encode("utf-8")
            )
        except (BadSignatureError, Exception):
            return False
