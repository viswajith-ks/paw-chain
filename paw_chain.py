import time
from typing import List
from paw_block import PawBlock
from paw_transaction import PawTransaction


class PawChain:
    """
    Represents the entire PawChain.

    This class manages the chain of blocks, the bowl of pending treats,
    and the rules for hunting (mining).
    """

    def __init__(self) -> None:
        """Initializes the PawChain with the First Meow (Genesis Block)."""
        self.the_long_yarn: List[PawBlock] = [self.create_first_meow()]
        self.hunt_difficulty: int = 2
        self.treats_in_bowl: List[PawTransaction] = []
        self.catnip_reward: float = 100.0

    def create_first_meow(self) -> PawBlock:
        """
        Creates the First Meow, the very first block of the PawChain.

        This is the equivalent of the Genesis Block.
        """
        return PawBlock(
            pounce_time=int(
                time.mktime(time.strptime("2025-09-01", "%Y-%m-%d")) * 1000
            ),
            shared_treats=[],
            previous_scratch_mark="",
        )

    def get_latest_catch(self) -> PawBlock:
        """
        Returns the most recently caught block at the end of the yarn.

        This is equivalent to getting the latest block in the chain.
        """
        return self.the_long_yarn[-1]

    def hunt_for_treats(self, hunter_cat_tag: str) -> None:
        """
        Gathers treats from the bowl and starts the hunt for the next block.

        This method is the core mining process. It creates a new block with
        all pending transactions and rewards the hunter (miner).

        Args:
            hunter_cat_tag: The Cat Tag (wallet address) of the miner.
        """
        reward_treat = PawTransaction(None, hunter_cat_tag, self.catnip_reward)
        self.treats_in_bowl.append(reward_treat)

        new_catch = PawBlock(
            pounce_time=int(time.time() * 1000),
            shared_treats=self.treats_in_bowl.copy(),
            previous_scratch_mark=self.get_latest_catch().scratch_mark,
        )
        new_catch.hunt_for_block(self.hunt_difficulty)

        print("Block successfully caught and added to the PawChain!")
        self.the_long_yarn.append(new_catch)
        self.treats_in_bowl = []

    def add_treat_to_bowl(self, transaction: PawTransaction) -> None:
        """
        Adds a new treat share to the bowl of pending treats.

        This is equivalent to adding a transaction to the pending pool.

        Args:
            transaction: The PawTransaction to add.
        """
        if not transaction.from_cat_tag or not transaction.to_cat_tag:
            raise Exception("Treat must have a sender and a receiver Cat Tag.")
        if not transaction.is_paw_print_valid():
            raise Exception("Cannot add a treat with an invalid paw print.")
        if transaction.catnip_amount <= 0:
            raise Exception("Catnip amount must be positive.")

        catnip_balance = self.get_catnip_balance(transaction.from_cat_tag)
        if catnip_balance < transaction.catnip_amount:
            raise Exception("Not enough Catnip in the stash!")

        # Prevent overspending from the bowl
        pending_treats_for_cat = [
            t for t in self.treats_in_bowl if t.from_cat_tag == transaction.from_cat_tag
        ]
        total_pending_catnip = sum(t.catnip_amount for t in pending_treats_for_cat)
        if total_pending_catnip + transaction.catnip_amount > catnip_balance:
            raise Exception("Pending treats exceed Catnip stash balance.")

        self.treats_in_bowl.append(transaction)
        print(f"New treat added to bowl: {transaction}")

    def get_catnip_balance(self, cat_tag: str) -> float:
        """
        Calculates the total Catnip stash for a given Cat Tag.

        This iterates through the entire chain to determine a wallet's balance.

        Args:
            cat_tag: The public Cat Tag (wallet address) to check.
        """
        catnip_stash = 0.0
        for block in self.the_long_yarn:
            for treat in block.shared_treats:
                if treat.from_cat_tag == cat_tag:
                    catnip_stash -= treat.catnip_amount
                if treat.to_cat_tag == cat_tag:
                    catnip_stash += treat.catnip_amount
        return catnip_stash

    def is_yarn_unbroken(self) -> bool:
        """
        Checks the integrity of the entire long yarn (chain).

        This validates the entire blockchain to ensure no blocks or
        transactions have been tampered with.
        """
        for i in range(1, len(self.the_long_yarn)):
            current_catch = self.the_long_yarn[i]
            previous_catch = self.the_long_yarn[i - 1]

            if current_catch.scratch_mark != current_catch.calculate_scratch_mark():
                print(f"Scratch mark is wrong on block: {current_catch.scratch_mark}")
                return False
            if current_catch.previous_scratch_mark != previous_catch.scratch_mark:
                print("The yarn is broken! Previous scratch mark doesn't match.")
                return False
            if not current_catch.has_good_treats():
                print(f"Block has fake treats: {current_catch.scratch_mark}")
                return False

        if (
            self.the_long_yarn[0].scratch_mark
            != self.the_long_yarn[0].calculate_scratch_mark()
        ):
            print("The First Meow has been tampered with!")
            return False

        return True
