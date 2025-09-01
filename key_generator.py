from typing import cast
from ecdsa import SigningKey, VerifyingKey, SECP256k1


def generate_cat_identity() -> tuple[str, str]:
    """
    Generates a new cat identity.

    This creates a new Secret Purr (private key) and a public Cat Tag (public key).
    """
    secret_purr: SigningKey = SigningKey.generate(curve=SECP256k1)
    cat_tag: VerifyingKey = cast(VerifyingKey, secret_purr.get_verifying_key())

    secret_purr_hex: str = secret_purr.to_string().hex()
    cat_tag_hex: str = cat_tag.to_string().hex()

    print(
        "\nYour Cat Tag (publicly shareable wallet address!)\n",
        cat_tag_hex,
    )
    print(
        "\nYour Secret Purr (private key - keep this secret!)\n",
        secret_purr_hex,
    )
    return (secret_purr_hex, cat_tag_hex)


if __name__ == "__main__":
    generate_cat_identity()
