import hashlib
import json
from typing import List
from paw_transaction import PawTransaction


class PawBlock:
    """
    Represents a single block in the PawChain.

    A block is a collection of shared treats (transactions) that has been
    successfully hunted (mined).
    """

    def __init__(
        self,
        pounce_time: int,
        shared_treats: List[PawTransaction],
        previous_scratch_mark: str = "",
    ) -> None:
        """
        Initializes a new PawBlock.

        Args:
            pounce_time: The time the block was created (timestamp).
            shared_treats: A list of PawTransactions included in the block.
            previous_scratch_mark: The hash of the previous block.
        """
        self.previous_scratch_mark: str = previous_scratch_mark
        self.pounce_time: int = pounce_time
        self.shared_treats: List[PawTransaction] = shared_treats
        self.purr_count: int = 0  # This is the nonce
        self.scratch_mark: str = self.calculate_scratch_mark()  # This is the hash

    def calculate_scratch_mark(self) -> str:
        """
        Calculates the unique scratch mark (hash) for this block of treats.
        """
        treat_data = json.dumps(
            [tx.__dict__ for tx in self.shared_treats], sort_keys=True
        )
        pawblock_contents = f"{self.previous_scratch_mark}{self.pounce_time}{treat_data}{self.purr_count}"
        return hashlib.sha256(pawblock_contents.encode("utf-8")).hexdigest()

    def hunt_for_block(self, hunt_difficulty: int) -> None:
        """
        Starts the hunt (mining) to find a valid scratch mark for the block.

        This is the Proof-of-Work algorithm. It iterates through the purr_count
        (nonce) until it finds a scratch_mark (hash) that meets the required
        hunt_difficulty (difficulty).

        Args:
            hunt_difficulty: The number of leading zeros for the hash.
        """
        mouse_to_catch = "0" * hunt_difficulty
        while not self.scratch_mark.startswith(mouse_to_catch):
            self.purr_count += 1
            self.scratch_mark = self.calculate_scratch_mark()
        print(f"Block caught! 🐾: {self.scratch_mark}")

    def has_good_treats(self) -> bool:
        """
        Checks if all shared treats in the block have valid paw prints.

        This method validates all transactions within the block.
        """
        for treat in self.shared_treats:
            if not treat.is_paw_print_valid():
                return False
        return True
